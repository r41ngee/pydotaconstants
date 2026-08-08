mkdir -p src/pydotaconstants/source_vdf/abilities
mkdir -p src/pydotaconstants/source_vdf/locals

BASE="https://raw.githubusercontent.com/dotabuff/d2vpkr/master/dota"

curl -L -o src/pydotaconstants/source_vdf/npc_heroes.txt \
    "$BASE/scripts/npc/npc_heroes.txt"
curl -L -o src/pydotaconstants/source_vdf/items.txt \
    "$BASE/scripts/npc/items.txt"

curl -L -o src/pydotaconstants/source_vdf/locals/abilities_english.txt \
    "$BASE/resource/localization/abilities_english.txt"
curl -L -o src/pydotaconstants/source_vdf/locals/dota_english.txt \
    "$BASE/resource/localization/dota_english.txt"

gh api repos/dotabuff/d2vpkr/contents/dota/scripts/npc/heroes \
    | jq -r '.[].download_url' \
    | while read -r url; do
        name=$(basename "$url")
        curl -L -o "src/pydotaconstants/source_vdf/abilities/$name" "$url"
    done

uv sync

uv run src/pydotaconstants/_update.py