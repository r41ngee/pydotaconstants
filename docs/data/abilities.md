# Abilities

Browse all Dota 2 abilities from pydotaconstants data.

<div class="controls">
    <input type="text" id="search" placeholder="Search by name or codename...">
    <select id="type-filter">
        <option value="">All types</option>
        <option value="Active">Active</option>
        <option value="Passive">Passive</option>
        <option value="Toggle">Toggle</option>
        <option value="Autocast">Autocast</option>
        <option value="Innate">Innate</option>
    </select>
    <span class="count" id="count"></span>
</div>

<div class="grid" id="grid"></div>
<div class="empty" id="empty" style="display:none">No abilities match your search.</div>

<div class="modal-overlay" id="modal">
    <div class="modal-content">
        <button class="modal-close" id="modal-close">&times;</button>
        <h2 id="modal-title"></h2>
        <div class="modal-sub" id="modal-sub"></div>
        <div id="modal-desc"></div>
        <div class="json-view" id="modal-json"></div>
    </div>
</div>

<script>
(async () => {
    const [abilRes, localsRes] = await Promise.all([
        fetch('./abilities.json'),
        fetch('./locals.json')
    ]);
    const rawAbilities = await abilRes.json();
    const locals = await localsRes.json();

    const TYPE_CLASS = {
        'Active': 'tag-active',
        'Passive': 'tag-passive',
        'Toggle': 'tag-toggle',
        'Autocast': 'tag-autocast',
        'Innate': 'tag-innate'
    };

    function getAbilityTypes(data) {
        const types = [];
        const b = data.AbilityBehavior || '';
        if (b.includes('DOTA_ABILITY_BEHAVIOR_PASSIVE')) types.push('Passive');
        else if (b.includes('DOTA_ABILITY_BEHAVIOR_TOGGLE')) types.push('Toggle');
        else if (b.includes('DOTA_ABILITY_BEHAVIOR_AUTOCAST')) types.push('Autocast');
        else types.push('Active');
        if (data.Innate == 1) types.push('Innate');
        return types;
    }

    function resolveDesc(codename, rawDesc, abilityData) {
        const av = abilityData.AbilityValues || {};
        let desc = rawDesc.replace(/<[^>]+>/g, '');

        desc = desc.replace(/%(\w+?)%+/g, (match, key) => {
            const val = av[key];
            if (!val) return match;
            const num = typeof val === 'string' ? val : (val && val.value ? val.value : '');
            if (!num) return match;
            const isPct = match.endsWith('%%');
            const formatted = num.split(' ').map(v => v && isPct ? v + '%' : v).filter(Boolean).join(' / ');
            return formatted;
        });

        const specials = [];
        for (const [key, val] of Object.entries(av)) {
            const tipKey = 'DOTA_Tooltip_ability_' + codename + '_' + key;
            if (locals[tipKey]) {
                const num = typeof val === 'string' ? val : (val && val.value ? val.value : '');
                const isPct = locals[tipKey].startsWith('%');
                const label = isPct ? locals[tipKey].slice(1) : locals[tipKey];
                const value = num.split(' ').map(v => v && isPct && !v.endsWith('%') ? v + '%' : v).filter(Boolean).join(' / ');
                specials.push({ label, value });
            }
        }

        return { desc, specials };
    }

    const abilities = Object.entries(rawAbilities)
        .filter(([key, data]) => typeof data === 'object' && data.BaseClass !== 'special_bonus_base' && !key.startsWith('special_bonus_'))
        .map(([key, data]) => {
            const rawDesc = locals['DOTA_Tooltip_ability_' + key + '_Description'] || '';
            const { desc, specials } = resolveDesc(key, rawDesc, data);
            return {
                codename: key,
                displayName: locals['DOTA_Tooltip_ability_' + key] || '',
                description: desc,
                specials,
                cooldown: data.AbilityCooldown ? data.AbilityCooldown.split(' ').filter(Boolean).join(' / ') : '—',
                manaCost: data.AbilityManaCost ? data.AbilityManaCost.split(' ').filter(Boolean).join(' / ') : '—',
                type: getAbilityTypes(data),
                data
            };
        })
        .filter(a => a.displayName)
        .sort((a, b) => a.displayName.localeCompare(b.displayName));

    const grid = document.getElementById('grid');
    const empty = document.getElementById('empty');
    const countEl = document.getElementById('count');
    const searchInput = document.getElementById('search');

    function render() {
        const q = searchInput.value.toLowerCase();
        const type = document.getElementById('type-filter').value;
        const filtered = abilities.filter(a => {
            if (q && !a.displayName.toLowerCase().includes(q) && !a.codename.includes(q)) return false;
            if (type && !a.type.includes(type)) return false;
            return true;
        });
        countEl.textContent = `${filtered.length} / ${abilities.length}`;
        if (filtered.length === 0) { grid.innerHTML = ''; empty.style.display = ''; return; }
        empty.style.display = 'none';
        const ABIL_IMG = 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/abilities/';
        grid.innerHTML = filtered.map(a => `
            <div class="card" data-codename="${a.codename}">
                <img class="card-icon" src="${ABIL_IMG}${a.codename}.png" alt="${a.displayName}" onerror="this.style.display='none'">
                <div class="card-name">${a.displayName}</div>
                ${a.displayName !== a.codename ? `<div class="card-codename">${a.codename}</div>` : ''}
                <div class="card-meta">
                    ${a.type.map(t => `<span class="tag ${TYPE_CLASS[t] || ''}">${t}</span>`).join(' ')}
                </div>
                <div class="card-desc">${a.description.substring(0, 120)}${a.description.length > 120 ? '…' : ''}</div>
                ${(a.cooldown !== '—' || a.manaCost !== '—') ? `
                <div class="stat-row">
                    ${a.cooldown !== '—' ? `<span class="stat">CD: ${a.cooldown}</span>` : ''}
                    ${a.manaCost !== '—' ? `<span class="stat">Mana: ${a.manaCost}</span>` : ''}
                </div>` : ''}
            </div>
        `).join('');
        grid.querySelectorAll('.card').forEach(card => {
            card.addEventListener('click', () => {
                const a = abilities.find(x => x.codename === card.dataset.codename);
                document.getElementById('modal-title').textContent = a.displayName;
                document.getElementById('modal-sub').textContent = a.codename;
                let html = `<img class="modal-icon" src="${ABIL_IMG}${a.codename}.png" alt="${a.displayName}" onerror="this.style.display='none'"><div class="card-desc">${a.description}</div>`;
                if (a.specials.length) {
                    html += '<div class="specials">' + a.specials.map(s =>
                        `<div class="special-line"><span class="special-label">${s.label}</span> ${s.value}</div>`
                    ).join('') + '</div>';
                }
                document.getElementById('modal-desc').innerHTML = html;
                document.getElementById('modal-json').textContent = JSON.stringify(a.data, null, 2);
                document.getElementById('modal').classList.add('active');
            });
        });
    }

    document.getElementById('modal-close').addEventListener('click', () => document.getElementById('modal').classList.remove('active'));
    document.getElementById('modal').addEventListener('click', e => { if (e.target === e.currentTarget) e.target.classList.remove('active'); });
    searchInput.addEventListener('input', render);
    document.getElementById('type-filter').addEventListener('change', render);
    render();
})();
</script>
