from typing import Self
from ._loader import _ABILITIES, LOCALS
import re

class Ability:
    """Class represents ability data
    should be created with class methods
    """    
    def __init__(self, name: str, data: dict):
        self._name = name
        self._data = data
        self._displayName = LOCALS.get(name, "")
        self._displayDescription = LOCALS.get(name+"_Description", "")

    @property
    def displayName(self) -> str:
        """Returns display name

        Returns:
            str: display name
        """        
        return self._displayName

    @property
    def name(self) -> str:
        """Returns codename of ability

        Returns:
            str: ability codename
        """        
        return self._name

    @property
    def data(self) -> dict:
        """Returns ability data

        Returns:
            dict: ability data
        """        
        return self._data

    @property
    def displayDescription(self) -> str:
        """Returns ability description

        Returns:
            str: ability description (english)
        """        
        return self._displayDescription

    @classmethod
    def getByName(cls, name: str) -> Self:
        """Returns Ability object

        Args:
            name (str): ability codename

        Returns:
            Ability: ability object
        """        
        return Ability(name, _ABILITIES[name])

    @classmethod
    def getByDisplayName(cls, display_name: str) -> Self:
        """Returns Ability object

        Args:
            display_name (str): ability display name

        Raises:
            IndexError: incorrect display name

        Returns:
            Self: Ability object

        ---

        **CAN LEAD TO UNDEFINED BEHAVIOR WITH SPELLS WITH SAME NAMES (SHADOW SHAMAN's HEX AND LION's HEX)**
        """        
        regex = re.compile(r"npc_dota_hero_[A-z_]+:n")
        for key in LOCALS:
            value = LOCALS[key]
            if (not regex.match(key)) and display_name == value:
                return Ability(key, _ABILITIES[key])

        raise IndexError(f"{display_name} - incorrect display name")