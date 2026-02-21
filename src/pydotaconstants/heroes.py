from ._core import _HEROES, _LOCALS
_heroes = _HEROES


class Hero():
    """Represents single hero data
    """
    def __init__(self, name: str, kv: dict):
        self._name = name
        self._id = int(kv.get("HeroID", -1))

    @property
    def name(self) -> str:
        """Hero code name
        example: npc_dota_hero_axe

        Returns:
            str: hero code name
        """
        return self._name

    @property
    def id(self) -> int:
        """Hero's HeroID

        Returns:
            int: Hero id
        """
        return self._id

    @property
    def displayName(self) -> str:
        """Returns name of given hero
        example: Axe

        Returns:
            str: hero name
        """
        return _LOCALS.get(self.name + ":n", "")