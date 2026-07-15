# Items

Browse all Dota 2 items from pydotaconstants data.

<div class="controls">
    <input type="text" id="search" placeholder="Search by name or codename...">
    <select id="quality-filter"><option value="">All qualities</option></select>
    <span class="count" id="count"></span>
</div>

<div class="grid" id="grid"></div>
<div class="empty" id="empty" style="display:none">No items match your search.</div>

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
    const [itemRes, localsRes] = await Promise.all([
        fetch('./items.json'),
        fetch('./locals.json')
    ]);
    const rawItems = await itemRes.json();
    const locals = await localsRes.json();

        const items = Object.entries(rawItems).map(([key, data]) => ({
            codename: key,
            displayName: locals['DOTA_Tooltip_Ability_' + key] || key,
            cost: parseInt(data.ItemCost || 0),
        quality: data.ItemQuality || '',
        cooldown: data.AbilityCooldown || '—',
        manaCost: data.AbilityManaCost || '—',
        data
    })).sort((a, b) => a.displayName.localeCompare(b.displayName));

    const qualities = [...new Set(items.map(i => i.quality).filter(Boolean))].sort();
    const qualitySelect = document.getElementById('quality-filter');
    qualities.forEach(q => { const o = document.createElement('option'); o.value = q; o.textContent = q; qualitySelect.appendChild(o); });

    const grid = document.getElementById('grid');
    const empty = document.getElementById('empty');
    const countEl = document.getElementById('count');
    const searchInput = document.getElementById('search');

    function render() {
        const q = searchInput.value.toLowerCase();
        const quality = qualitySelect.value;
        const filtered = items.filter(i => {
            if (q && !i.displayName.toLowerCase().includes(q) && !i.codename.includes(q)) return false;
            if (quality && i.quality !== quality) return false;
            return true;
        });
        countEl.textContent = `${filtered.length} / ${items.length}`;
        if (filtered.length === 0) { grid.innerHTML = ''; empty.style.display = ''; return; }
        empty.style.display = 'none';
        grid.innerHTML = filtered.map(i => `
            <div class="card" data-codename="${i.codename}">
                <div class="card-name">${i.displayName}</div>
                ${i.displayName !== i.codename ? `<div class="card-codename">${i.codename}</div>` : ''}
                <div class="card-meta">
                    ${i.cost ? `<span class="tag tag-cost">${i.cost}g</span>` : ''}
                    ${i.quality ? `<span class="tag">${i.quality}</span>` : ''}
                    <span class="tag">CD: ${i.cooldown}</span>
                </div>
            </div>
        `).join('');
        grid.querySelectorAll('.card').forEach(card => {
            card.addEventListener('click', () => {
                const i = items.find(x => x.codename === card.dataset.codename);
                document.getElementById('modal-title').textContent = i.displayName;
                document.getElementById('modal-sub').textContent = i.codename;
                document.getElementById('modal-json').textContent = JSON.stringify(i.data, null, 2);
                document.getElementById('modal').classList.add('active');
            });
        });
    }

    document.getElementById('modal-close').addEventListener('click', () => document.getElementById('modal').classList.remove('active'));
    document.getElementById('modal').addEventListener('click', e => { if (e.target === e.currentTarget) e.target.classList.remove('active'); });
    searchInput.addEventListener('input', render);
    qualitySelect.addEventListener('change', render);
    render();
})();
</script>
