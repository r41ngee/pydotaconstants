from ._core import _HEROES, _LOCALS

class Hero():
    """Represents single hero data
    should not be created with constructor
    """
    def __init__(self, name: str, kv: dict):
        self._name = name
        self._id = int(kv.get("HeroID", -1))
        self._data = kv

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
    def data(self) -> dict:
        return self._data

    @property
    def displayName(self) -> str:
        """Returns name of given hero
        example: Axe

        Returns:
            str: hero name. Returns empty string if incorrect codename
        """
        return _LOCALS.get(self.name + ":n", "")

    def getByName(name: str) -> Hero:
        """Get Hero object from hero codename

        Args:
            name (str): hero codename

        Returns:
            Hero: Hero object
        """        
        return Hero(name, _HEROES[name])

    def getById(id: int | str) -> Hero:
        """Get Hero object by HeroID

        Args:
            id (int | str): HeroID

        Raises:
            IndexError: incorrect hero id


        Returns:
            Hero: Hero object
        """
        id = str(id)

        for i in _HEROES:
            hero_kv = _HEROES[i]
            if hero_kv["HeroID"] == id:
                return Hero(i, hero_kv)

        raise IndexError(f"ID {id} not found.")
