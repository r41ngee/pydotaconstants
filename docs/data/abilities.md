# Abilities

Browse all Dota 2 abilities from pydotaconstants data.

<div class="controls">
    <input type="text" id="search" placeholder="Search by name or codename...">
    <span class="count" id="count"></span>
</div>

<div class="grid" id="grid"></div>
<div class="empty" id="empty" style="display:none">No abilities match your search.</div>

<div class="modal-overlay" id="modal">
    <div class="modal-content">
        <button class="modal-close" id="modal-close">&times;</button>
        <h2 id="modal-title"></h2>
        <div class="modal-sub" id="modal-sub"></div>
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

        const abilities = Object.entries(rawAbilities)
            .filter(([key, data]) => data.BaseClass !== 'special_bonus_base' && !key.startsWith('special_bonus_'))
            .map(([key, data]) => ({
            codename: key,
            displayName: locals['DOTA_Tooltip_ability_' + key] || key,
            description: (locals['DOTA_Tooltip_ability_' + key + '_Description'] || '').replace(/<[^>]+>/g, ''),
            cooldown: data.AbilityCooldown || '—',
            manaCost: data.AbilityManaCost || '—',
            behavior: data.AbilityBehavior || '',
            data
        })).sort((a, b) => a.displayName.localeCompare(b.displayName));

    const grid = document.getElementById('grid');
    const empty = document.getElementById('empty');
    const countEl = document.getElementById('count');
    const searchInput = document.getElementById('search');

    function render() {
        const q = searchInput.value.toLowerCase();
        const filtered = abilities.filter(a => {
            if (q && !a.displayName.toLowerCase().includes(q) && !a.codename.includes(q)) return false;
            return true;
        });
        countEl.textContent = `${filtered.length} / ${abilities.length}`;
        if (filtered.length === 0) { grid.innerHTML = ''; empty.style.display = ''; return; }
        empty.style.display = 'none';
        grid.innerHTML = filtered.map(a => `
            <div class="card" data-codename="${a.codename}">
                <div class="card-name">${a.displayName}</div>
                ${a.displayName !== a.codename ? `<div class="card-codename">${a.codename}</div>` : ''}
                <div class="card-desc">${a.description.substring(0, 120)}${a.description.length > 120 ? '…' : ''}</div>
                <div class="stat-row">
                    <span class="stat">CD: ${a.cooldown}</span>
                    <span class="stat">Mana: ${a.manaCost}</span>
                </div>
            </div>
        `).join('');
        grid.querySelectorAll('.card').forEach(card => {
            card.addEventListener('click', () => {
                const a = abilities.find(x => x.codename === card.dataset.codename);
                document.getElementById('modal-title').textContent = a.displayName;
                document.getElementById('modal-sub').textContent = a.codename;
                document.getElementById('modal-json').textContent = JSON.stringify(a.data, null, 2);
                document.getElementById('modal').classList.add('active');
            });
        });
    }

    document.getElementById('modal-close').addEventListener('click', () => document.getElementById('modal').classList.remove('active'));
    document.getElementById('modal').addEventListener('click', e => { if (e.target === e.currentTarget) e.target.classList.remove('active'); });
    searchInput.addEventListener('input', render);
    render();
})();
</script>
