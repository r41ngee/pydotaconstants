from copy import deepcopy
import vdf2
import json
import pickle
import os

def _update():
    ALLHERO = {}
    ALLABILITIES = {}

    for file in os.listdir("src/pydotaconstants/source_vdf/heroes/"):
        with open(f"src/pydotaconstants/source_vdf/heroes/{file}") as rf:
            data = vdf2.load(rf)["DOTAHeroes"]

            # MEEPO AINT FIXED ANYWAY :)
            if file == "npc_dota_hero_meepo":
                fixing: dict = data["npc_dota_hero_meepo"]["AbilityDefinitions"]
                fixing.pop("AbilityCastPoint")
                fixing.pop("AbilityCastAnimation")

            abilities = data[file].pop("AbilityDefinitions")
            ALLHERO[file] = data[file]
            ALLABILITIES[file] = abilities

    # LOCALIZATION
    LOCALS_DIR = "src/pydotaconstants/source_vdf/locals/"
    locals_files = os.listdir(LOCALS_DIR)

    locals_alldata = {}

    for file in locals_files:
        with open(LOCALS_DIR + file, encoding="utf-8") as rf:
            data = vdf2.load(rf)
            data = data["lang"]["Tokens"]
            locals_alldata.update(data)

    locals_alldata = dict(sorted(locals_alldata.items()))

    with open("src/pydotaconstants/data/locals.json", "w", encoding="utf-8") as wf:
        json.dump(locals_alldata, wf, indent=4, ensure_ascii=False)
    with open("src/pydotaconstants/data/locals.pkl", "wb") as wf:
        pickle.dump(locals_alldata, wf)

    with open("src/pydotaconstants/source_vdf/items.txt") as rf:
        data = vdf2.load(rf)
    items: dict = deepcopy(data["DOTAAbilities"])
    for item in list(items):
        if item in ["Version"]:
            items.pop(item)
            continue

    # ITEMS
    items = dict(sorted(items.items()))
    
    with open("src/pydotaconstants/data/items.json", "w") as wf:
        json.dump(items, wf, indent=4)
    with open("src/pydotaconstants/data/items.pkl", "wb") as pkl_f:
        pickle.dump(items, pkl_f)

if __name__ == "__main__":
    _update()