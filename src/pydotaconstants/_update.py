from copy import deepcopy
import vdf2
import json
import pickle
import os

def _update():
    print("[update] starting data refresh...")
    ALLHERO = {}
    ALLABILITIES = {}
    hero_files = os.listdir("src/pydotaconstants/source_vdf/heroes/")
    print(f"[update] found {len(hero_files)} hero files")

    for file in hero_files:
        print(f"[update] processing hero: {file}")
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

        

        print(f"[update] hero processed: {file}")

    print(f"[update] heroes loaded: {len(ALLHERO)}")

    ALLHERO = dict(sorted(ALLHERO))
    with open("src/pydotaconstants/data/heroes.json", "w", encoding="utf-8") as wf:
        vdf2.dump(ALLHERO, wf)

    ALLABILITIES = dict(sorted(ALLABILITIES))
    with open("src/pydotaconstants/data/abilities.json", "w", encoding = "utf-8") as wf:
        vdf2.dump(ALLABILITIES, wf)

    # LOCALIZATION
    LOCALS_DIR = "src/pydotaconstants/source_vdf/locals/"
    locals_files = os.listdir(LOCALS_DIR)
    print(f"[update] found {len(locals_files)} localization files")

    locals_alldata = {}

    for file in locals_files:
        print(f"[update] processing localization: {file}")
        with open(LOCALS_DIR + file, encoding="utf-8") as rf:
            data = vdf2.load(rf)
            data = data["lang"]["Tokens"]
            locals_alldata.update(data)

    locals_alldata = dict(sorted(locals_alldata.items()))
    print(f"[update] total locales collected: {len(locals_alldata)}")

    with open("src/pydotaconstants/data/locals.json", "w", encoding="utf-8") as wf:
        json.dump(locals_alldata, wf, indent=4, ensure_ascii=False)
    with open("src/pydotaconstants/data/locals.pkl", "wb") as wf:
        pickle.dump(locals_alldata, wf)
    print("[update] saved locals.json and locals.pkl")

    print("[update] processing items...")
    with open("src/pydotaconstants/source_vdf/items.txt") as rf:
        data = vdf2.load(rf)
    items: dict = deepcopy(data["DOTAAbilities"])
    for item in list(items):
        if item in ["Version"]:
            items.pop(item)
            continue

    # ITEMS
    items = dict(sorted(items.items()))
    print(f"[update] total items collected: {len(items)}")

    with open("src/pydotaconstants/data/items.json", "w") as wf:
        json.dump(items, wf, indent=4)
    with open("src/pydotaconstants/data/items.pkl", "wb") as pkl_f:
        pickle.dump(items, pkl_f)
    print("[update] saved items.json and items.pkl")
    print("[update] finished successfully")

if __name__ == "__main__":
    _update()