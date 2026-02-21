from ._core import HEROES, LOCALS
_heroes = HEROES


def getById(id):
    for hero in _heroes:
        if hero["HeroID"] == id:
            return hero
    else:
        raise IndexError("Incorrect ID.")

def getDisplayName(hero_name: str | None = None, hero_id: int | None = None):
    if hero_name:
        pass
    elif hero_id:
        hero_name = getById(hero_id)
    else:
        raise TypeError(f"{getDisplayName.__name__} requires at least 1 argument")

    return LOCALS[hero_name+":n"]
