from copy import deepcopy
import vdf2
import json

def update():
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

        json.dump(data, wf, indent=4)


if __name__ == "__main__":
    update()