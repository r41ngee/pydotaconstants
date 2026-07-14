# Hero

```python
from pydotaconstants import Hero
```

The `Hero` class represents a single Dota 2 hero. Do not instantiate directly — use the class methods below.

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `name` | `str` | Hero codename, e.g. `npc_dota_hero_axe` |
| `id` | `int` | Hero's HeroID, e.g. `2` |
| `displayName` | `str` | Localized name, e.g. `Axe` |
| `data` | `dict` | Raw hero data dictionary |

## Methods

### `Hero.getByName(name)`

Get a hero by its codename.

```python
hero = Hero.getByName("npc_dota_hero_axe")
print(hero.displayName)  # Axe
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `name` | `str` | Hero codename |

**Returns:** `Hero`

---

### `Hero.getById(id)`

Get a hero by its HeroID.

```python
hero = Hero.getById(2)
print(hero.displayName)  # Axe
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `id` | `int \| str` | Hero ID |

**Returns:** `Hero`

**Raises:** `IndexError` — if the ID is not found.

---

### `Hero.getByDisplayName(display_name)`

Get a hero by its display name.

```python
hero = Hero.getByDisplayName("Axe")
print(hero.name)  # npc_dota_hero_axe
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `display_name` | `str` | Hero display name (English) |

**Returns:** `Hero`

**Raises:** `IndexError` — if the display name is not found.

---

### `Hero.all()`

Get all heroes.

```python
heroes = Hero.all()
print(len(heroes))  # 124
```

**Returns:** `list[Hero]`
