import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

CASE_DIR = BASE_DIR / "Precedent_Data" / "json_cases"
OUTPUT_DIR = BASE_DIR / "Precedent_Data" / "merged"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

output_json = OUTPUT_DIR / "highrise_precedent_database.json"
output_txt = OUTPUT_DIR / "highrise_precedent_database_for_gem.txt"

case_files = sorted(CASE_DIR.glob("case_*.json"))

cases = []
case_index = []

for file_path in case_files:
    with open(file_path, "r", encoding="utf-8") as f:
        case_data = json.load(f)

    cases.append(case_data)

    case_index.append({
        "id": case_data.get("id"),
        "project_name": case_data.get("project_name"),
        "location": case_data.get("location"),
        "year": case_data.get("year"),
        "building_type": case_data.get("building_type"),
        "main_theme": case_data.get("main_theme", []),
        "keywords": case_data.get("keywords", [])
    })

database = {
    "database_name": "High-Rise Residential Precedent Knowledge Base",
    "version": "v1.0",
    "created_for": "High-Rise Residential Design Assistant",
    "description": "A precedent knowledge base containing 20 high-rise residential cases analyzed through site context, drawings, photos, Gene_A, Gene_B, Gene_C1, Gene_C2, and Gene_D.",
    "case_count": len(cases),
    "cases": cases,
    "case_index": case_index
}

with open(output_json, "w", encoding="utf-8") as f:
    json.dump(database, f, ensure_ascii=False, indent=2)

with open(output_txt, "w", encoding="utf-8") as f:
    f.write(json.dumps(database, ensure_ascii=False, indent=2))

print(f"Saved: {output_json}")
print(f"Saved: {output_txt}")
print(f"Total cases: {len(cases)}")
