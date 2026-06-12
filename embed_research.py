import json
import os
import re

def embed():
    data = {}
    
    # Bundle RESEARCH directory files
    research_dir = "RESEARCH"
    if os.path.exists(research_dir):
        files = os.listdir(research_dir)
        for f in files:
            if f.endswith(".md"):
                fid = None
                if "History and Concepts" in f:
                    fid = "concepts"
                elif "History" in f and "Bell Labs" in f:
                    fid = "history"
                elif "Lineage" in f and "Foraging" in f:
                    fid = "foraging"
                elif "Unearthing" in f:
                    fid = "unearthing"
                elif "Lineage" in f:
                    fid = "lineage"
                elif "Film Theory" in f:
                    fid = "film-theory"
                elif "Calculus" in f:
                    fid = "calculus"
                elif "Audit Engine" in f:
                    fid = "audit-engine"
                
                if fid:
                    filepath = os.path.join(research_dir, f)
                    with open(filepath, "r", encoding="utf-8") as file:
                        data[fid] = file.read()
                        print(f"Read: {filepath} -> {fid}")
    
    # Bundle HAPPY HORSE directory files
    happy_horse_dir = "HAPPY HORSE"
    if os.path.exists(happy_horse_dir):
        files = os.listdir(happy_horse_dir)
        for f in files:
            if f.endswith(".md"):
                fid = f.replace(".md", "")
                filepath = os.path.join(happy_horse_dir, f)
                with open(filepath, "r", encoding="utf-8") as file:
                    data[fid] = file.read()
                    print(f"Read: {filepath} -> {fid}")

    # Bundle workspace root d1-d3.md files
    for d in ["d1.md", "d2.md", "d3.md"]:
        if os.path.exists(d):
            with open(d, "r", encoding="utf-8") as file:
                data[d.replace(".md", "")] = file.read()
                print(f"Read: {d} -> {d.replace('.md', '')}")
                
    # Bundle ABC_Cineosis_Paper.md as thesis
    if os.path.exists("ABC_Cineosis_Paper.md"):
        with open("ABC_Cineosis_Paper.md", "r", encoding="utf-8") as file:
            data["thesis"] = file.read()
            print("Read: ABC_Cineosis_Paper.md -> thesis")

    # Bundle deep research reports if they exist
    for r in ["deep-research-report (24).md", "deep-research-report (25).md"]:
        if os.path.exists(r):
            with open(r, "r", encoding="utf-8") as file:
                rid = "report24" if "24" in r else "report25"
                data[rid] = file.read()
                print(f"Read: {r} -> {rid}")
                
    # Read index.html
    index_path = "index.html"
    with open(index_path, "r", encoding="utf-8") as file:
        content = file.read()
        
    # JSON payload
    json_payload = json.dumps(data, ensure_ascii=False, indent=2)
    
    # Form the data script block
    data_script = f'<script id="preloaded-research-data" type="application/json">\n{json_payload}\n</script>'
    
    # Check if the script block is already in the file
    pattern = r'<script id="preloaded-research-data" type="application/json">[\s\S]*?</script>'
    if re.search(pattern, content):
        # Replace the existing block using a lambda to prevent backslash escaping issues
        content = re.sub(pattern, lambda m: data_script, content)
        print("Replaced existing preloaded-research-data script block in index.html")
    else:
        # If it doesn't exist, remove the old research_data.js script tag if present
        old_tag = '<script src="research_data.js"></script>'
        if old_tag in content:
            content = content.replace(old_tag, data_script)
            print("Replaced research_data.js script tag with embedded JSON script block in index.html")
        else:
            # Otherwise, insert before the main script tag
            # Find the first <script> tag without src
            script_match = re.search(r'<script\b[^>]*>', content)
            if script_match:
                start_idx = script_match.start()
                content = content[:start_idx] + data_script + "\n  " + content[start_idx:]
                print("Inserted embedded JSON script block before the main script tag in index.html")
            else:
                print("Error: Could not find any script tag in index.html to insert before!")
                return
                
    # Write updated index.html
    with open(index_path, "w", encoding="utf-8") as file:
        file.write(content)
    print("Embedded research data into index.html successfully!")

if __name__ == "__main__":
    embed()
