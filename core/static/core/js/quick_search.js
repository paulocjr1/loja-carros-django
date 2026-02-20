document.addEventListener('DOMContentLoaded', () => {

    console.log('quick_search.js carregado corretamente');

    const input = document.getElementById('quick-search');
    const dropdown = document.getElementById('search-results');

    if (!input || !dropdown) {
        console.error('Elementos da quick search não encontrados');
        return;
    }

    let timeout = null;

    input.addEventListener('input', function () {
        clearTimeout(timeout);

        const q = this.value.trim();

        if (q.length < 2) {
            dropdown.classList.add('hidden');
            dropdown.innerHTML = '';
            return;
        }

        timeout = setTimeout(() => {
            fetch(`/quick-search/?q=${encodeURIComponent(q)}`)
                .then(res => res.json())
                .then(data => {
                    dropdown.innerHTML = '';

                    if (!data.length) {
                        dropdown.classList.add('hidden');
                        return;
                    }

                    data.forEach(item => {
                        const div = document.createElement('div');
                        div.className = 'flex items-center gap-3 p-3 hover:bg-orange-100 cursor-pointer transition';

                        div.innerHTML = `
                            <img src="${item.img}" 
                                class="w-14 h-14 object-cover rounded-md border" />

                            <div class="flex flex-col">
                                <span class="font-semibold text-gray-800">${item.label}</span>
                                <span class="text-sm text-gray-500">${item.ano}</span>
                                <span class="text-sm font-medium text-orange-600">R$ ${item.preco}</span>
                            </div>
                        `;

                        div.onclick = () => {
                            window.location.href = item.url;
                        };

                        dropdown.appendChild(div);
                    });

                    dropdown.classList.remove('hidden');
                });
        }, 250);
    });

    document.addEventListener('click', function(e){
        if(!input.contains(e.target) && !dropdown.contains(e.target)){
            dropdown.classList.add('hidden');
        }
    });

});

document.addEventListener('DOMContentLoaded', function () {
    const input = document.getElementById('quick-search');
    const btn = document.getElementById('qs-btn');

    if (!input || !btn) return;

    btn.addEventListener('click', function () {
        const q = input.value.trim();

        if (q.length < 1) return;

        // redireciona pro catálogo com filtro
        window.location.href = `/?q=${encodeURIComponent(q)}#catalogo`;
    });

    // Enter também busca
    input.addEventListener('keydown', function(e){
        if(e.key === 'Enter'){
            e.preventDefault();
            btn.click();
        }
    });
});