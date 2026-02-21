from typing import Self
from ._loader import _HEROES, _LOCALS
import re

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

    @classmethod
    def getByName(cls, name: str) -> Self:
        """Get Hero object from hero codename

        Args:
            name (str): hero codename

        Returns:
            Hero: Hero object
        """        
        return Hero(name, _HEROES[name])

    @classmethod
    def getById(cls, id: int | str) -> Self:
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

    @classmethod
    def getByDisplayName(cls, displayName: str) -> Self:
        """Get Hero object by display name

        Args:
            displayName (str): hero display name

        Raises:
            IndexError: incorrect display name

        Returns:
            Hero: Hero object
        """        
        for k in _LOCALS:
            v = _LOCALS[k]
            regex = re.compile(r"npc_dota_hero_[A-z_]+:n")
            if regex.match(k) and v == displayName:
                return Hero(k, _HEROES[k[:-2]])

        raise IndexError(f"{displayName} - incorrect display name")
