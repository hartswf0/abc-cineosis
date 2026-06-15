import re
import os

branch_md_path = "/Users/gaia/ABC-CINEOSIS/HAPPY HORSE/BRANCH/branch-01.md"
output_dir = "/Users/gaia/ABC-CINEOSIS/HAPPY HORSE/BRANCH"

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

def get_horse_commands(hx, hy, val_body, val_high, val_dark, frame_idx):
    head_y = hy - 6 + (frame_idx % 2) # head bobbing
    commands = [
        # Body core layers
        f"PNT {hx + 10} {hy} 14 7 {val_body}",
        f"PNT {hx + 12} {hy + 1} 10 5 {val_high}",
        f"PNT {hx + 8} {hy + 2} 4 4 {val_dark}",
        # Neck base and arch
        f"PNT {hx + 13} {hy - 4} 4 5 {val_body}",
        f"PNT {hx + 14} {hy - 3} 2 3 {val_high}",
        # Head and muzzle
        f"PNT {hx + 17} {head_y} 5 4 {val_body}",
        f"PNT {hx + 19} {head_y + 1} 2 2 {val_high}",
        # Eye glint
        f"PNT {hx + 18} {head_y + 1} 1 1 {val_high}",
        # Ears
        f"PNT {hx + 15} {head_y - 3} 1 3 {val_body}",
        f"PNT {hx + 16} {head_y - 3} 1 3 {val_high}",
    ]
    # Legs (moving animation)
    if frame_idx == 0:
        commands.extend([
            f"LIN {hx + 11} {hy + 7} {hx + 11} {hy + 14} {val_body}",
            f"LIN {hx + 15} {hy + 7} {hx + 15} {hy + 14} {val_high}",
            f"LIN {hx + 19} {hy + 7} {hx + 18} {hy + 14} {val_body}",
            f"LIN {hx + 22} {hy + 7} {hx + 23} {hy + 14} {val_high}",
        ])
    elif frame_idx == 1:
        commands.extend([
            f"LIN {hx + 11} {hy + 7} {hx + 13} {hy + 14} {val_body}",
            f"LIN {hx + 15} {hy + 7} {hx + 13} {hy + 14} {val_high}",
            f"LIN {hx + 19} {hy + 7} {hx + 20} {hy + 14} {val_body}",
            f"LIN {hx + 22} {hy + 7} {hx + 21} {hy + 14} {val_high}",
        ])
    else:
        commands.extend([
            f"LIN {hx + 11} {hy + 7} {hx + 9} {hy + 14} {val_body}",
            f"LIN {hx + 15} {hy + 7} {hx + 17} {hy + 14} {val_high}",
            f"LIN {hx + 19} {hy + 7} {hx + 19} {hy + 14} {val_body}",
            f"LIN {hx + 22} {hy + 7} {hx + 22} {hy + 14} {val_high}",
        ])
    # Tail
    tail_y = hy + (frame_idx % 2)
    commands.append(f"LIN {hx + 10} {hy + 2} {hx + 6} {tail_y + 8} {val_dark}")
    return commands

def get_human_commands(px, py, val_human, frame_idx):
    head_y = py - 5 + (frame_idx % 2)
    commands = [
        f"PNT {px} {py} 4 8 {val_human}", # torso
        f"PNT {px+1} {head_y} 2 2 {val_human+1 if val_human < 7 else 7}", # head
    ]
    # Legs (walking)
    if frame_idx % 2 == 0:
        commands.extend([
            f"LIN {px+1} {py+8} {px-1} {py+14} {val_human}",
            f"LIN {px+2} {py+8} {px+4} {py+14} {val_human}",
        ])
    else:
        commands.extend([
            f"LIN {px+1} {py+8} {px+2} {py+14} {val_human}",
            f"LIN {px+2} {py+8} {px+1} {py+14} {val_human}",
        ])
    # Arm
    commands.append(f"LIN {px-1} {py+1} {px-2} {py+5} {val_human}")
    return commands

def get_device_commands(dx, dy, val_device, frame_idx):
    commands = [
        f"C Drawing device screen",
        f"PNT {dx} {dy} 20 14 {val_device}", # bezel
        f"PNT {dx+2} {dy+2} 16 10 0", # screen face (black)
    ]
    # Blinking text lines or waveforms
    if frame_idx % 2 == 0:
        commands.append(f"LIN {dx+4} {dy+4} {dx+12} {dy+4} {val_device+1 if val_device < 7 else 7}")
        commands.append(f"LIN {dx+4} {dy+7} {dx+10} {dy+7} {val_device+1 if val_device < 7 else 7}")
    else:
        commands.append(f"LIN {dx+4} {dy+4} {dx+10} {dy+4} {val_device+1 if val_device < 7 else 7}")
        commands.append(f"LIN {dx+4} {dy+7} {dx+14} {dy+7} {val_device+1 if val_device < 7 else 7}")
    # Status LED blinking
    led_val = 7 if frame_idx % 2 == 0 else 2
    commands.append(f"PNT {dx+17} {dy+12} 1 1 {led_val}")
    return commands

def get_server_commands(sx, sy, val_server, frame_idx):
    commands = [
        f"PNT {sx} {sy} 14 36 {val_server}", # rack unit
        f"LIN {sx} {sy+6} {sx+13} {sy+6} 0",
        f"LIN {sx} {sy+12} {sx+13} {sy+12} 0",
        f"LIN {sx} {sy+18} {sx+13} {sy+18} 0",
        f"LIN {sx} {sy+24} {sx+13} {sy+24} 0",
    ]
    # Blinking lights
    for ly in range(sy+3, sy+36, 6):
        l_val = 7 if (ly + frame_idx) % 2 == 0 else 1
        commands.append(f"PNT {sx+2} {ly} 1 1 {l_val}")
    return commands

def get_paper_commands(px, py, val_paper, frame_idx):
    offset_y = py + (frame_idx % 2)
    return [
        f"C Floating paper sheet",
        f"PNT {px} {offset_y} 10 12 {val_paper}",
        f"PNT {px+1} {offset_y+1} 8 10 7",
        f"LIN {px+2} {offset_y+3} {px+6} {offset_y+3} 2",
        f"LIN {px+2} {offset_y+6} {px+5} {offset_y+6} 2",
    ]

def generate_beflix_code(beat, temporal, category, description):
    desc = description.lower()
    
    val_pasture = 3 if temporal == "past" else 2
    val_grass = 4 if temporal == "past" else 3
    val_horse_body = 5 if temporal == "past" else 6
    val_horse_high = 6 if temporal == "past" else 7
    val_horse_dark = 4 if temporal == "past" else 5
    val_human = 5 if temporal == "past" else 6
    val_cart = 4 if temporal == "past" else 5
    val_device = 4 if temporal == "past" else 5
    val_server = 4 if temporal == "past" else 5
    val_building = 3 if temporal == "past" else 4
    val_paper = 5 if temporal == "past" else 6
    
    frames_code = []
    
    # Generate 3 frames of animation
    for frame_idx in range(3):
        frame_commands = []
        frame_commands.append(f"C --- FRAME {frame_idx + 1} ---")
        
        # Clear screen first
        if temporal == "future" and "grid" in desc:
            frame_commands.append("CLR 0")
            frame_commands.append("C Grid lines underlay")
            for gx in range(0, 128, 16):
                frame_commands.append(f"LIN {gx} 0 {gx} 95 1")
            for gy in range(0, 96, 16):
                frame_commands.append(f"LIN 0 {gy} 127 {gy} 1")
        elif temporal == "future":
            frame_commands.append("CLR 0")
            if "sensor" in desc or "light" in desc or "biometric" in desc:
                frame_commands.append(f"C Sensor interface bounds")
                frame_commands.append(f"LIN 2 2 125 2 1")
                frame_commands.append(f"LIN 125 2 125 93 1")
                frame_commands.append(f"LIN 125 93 2 93 1")
                frame_commands.append(f"LIN 2 93 2 2 1")
        else:
            frame_commands.append("CLR 0")
            
        # Draw background pasture / road
        if any(w in desc for w in ["pasture", "field", "road", "track", "ground", "grass", "stable", "stable wall", "barn"]):
            frame_commands.append("C Pasture background")
            frame_commands.append(f"LIN 0 54 127 54 {val_pasture}")
            frame_commands.append(f"PNT 0 55 128 20 {val_pasture-1 if val_pasture > 1 else val_pasture}")
            
        # Draw wagon tracks/road lines
        if "road" in desc or "tracks" in desc or "ruts" in desc:
            frame_commands.append("C Road ruts")
            frame_commands.append(f"LIN 10 55 30 95 {val_pasture}")
            frame_commands.append(f"LIN 18 55 42 95 {val_pasture}")
            frame_commands.append(f"LIN 80 55 90 95 {val_pasture}")
            frame_commands.append(f"LIN 88 55 102 95 {val_pasture}")
            
        # Draw grass
        if "grass" in desc or "pasture" in desc or "field" in desc:
            frame_commands.append("C Grass stipples")
            for gx in range(4, 128, 12):
                gx_animated = gx + (frame_idx % 3)
                frame_commands.append(f"LIN {gx_animated} 65 {gx_animated} 62 {val_grass}")
                
        # Draw fence or grid lines
        if any(w in desc for w in ["fence", "grid", "tripwire", "tripwires", "lines", "mesh"]):
            frame_commands.append("C Fence/Grid rails")
            for fx in range(12, 128, 24):
                frame_commands.append(f"PNT {fx} 38 2 20 {val_pasture+1 if val_pasture < 7 else 7}")
            frame_commands.append(f"LIN 0 42 127 42 {val_pasture+1 if val_pasture < 7 else 7}")
            frame_commands.append(f"LIN 0 50 127 50 {val_pasture+1 if val_pasture < 7 else 7}")
            
        # Draw building / stable / monastery / courthouse
        if any(w in desc for w in ["stable", "barn", "monastery", "house", "building", "courthouse", "classroom", "clinic", "office", "museum"]):
            bx = 95
            by = 30
            frame_commands.append(f"C Building silhouette")
            frame_commands.append(f"PNT {bx} {by} 20 25 {val_building}")
            frame_commands.append(f"LIN {bx} {by} {bx+10} {by-8} {val_building+1 if val_building < 7 else 7}")
            frame_commands.append(f"LIN {bx+10} {by-8} {bx+20} {by} {val_building+1 if val_building < 7 else 7}")
            frame_commands.append(f"PNT {bx+6} {by+12} 6 13 0") # Door
            
        # Draw server rack
        if any(w in desc for w in ["server", "servers", "datacenter", "drives"]):
            frame_commands.append(f"C Server units")
            frame_commands.extend(get_server_commands(20, 20, val_server, frame_idx))
            frame_commands.extend(get_server_commands(50, 20, val_server, frame_idx))
            
        # Draw cart or wagon
        if any(w in desc for w in ["cart", "wagon", "cart-line", "harness lines"]):
            cx = 40 + (frame_idx * 4) # rolling cart motion
            frame_commands.append(f"C Rolling cart")
            frame_commands.append(f"PNT {cx} 52 24 8 {val_cart}")
            frame_commands.append(f"LIN {cx+4} 58 {cx+4} 62 {val_cart+1 if val_cart < 7 else 7}")
            frame_commands.append(f"LIN {cx+18} 58 {cx+18} 62 {val_cart+1 if val_cart < 7 else 7}")
            if frame_idx % 2 == 0:
                frame_commands.append(f"LIN {cx+2} 60 {cx+6} 60 {val_cart+1 if val_cart < 7 else 7}")
                frame_commands.append(f"LIN {cx+16} 60 {cx+20} 60 {val_cart+1 if val_cart < 7 else 7}")
            else:
                frame_commands.append(f"LIN {cx+4} 58 {cx+4} 62 {val_cart+1 if val_cart < 7 else 7}")
                frame_commands.append(f"LIN {cx+18} 58 {cx+18} 62 {val_cart+1 if val_cart < 7 else 7}")
                
        # Draw horse / animal / calypso
        if any(w in desc for w in ["horse", "calypso", "animal"]):
            if any(w in desc for w in ["eye", "eye ", "nostril", "mouth", "teeth", "flank", "jaw", "shoulder"]):
                frame_commands.append("C Extreme close up of horse details")
                frame_commands.append("PNT 40 25 48 48 5")
                frame_commands.append("PNT 52 35 24 24 1")
                blink_val = 7 if frame_idx % 2 == 0 else 3
                frame_commands.append(f"PNT 58 40 6 6 {blink_val}")
                jaw_y = 65 + (frame_idx % 2)
                frame_commands.append(f"LIN 40 {jaw_y} 88 {jaw_y} 2")
            else:
                hx = 15
                hy = 40
                if any(w in desc for w in ["cart", "wagon"]):
                    hx = 15 + (frame_idx * 4)
                frame_commands.append(f"C Animated horse figure")
                frame_commands.extend(get_horse_commands(hx, hy, val_horse_body, val_horse_high, val_horse_dark, frame_idx))
                
        # Draw human / Dario
        if any(w in desc for w in ["dario", "man", "worker", "person", "child", "scribe", "librarian", "official", "regulator"]):
            px = 85
            py = 40
            frame_commands.append(f"C Animated human figure")
            frame_commands.extend(get_human_commands(px, py, val_human, frame_idx))
            
        # Draw device / screen / laptop / phone / monitor / dashboard
        if any(w in desc for w in ["laptop", "screen", "phone", "device", "monitor", "dashboard", "panel", "display"]):
            dx = 75 if not any(w in desc for w in ["laptop", "phone"]) else 50
            dy = 35
            frame_commands.extend(get_device_commands(dx, dy, val_device, frame_idx))
            
        # Draw document / paper
        if any(w in desc for w in ["document", "paper", "book", "bible", "manuscript", "lyrics", "invoices", "sheets", "royalty", "statement"]):
            px = 55
            py = 40
            frame_commands.extend(get_paper_commands(px, py, val_paper, frame_idx))
            
        # Draw flying/moving particles or sensor blinks
        if any(w in desc for w in ["flies", "dust", "sensor", "light", "spark", "markers"]):
            frame_commands.append("C Scattered particle noise")
            for px in range(10, 110, 20):
                py = (px * 3 + frame_idx * 15) % 80 + 10
                frame_commands.append(f"PNT {px} {py} 1 1 6")
                
        # Hold frame
        hold_time = 6 if frame_idx < 2 else 12
        frame_commands.append(f"REC {hold_time}")
        frame_commands.append("C")
        
        frames_code.append("\n".join(frame_commands))
        
    return "\n\n".join(frames_code)

def main():
    print(f"Reading master branch structure: {branch_md_path}")
    if not os.path.exists(branch_md_path):
        print(f"Error: {branch_md_path} does not exist!")
        return

    with open(branch_md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    beat_num = 0
    layer = None # "past", "present", "future"
    current_cat = None
    current_desc = []
    cells = []

    beat_pat = re.compile(r'^#\s+BEAT\s+(\d+)')
    layer_pat = re.compile(r'^##\s+(PAST_IMAGES|PRESENT_IMAGES|FUTURE_IMAGES)')
    cat_pat = re.compile(r'^###\s+(\d)\.\s*([a-zA-Z\-_]+)')

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
        
        # Check Beat
        bm = beat_pat.match(line_str)
        if bm:
            save_current_cell()
            beat_num = int(bm.group(1))
            layer = None
            current_cat = None
            continue
            
        # Check Layer
        lm = layer_pat.match(line_str)
        if lm:
            save_current_cell()
            layer_text = lm.group(1).lower()
            if "past" in layer_text: layer = "past"
            elif "present" in layer_text: layer = "present"
            elif "future" in layer_text: layer = "future"
            current_cat = None
            continue
            
        # Check Category
        cm = cat_pat.match(line_str)
        if cm:
            save_current_cell()
            cat_num = int(cm.group(1))
            raw_cat_name = cm.group(2)
            current_cat = get_category_id(raw_cat_name)
            continue
            
        # If inside a cell and we have non-empty line
        if current_cat is not None and line_str:
            if not line_str.startswith("---") and not line_str.startswith("#"):
                current_desc.append(line_str)

    # Save final cell
    save_current_cell()

    print(f"Parsed {len(cells)} cells from branch-01.md")

    # Generate 252 branch BEFLIX files
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for cell in cells:
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
            f"C  ============================================================\n\n"
        )
        
        beflix_code = generate_beflix_code(beat, temporal, category, desc)
        
        with open(filepath, 'w', encoding='utf-8') as out_f:
            out_f.write(header + beflix_code + "\n")
            
    print("Successfully generated all 252 branching BEFLIX files!")

if __name__ == "__main__":
    main()
