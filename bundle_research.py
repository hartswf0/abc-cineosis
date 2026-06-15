import json
import os

def bundle():
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
                        print(f"Bundled: {filepath} -> {fid}")
                else:
                    print(f"Ignored/unmatched: {f}")
    
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
                    print(f"Bundled: {filepath} -> {fid}")

    # Bundle HAPPY HORSE/BRANCH directory files
    branch_dir = os.path.join("HAPPY HORSE", "BRANCH")
    if os.path.exists(branch_dir):
        files = os.listdir(branch_dir)
        for f in files:
            if f.endswith(".md"):
                fid = f.replace(".md", "")
                filepath = os.path.join(branch_dir, f)
                with open(filepath, "r", encoding="utf-8") as file:
                    data[fid] = file.read()
                    print(f"Bundled: {filepath} -> {fid}")

    # Bundle HAPPY HORSE/FORM files
    form_dir = os.path.join("HAPPY HORSE", "FORM")
    if os.path.exists(form_dir):
        files = os.listdir(form_dir)
        for f in files:
            if f.endswith(".txt") and "abc-macro" in f:
                fid = f.replace("abc-macro (", "macro").replace(").txt", "")
                filepath = os.path.join(form_dir, f)
                with open(filepath, "r", encoding="utf-8") as file:
                    data[fid] = file.read()
                    print(f"Bundled: {filepath} -> {fid}")

    # Bundle workspace root d1-d3.md files
    for d in ["d1.md", "d2.md", "d3.md"]:
        if os.path.exists(d):
            with open(d, "r", encoding="utf-8") as file:
                data[d.replace(".md", "")] = file.read()
                print(f"Bundled: {d} -> {d.replace('.md', '')}")
                
    # Bundle ABC_Cineosis_Paper.md as thesis
    if os.path.exists("ABC_Cineosis_Paper.md"):
        with open("ABC_Cineosis_Paper.md", "r", encoding="utf-8") as file:
            data["thesis"] = file.read()
            print("Bundled: ABC_Cineosis_Paper.md -> thesis")

    # Bundle deep research reports if they exist
    for r in ["deep-research-report (24).md", "deep-research-report (25).md"]:
        if os.path.exists(r):
            with open(r, "r", encoding="utf-8") as file:
                # normalize ID to report24 / report25
                rid = "report24" if "24" in r else "report25"
                data[rid] = file.read()
                print(f"Bundled: {r} -> {rid}")
                
    # Write to research_data.js
    with open("research_data.js", "w", encoding="utf-8") as out:
        out.write("// This file is auto-generated to preload markdown research paper data for offline usage under file://\n")
        out.write("window.PRELOADED_RESEARCH_REPORTS = ")
        json.dump(data, out, ensure_ascii=False, indent=2)
        out.write(";\n")
        print("Generated research_data.js successfully!")

if __name__ == "__main__":
    bundle()
