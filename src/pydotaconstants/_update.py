from copy import deepcopy
import vdf2
import json
import pickle
import os

def _update():
    with open("src/pydotaconstants/source_vdf/npc_heroes.txt") as rf:
        data = vdf2.load(rf)
    heroes: dict = deepcopy(data["DOTAHeroes"])
    for hero in heroes:
        if hero in ["Version", "npc_dota_hero_base"]:
            data["DOTAHeroes"].pop(hero)
            continue
    
    with open("src/pydotaconstants/data/heroes.json", "w") as wf:
        json.dump(data["DOTAHeroes"], wf, indent=4)
    with open("src/pydotaconstants/data/heroes.pkl", "wb") as pkl_f:
        pickle.dump(data["DOTAHeroes"], pkl_f)

    # ABILITIES
    ABT_DIR = "src/pydotaconstants/source_vdf/abilities/"
    ability_files = os.listdir(ABT_DIR)

    ability_alldata = {}

    for file in ability_files:
        with open(ABT_DIR + file) as rf:
            data = vdf2.load(rf)["DOTAAbilities"]
        for ability in deepcopy(data):
            if ability == "Version":
                data.pop(ability)
                continue

        ability_alldata.update(data)

    with open("src/pydotaconstants/data/abilities.json", "w") as wf:
        json.dump(ability_alldata, wf, indent=4)
    with open("src/pydotaconstants/data/abilities.pkl", "wb") as wf:
        pickle.dump(ability_alldata, wf)

    # LOCALIZATION
    LOCALS_DIR = "src/pydotaconstants/source_vdf/locals/"
    locals_files = os.listdir(LOCALS_DIR)

    locals_alldata = {}

    for file in locals_files:
        with open(LOCALS_DIR + file, encoding="utf-8") as rf:
            data = vdf2.load(rf)["lang"]["Tokens"]
            locals_alldata.update(data)

    with open("src/pydotaconstants/data/locals.json", "w", encoding="utf-8") as wf:
        json.dump(locals_alldata, wf, indent=4, ensure_ascii=False)
    with open("src/pydotaconstants/data/locals.pkl", "wb") as wf:
        pickle.dump(locals_alldata, wf)

if __name__ == "__main__":
    _update()