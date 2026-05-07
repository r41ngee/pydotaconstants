from typing import Self
from ._loader import _HEROES, LOCALS, _ITEMS
import re

class Item():
    """Represents single item data
    should not be created with constructor
    """
    def __init__(self, name: str, kv: dict):
        self._name = name
        self._id = int(kv.get("HeroID", -1))
        self._data = kv

    @property
    def name(self) -> str:
        """Item code name
        example: item_blink

        Returns:
            str: item code name
        """
        return self._name

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
        return LOCALS.get(self.name, "")

    @classmethod
    def getByName(cls, name: str) -> Self:
        """Get Hero object from hero codename

        Args:
            name (str): hero codename

        Returns:
            Item: Item object
        """
        return Item(name, _ITEMS[name])

    @classmethod
    def getByDisplayName(cls, display_name: str) -> Self:
        """Get Hero object by display name

        Args:
            displayName (str): item display name

        Raises:
            IndexError: incorrect display name

        Returns:
            Item: Item object
        """
        regex = re.compile(r"item_[A-z_]+:n")
        for k in LOCALS:
            v = LOCALS[k]
            if regex.match(k) and v == display_name:
                return Item(k, _ITEMS[k])

        raise IndexError(f"{display_name} - incorrect display name")

    @classmethod
    def all(cls) -> list[Self]:
        result = []
        for item_name in _ITEMS:
            result.append(cls.getByName(item_name))

        return result
