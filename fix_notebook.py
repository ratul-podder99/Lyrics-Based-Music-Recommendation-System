import json

with open("Music_Recommendation_System(488).ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

# Fix: add 'state' key if missing, or remove widgets metadata entirely
if "widgets" in nb.get("metadata", {}):
    widgets = nb["metadata"]["widgets"]
    for key, val in widgets.items():
        if isinstance(val, dict) and "state" not in val:
            val["state"] = {}  # Add empty state

with open("Music_Recommendation_System_fixed.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)

print("Fixed!")