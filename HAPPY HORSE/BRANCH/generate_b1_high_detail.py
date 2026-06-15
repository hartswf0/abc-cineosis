import os
import re

base_fable_path = "/Users/gaia/ABC-CINEOSIS/HAPPY HORSE/BRANCH/a-happy-horse-base-fable.md"
output_dir = "/Users/gaia/ABC-CINEOSIS/HAPPY HORSE/BRANCH"

def parse_base_fable_horse():
    """
    Parses a-happy-horse-base-fable.md to extract the detailed horse drawing commands
    from Frame 9, Frame 10, and Frame 11 (the standing/flicking loop).
    """
    if not os.path.exists(base_fable_path):
        print(f"Error: {base_fable_path} not found!")
        return None

    with open(base_fable_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by frames
    frame_blocks = re.split(r'C ===== FRAME \d+:', content)
    
    # We want Frame 9, 10, 11
    # Note that splitting by 'C ===== FRAME \d+:' will put the contents of Frame 9 in block 9, etc.
    frames_data = {}
    
    for idx, block in enumerate(frame_blocks):
        if idx < 1: continue
        # Find which frame this block represents by reading the index from the splits
        # Let's search inside the block or use sequence mapping
        # Let's clean the block lines
        lines = block.split('\n')
        
        # Determine frame index by comment or pattern
        # Since the blocks split sequentially:
        # block 1 is Frame 1, block 9 is Frame 9, etc.
        if idx in [9, 10, 11]:
            frames_data[idx] = clean_horse_lines(lines)

    return frames_data

def clean_horse_lines(lines, base_x=44, base_y=84):
    """
    Excludes environment commands and relativizes horse coordinates based on anchor (base_x, base_y).
    """
    horse_cmds = []
    for line in lines:
        line_str = line.strip()
        if not line_str: continue
        if line_str.startswith('C') or line_str.startswith('REC') or line_str.startswith('CLR') or line_str.startswith('SHF'):
            continue
        
        tokens = line_str.split()
        if not tokens: continue
        cmd = tokens[0]
        
        if cmd == 'PNT':
            try:
                x, y, w, h, c = map(int, tokens[1:])
                # Exclude sky, ground baseline, sun, and ground shadows
                if x == 0 and w == 128: continue
                if x >= 102 and y <= 12: continue
                if y >= 84: continue
                # Relativize
                rx = x - base_x
                ry = y - base_y
                horse_cmds.append(('PNT', rx, ry, w, h, c))
            except ValueError:
                continue
        elif cmd == 'LIN':
            try:
                x1, y1, x2, y2, c = map(int, tokens[1:])
                # Exclude horizon baseline, grass lines, sky lines, and hills
                if x1 == 0 and x2 == 127: continue
                if y1 >= 84 or y2 >= 84: continue
                if y1 <= 12 and y2 <= 12: continue
                # Hill checks
                if x1 == 0 and y1 == 58: continue
                if x1 == 22 and y1 == 52: continue
                if x1 == 102 and y1 == 55: continue
                # Relativize
                rx1 = x1 - base_x
                ry1 = y1 - base_y
                rx2 = x2 - base_x
                ry2 = y2 - base_y
                horse_cmds.append(('LIN', rx1, ry1, rx2, ry2, c))
            except ValueError:
                continue
    return horse_cmds

def render_horse(horse_cmds, hx, hy, pose='standing', frame_idx=0):
    """
    Translates relative horse commands to the target hx, hy position, 
    applying pose modifications (like grazing head shifts).
    """
    rendered = []
    for cmd_tuple in horse_cmds:
        cmd = cmd_tuple[0]
        if cmd == 'PNT':
            _, rx, ry, w, h, c = cmd_tuple
            # Grazing pose: shift head/neck downwards and slightly left
            if pose == 'grazing':
                # Bounding box of head and neck in relative coordinates
                # Head/neck is generally x < 2 (relative to base_x=44) and y < -25 (relative to base_y=84)
                if rx <= 2 and ry <= -25:
                    # Shift head lower
                    tx = hx + rx - 2 + (frame_idx % 2)
                    ty = hy + ry + 25 + (frame_idx % 3)
                elif rx <= 10 and ry <= -15:
                    # Shift neck down
                    tx = hx + rx - 1
                    ty = hy + ry + 15
                else:
                    tx = hx + rx
                    ty = hy + ry
            else:
                # Normal standing/flicking
                tx = hx + rx
                ty = hy + ry
            
            # Clip coordinates
            tx = max(0, min(127, tx))
            ty = max(0, min(95, ty))
            rendered.append(f"PNT {tx} {ty} {w} {h} {c}")
            
        elif cmd == 'LIN':
            _, rx1, ry1, rx2, ry2, c = cmd_tuple
            if pose == 'grazing':
                # Relocate head/neck lines
                if rx1 <= 2 and ry1 <= -25:
                    tx1 = hx + rx1 - 2 + (frame_idx % 2)
                    ty1 = hy + ry1 + 25 + (frame_idx % 3)
                elif rx1 <= 10 and ry1 <= -15:
                    tx1 = hx + rx1 - 1
                    ty1 = hy + ry1 + 15
                else:
                    tx1 = hx + rx1
                    ty1 = hy + ry1
                    
                if rx2 <= 2 and ry2 <= -25:
                    tx2 = hx + rx2 - 2 + (frame_idx % 2)
                    ty2 = hy + ry2 + 25 + (frame_idx % 3)
                elif rx2 <= 10 and ry2 <= -15:
                    tx2 = hx + rx2 - 1
                    ty2 = hy + ry2 + 15
                else:
                    tx2 = hx + rx2
                    ty2 = hy + ry2
            else:
                tx1 = hx + rx1
                ty1 = hy + ry1
                tx2 = hx + rx2
                ty2 = hy + ry2
                
            tx1 = max(0, min(127, tx1))
            ty1 = max(0, min(95, ty1))
            tx2 = max(0, min(127, tx2))
            ty2 = max(0, min(95, ty2))
            rendered.append(f"LIN {tx1} {ty1} {tx2} {ty2} {c}")
            
    # If grazing, draw a neck connection line to bridge any gaps
    if pose == 'grazing':
        # Connection from shoulder to head
        cx1 = max(0, min(127, hx + 2))
        cy1 = max(0, min(95, hy - 32))
        cx2 = max(0, min(127, hx - 12))
        cy2 = max(0, min(95, hy - 10))
        rendered.append(f"LIN {cx1} {cy1} {cx2} {cy2} 4")
        rendered.append(f"LIN {cx1+1} {cy1} {cx2+1} {cy2} 5")
        
    return rendered

def generate_scene_frames(temporal, category, desc, horse_templates):
    """
    Generates the BEFLIX commands for the 3 frames of animation,
    tailored to the temporal regime, category and description.
    """
    frames = []
    
    # Establish shared background environment stipples
    is_dusk = (temporal == "future")
    val_sky = 1 if is_dusk else 2
    val_hills = 2 if is_dusk else 3
    val_ground = 3 if is_dusk else 4
    val_grass = 4 if is_dusk else 5
    
    # Map scene requirements based on category and description keywords
    has_horse = not any(w in desc.lower() for w in ["hitching post", "stable wall", "empty hallway", "waveform traces"])
    is_closeup = any(w in desc.lower() for w in ["eye", "mouth", "teeth", "nostril", "jaw", "fibers breaking"])
    is_grazing = any(w in desc.lower() for w in ["grazes", "grazing", "chewing", "tears it", "lowers her head", "wooden feed trough", "grass fibers"])
    
    for f_idx in range(3):
        cmds = []
        cmds.append(f"C --- FRAME {f_idx + 1} ---")
        cmds.append("CLR 0")
        
        # 1. Environment Underlay
        if not is_closeup:
            cmds.append("C Environment Backdrop")
            cmds.append(f"PNT 0 0 128 32 {val_sky}") # sky
            cmds.append(f"LIN 0 58 22 52 {val_hills}") # hills
            cmds.append(f"LIN 22 52 44 58 {val_hills}")
            cmds.append(f"LIN 102 55 127 50 {val_hills}")
            cmds.append(f"LIN 0 84 127 84 {val_ground}") # ground plane
            
            # Sun or sensor grid
            if temporal == "past":
                cmds.append("C Late afternoon sun")
                cmds.append("PNT 108 6 9 9 1")
                cmds.append("PNT 110 8 5 5 2")
            elif temporal == "future":
                cmds.append("C Future sensor layout underlay")
                cmds.append("LIN 2 2 125 2 1")
                cmds.append("LIN 125 2 125 93 1")
                cmds.append("LIN 125 93 2 93 1")
                cmds.append("LIN 2 93 2 2 1")
                
            # Ground details
            if "road" in desc.lower() or "tracks" in desc.lower() or "wagon tracks" in desc.lower():
                cmds.append("C Wagon tracks / road ruts")
                cmds.append(f"LIN 10 84 48 95 {val_ground - 1}")
                cmds.append(f"LIN 18 84 54 95 {val_ground - 1}")
                
            # Grass stippling
            if "grass" in desc.lower() or "pasture" in desc.lower() or "field" in desc.lower():
                cmds.append("C Grass elements")
                for gx in range(6, 120, 18):
                    cmds.append(f"LIN {gx + f_idx*2} 86 {gx + f_idx*2} 89 {val_grass}")
        
        # 2. Main Narrative Subject Rendering
        if has_horse and not is_closeup:
            cmds.append("C High-detail horse render")
            template_idx = 9 + f_idx
            template = horse_templates[template_idx]
            
            # Determine placement scale and position
            if "small in the frame" in desc.lower() or "small" in desc.lower():
                # Micro-scale horse (procedural simple stipple)
                cmds.append("C Micro scale profile")
                cmds.append(f"PNT 40 55 12 6 5")
                cmds.append(f"LIN 42 61 42 66 5")
                cmds.append(f"LIN 48 61 48 66 5")
                cmds.append(f"LIN 51 55 53 52 6")
            else:
                # Macro-scale horse (use fable coordinates)
                pose = 'grazing' if is_grazing else 'standing'
                cmds.extend(render_horse(template, hx=44, hy=84, pose=pose, frame_idx=f_idx))
                
        # 3. Handle Special Close-ups
        if is_closeup:
            if "eye" in desc.lower():
                cmds.append("C Close up of horse eye reflecting lantern glow")
                cmds.append("PNT 20 20 88 56 4") # eye lids
                cmds.append("PNT 40 28 48 40 1") # eyeball
                cmds.append("PNT 56 40 16 16 7") # pupil/reflection
                # Lantern blinking reflection
                glow = 7 if f_idx % 2 == 0 else 2
                cmds.append(f"PNT 62 44 4 6 {glow}")
            elif "mouth" in desc.lower() or "jaw" in desc.lower() or "chewing" in desc.lower():
                cmds.append("C Close up of chewing muzzle and jaw")
                cmds.append("PNT 30 20 68 56 4") # muzzle
                chew_y = 52 + (f_idx % 2)
                cmds.append(f"LIN 32 {chew_y} 90 {chew_y} 1") # chewing mouth line
                cmds.append(f"LIN 35 {chew_y + 4} 45 {chew_y + 8} 3") # grass sticking out
                cmds.append(f"LIN 40 {chew_y + 4} 52 {chew_y + 6} 2")
            elif "fibers breaking" in desc.lower() or "teeth" in desc.lower():
                cmds.append("C Grass fibers tearing between teeth")
                cmds.append("PNT 35 15 58 12 5") # upper tooth
                cmds.append("PNT 35 60 58 12 5") # lower tooth
                # Grass breaking loop
                if f_idx == 0:
                    cmds.append("LIN 20 40 108 40 3") # intact blade
                elif f_idx == 1:
                    cmds.append("LIN 20 40 50 40 3") # tearing
                    cmds.append("LIN 68 40 108 40 3")
                    cmds.append("PNT 54 40 6 3 1")
                else:
                    cmds.append("LIN 20 40 45 42 3") # broken
                    cmds.append("LIN 75 38 108 40 3")
        
        # 4. Handle Specific Scene Overlays
        # Pasture road ears
        if "village framed between animal ears" in desc.lower():
            cmds.append("C Horse ears framing road view")
            # Left ear
            cmds.append("PNT 10 16 14 36 4")
            cmds.append("LIN 10 16 22 52 6")
            # Right ear
            cmds.append("PNT 104 16 14 36 4")
            cmds.append("LIN 104 16 92 52 6")
            
        # Wooden feed trough
        if "wooden feed trough" in desc.lower():
            cmds.append("C Wooden feed trough")
            cmds.append("PNT 10 65 24 16 3")
            cmds.append("LIN 10 65 34 65 6")
            cmds.append("LIN 10 81 34 81 6")
            
        # Empty hitching post
        if "hitching post" in desc.lower():
            cmds.append("C Empty hitching post")
            cmds.append("PNT 32 20 8 64 4")
            cmds.append("LIN 32 20 40 20 5")
            cmds.append("LIN 38 40 48 70 3") # rope
            
        # Stable wall
        if "stable wall" in desc.lower() or "hanging tack" in desc.lower():
            cmds.append("C stable wall details")
            cmds.append("LIN 0 20 127 20 3")
            cmds.append("LIN 0 40 127 40 3")
            cmds.append("LIN 0 60 127 60 3")
            cmds.append("LIN 40 30 46 36 6") # hanging ring
            cmds.append("PNT 35 48 16 18 3") # feed bucket
            
        # Rain puddle reflecting grazing horse
        if "rain puddle reflects a horse" in desc.lower():
            cmds.append("C Puddle reflecting horse")
            cmds.append("PNT 10 65 64 24 2") # puddle surface
            # upside down horse reflection (low opacity)
            cmds.append("PNT 20 75 14 6 1")
            
        # Photo frame in drawer
        if "family photograph" in desc.lower():
            cmds.append("C Photograph frame inside drawer")
            cmds.append("LIN 0 76 127 76 3") # drawer partition
            cmds.append("PNT 20 20 88 50 6") # photopaper
            cmds.append("PNT 32 26 64 38 4") # image details
            
        # Dario sitting
        if "dario sits" in desc.lower():
            cmds.append("C Seated Dario silhouette")
            cmds.append("PNT 96 50 8 16 4")
            cmds.append("PNT 98 44 4 6 5")
            
        # Ghostly outlines of old workhorses
        if "ghostly outlines" in desc.lower():
            cmds.append("C Ghostly workhorse outline overlay")
            cmds.append("LIN 30 40 60 40 1")
            cmds.append("LIN 40 40 28 56 1")
            
        # Smart farm fence sensors
        if "sensors hidden in fence posts" in desc.lower() or "fence post" in desc.lower():
            cmds.append("C Blinking sensor indicator")
            led_c = 7 if f_idx % 2 == 0 else 1
            cmds.append(f"PNT 78 32 2 2 {led_c}")
            
        # Automated gate sliding open
        if "automated gate" in desc.lower():
            cmds.append("C Sliding gate rails")
            gate_x = 70 + f_idx * 12
            cmds.append(f"LIN {gate_x} 20 {gate_x} 70 5")
            cmds.append(f"LIN {gate_x+8} 20 {gate_x+8} 70 5")
            
        # Solar panel
        if "solar panel" in desc.lower():
            cmds.append("C Solar panel grid lines")
            cmds.append("PNT 40 25 56 36 3")
            cmds.append("LIN 40 25 96 61 6")
            cmds.append("LIN 96 25 40 61 6")
            
        # Museum screen
        if "museum screen" in desc.lower():
            cmds.append("C Museum screen frame")
            cmds.append("PNT 24 15 80 48 3")
            # Visitor silhouette passing in front
            vx = 10 + f_idx * 32
            cmds.append(f"PNT {vx} 64 8 20 1")
            cmds.append(f"PNT {vx+2} 60 4 4 1")
            
        # Hold frame
        hold_time = 6 if f_idx < 2 else 12
        cmds.append(f"REC {hold_time}")
        cmds.append("C")
        
        frames.append("\n".join(cmds))
        
    return "\n\n".join(frames)

def main():
    print("Parsing high-detail horse templates from base fable...")
    horse_templates = parse_base_fable_horse()
    if not horse_templates:
        print("Parsing failed. Check a-happy-horse-base-fable.md.")
        return

    print("Reading branch-01.md blueprint...")
    branch_md_path = "/Users/gaia/ABC-CINEOSIS/HAPPY HORSE/BRANCH/branch-01.md"
    if not os.path.exists(branch_md_path):
        print(f"Error: {branch_md_path} does not exist!")
        return

    with open(branch_md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    beat_num = 0
    layer = None
    current_cat = None
    current_desc = []
    cells = []

    beat_pat = re.compile(r'^#\s+BEAT\s+(\d+)')
    layer_pat = re.compile(r'^##\s+(PAST_IMAGES|PRESENT_IMAGES|FUTURE_IMAGES)')
    cat_pat = re.compile(r'^###\s+(\d)\.\s*([a-zA-Z\-_]+)')

    def get_category_id(header_text):
        h = header_text.lower()
        if "perception" in h: return "perception"
        if "action" in h: return "action"
        if "affection" in h: return "affection"
        if "opsign" in h: return "opsign"
        if "sonsign" in h: return "sonsign"
        if "crystal" in h: return "crystal"
        if "recollection" in h: return "recollection"
        return None

    def save_current_cell():
        nonlocal current_cat, current_desc, beat_num, layer
        if current_cat and current_desc:
            desc_text = " ".join(current_desc).strip()
            desc_text = desc_text.strip('"').strip("'")
            desc_text = re.sub(r'\s*--ar\s+\d+:\d+\s*$', '', desc_text)
            cells.append({
                "beat": beat_num,
                "temporal": layer,
                "category": current_cat,
                "description": desc_text
            })
            current_desc = []

    for line in lines:
        line_str = line.strip()
        bm = beat_pat.match(line_str)
        if bm:
            save_current_cell()
            beat_num = int(bm.group(1))
            layer = None
            current_cat = None
            continue
            
        lm = layer_pat.match(line_str)
        if lm:
            save_current_cell()
            layer_text = lm.group(1).lower()
            if "past" in layer_text: layer = "past"
            elif "present" in layer_text: layer = "present"
            elif "future" in layer_text: layer = "future"
            current_cat = None
            continue
            
        cm = cat_pat.match(line_str)
        if cm:
            save_current_cell()
            current_cat = get_category_id(cm.group(2))
            continue
            
        if current_cat is not None and line_str:
            if not line_str.startswith("---") and not line_str.startswith("#"):
                current_desc.append(line_str)

    save_current_cell()

    # Filter to only Beat 1 cells
    b1_cells = [c for c in cells if c["beat"] == 1]
    print(f"Extracted {len(b1_cells)} cells for Beat 1.")

    for cell in b1_cells:
        beat = cell["beat"]
        temporal = cell["temporal"]
        category = cell["category"]
        desc = cell["description"]
        
        filename = f"b{beat}_{temporal}_{category}.md"
        filepath = os.path.join(output_dir, filename)
        
        header = (
            f"C ============================================================\n"
            f"C  NARRATIVE BRANCH: b{beat}_{temporal}_{category}\n"
            f"C  TITLE: Beat {beat} / {temporal.upper()} / {category.capitalize()}-Image\n"
            f"C  DESCRIPTION: {desc}\n"
            f"C  LEVEL OF DETAIL: BASE FABLE HIGH FIDELITY STIPPLE\n"
            f"C  ============================================================\n\n"
        )
        
        beflix_code = generate_scene_frames(temporal, category, desc, horse_templates)
        
        with open(filepath, 'w', encoding='utf-8') as out_f:
            out_f.write(header + beflix_code + "\n")
            
    print("Successfully generated all 21 high-detail branch files for Beat 1!")

if __name__ == "__main__":
    main()
