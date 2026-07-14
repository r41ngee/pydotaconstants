# Ability

```python
from pydotaconstants import Ability
```

The `Ability` class represents a single Dota 2 ability. Do not instantiate directly — use the class methods below.

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `name` | `str` | Ability codename, e.g. `antimage_mana_break` |
| `displayName` | `str` | Localized name |
| `displayDescription` | `str` | Localized description |
| `data` | `dict` | Raw ability data dictionary |

## Methods

### `Ability.getByName(name)`

Get an ability by its codename.

```python
ability = Ability.getByName("antimage_mana_break")
print(ability.displayName)  # Mana Break
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `name` | `str` | Ability codename |

**Returns:** `Ability`

---

### `Ability.getByDisplayName(display_name)`

Get an ability by its display name.

```python
ability = Ability.getByDisplayName("Blink")
print(ability.displayDescription)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `display_name` | `str` | Ability display name (English) |

**Returns:** `Ability`

**Raises:** `IndexError` - if the display name is not found.

!!! warning
    This method may return unexpected results for abilities with duplicate names across different heroes (e.g., Shadow Shaman's Hex and Lion's Hex).

---

### `Ability.all()`

Get all abilities.

```python
abilities = Ability.all()
print(len(abilities))  # 1000+
```

**Returns:** `list[Ability]`
