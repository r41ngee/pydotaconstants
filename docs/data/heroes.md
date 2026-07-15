# Heroes

Browse all Dota 2 heroes from pydotaconstants data.

<div class="controls">
    <input type="text" id="search" placeholder="Search by name or codename...">
    <select id="attr-filter">
        <option value="">All attributes</option>
        <option value="Strength">Strength</option>
        <option value="Agility">Agility</option>
        <option value="Intelligence">Intelligence</option>
        <option value="Universal">Universal</option>
    </select>
    <select id="attack-filter">
        <option value="">All attacks</option>
        <option value="Melee">Melee</option>
        <option value="Ranged">Ranged</option>
    </select>
    <select id="complexity-filter">
        <option value="">All complexity</option>
        <option value="1">Low</option>
        <option value="2">Medium</option>
        <option value="3">High</option>
    </select>
    <span class="count" id="count"></span>
</div>

<div class="grid" id="grid"></div>
<div class="empty" id="empty" style="display:none">No heroes match your search.</div>

<div class="modal-overlay" id="modal">
    <div class="modal-content">
        <button class="modal-close" id="modal-close">&times;</button>
        <h2 id="modal-title"></h2>
        <div id="modal-desc"></div>
        <div class="json-view" id="modal-json"></div>
    </div>
</div>

<script>
(async () => {
    const res = await fetch('./heroes.json');
    const raw = await res.json();
    const localsRes = await fetch('./locals.json');
    const locals = await localsRes.json();

    const ATTR_MAP = {
        'DOTA_ATTRIBUTE_STRENGTH': 'Strength',
        'DOTA_ATTRIBUTE_AGILITY': 'Agility',
        'DOTA_ATTRIBUTE_INTELLECT': 'Intelligence',
        'DOTA_ATTRIBUTE_ALL': 'Universal'
    };
    const ATTR_CLASS = {
        'Strength': 'tag-str',
        'Agility': 'tag-agi',
        'Intelligence': 'tag-int',
        'Universal': 'tag-all'
    };
    const ATTACK_MAP = {
        'DOTA_UNIT_CAP_MELEE_ATTACK': 'Melee',
        'DOTA_UNIT_CAP_RANGED_ATTACK': 'Ranged'
    };

    const heroes = Object.entries(raw).map(([key, data]) => ({
        codename: key,
        id: parseInt(data.HeroID || -1),
        displayName: locals[key + ':n'] || key,
        attribute: ATTR_MAP[data.AttributePrimary] || data.AttributePrimary || '',
        attack: ATTACK_MAP[data.AttackCapabilities] || data.AttackCapabilities || '',
        complexity: parseInt(data.Complexity || 0),
        data
    })).sort((a, b) => a.displayName.localeCompare(b.displayName));

    const grid = document.getElementById('grid');
    const empty = document.getElementById('empty');
    const countEl = document.getElementById('count');
    const searchInput = document.getElementById('search');

    function render() {
        const q = searchInput.value.toLowerCase();
        const attr = document.getElementById('attr-filter').value;
        const attack = document.getElementById('attack-filter').value;
        const complexity = document.getElementById('complexity-filter').value;
        const filtered = heroes.filter(h => {
            if (q && !h.displayName.toLowerCase().includes(q) && !h.codename.includes(q)) return false;
            if (attr && h.attribute !== attr) return false;
            if (attack && h.attack !== attack) return false;
            if (complexity && h.complexity !== parseInt(complexity)) return false;
            return true;
        });
        countEl.textContent = `${filtered.length} / ${heroes.length}`;
        if (filtered.length === 0) { grid.innerHTML = ''; empty.style.display = ''; return; }
        empty.style.display = 'none';
        const HERO_IMG = 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/';
        grid.innerHTML = filtered.map(h => `
            <div class="card" data-codename="${h.codename}">
                <img class="card-icon" src="${HERO_IMG}${h.codename.replace('npc_dota_hero_', '')}.png" alt="${h.displayName}" onerror="this.style.display='none'">
                <div class="card-name">${h.displayName}</div>
                <div class="card-id">${h.codename}</div>
                <div class="card-meta">
                    <span class="tag ${ATTR_CLASS[h.attribute] || ''}">${h.attribute}</span>
                    <span class="tag tag-attack">${h.attack}</span>
                </div>
            </div>
        `).join('');
        grid.querySelectorAll('.card').forEach(card => {
            card.addEventListener('click', () => {
                const h = heroes.find(x => x.codename === card.dataset.codename);
                document.getElementById('modal-title').textContent = h.displayName;
                let modalHtml = `<img class="modal-icon" src="${HERO_IMG}${h.codename.replace('npc_dota_hero_', '')}.png" alt="${h.displayName}" onerror="this.style.display='none'">`;
                document.getElementById('modal-desc').innerHTML = modalHtml;
                document.getElementById('modal-json').textContent = JSON.stringify(h.data, null, 2);
                document.getElementById('modal').classList.add('active');
            });
        });
    }

    document.getElementById('modal-close').addEventListener('click', () => document.getElementById('modal').classList.remove('active'));
    document.getElementById('modal').addEventListener('click', e => { if (e.target === e.currentTarget) e.target.classList.remove('active'); });
    searchInput.addEventListener('input', render);
    document.getElementById('attr-filter').addEventListener('change', render);
    document.getElementById('attack-filter').addEventListener('change', render);
    document.getElementById('complexity-filter').addEventListener('change', render);
    render();
})();
</script>
