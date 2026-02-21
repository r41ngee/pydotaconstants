from copy import deepcopy
import vdf2
import json
import os

def _update():
    # HEROES
    H_KEY_LIST = [
        "Ability1",
        "Ability2",
        "Ability3",
        "Ability4",
        "Ability5",
        "Ability6",
        "Ability7",
        "Ability8",
        "Ability9",
        "HeroID",
        "Facets",
        "ArmorPhysical",
        "AttackCapabilities",
        "AttackDamageMin",
        "AttackDamageMax",
        "BaseAttackSpeed",
        "AttackRate",
        "AttackRange",
        "AttributePrimary",
        "AttributeBaseStrength",
        "AttributeStrengthGain",
        "AttributeBaseAgility",
        "AttributeAgilityGain",
        "AttributeBaseIntelligence",
        "AttributeIntelligenceGain",
        "MovementSpeed"
    ]

    with open("src/pydotaconstants/source_vdf/npc_heroes.txt") as rf, open("src/pydotaconstants/data/heroes.json", "w") as wf:
        data = vdf2.load(rf)
        heroes: dict = deepcopy(data["DOTAHeroes"])
        for hero in heroes:
            if hero in ["Version", "npc_dota_hero_base"]:
                data["DOTAHeroes"].pop(hero)
                continue

            for k in heroes[hero]:
                if not k in H_KEY_LIST:
                    data["DOTAHeroes"][hero].pop(k)
                else:
                    print(hero)
                    print(k)

        json.dump(data["DOTAHeroes"], wf, indent=4)

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

if __name__ == "__main__":
    _update()