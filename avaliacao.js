document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('form-avaliacao');
    const notaSelect = document.getElementById('nota');

    // Limpa opções antigas e adiciona a opção padrão
    notaSelect.innerHTML = '';
    const optionPadrao = document.createElement('option');
    optionPadrao.value = '';
    optionPadrao.text = 'Selecione a nota';
    optionPadrao.disabled = true;
    optionPadrao.selected = true;
    notaSelect.appendChild(optionPadrao);

    // Adiciona opções de 0 a 10
    for (let i = 0; i <= 10; i++) {
        const option = document.createElement('option');
        option.value = i;
        option.text = i;
        notaSelect.appendChild(option);
    }

    form.addEventListener('submit', (event) => {
        event.preventDefault();

        const nome = document.getElementById('nome').value.trim();
        const ra = document.getElementById('ra').value.trim();
        const dataNascimento = document.getElementById('data-nascimento').value;
        const curso = document.getElementById('curso').value;
        const nota = document.getElementById('nota').value;
        const sugestoes = document.getElementById('sugestoes').value.trim();
        const obs = document.getElementById('obs').value.trim();

        if (!nome || !ra || !dataNascimento || !curso || !nota || !sugestoes) {
            alert('Por favor, preencha todos os campos obrigatórios.');
            return;
        }

        console.log('Formulário preenchido:', {
            nome,
            ra,
            dataNascimento,
            curso,
            nota,
            sugestoes,
            obs
        });

        alert(`Obrigado pelo feedback, ${nome}!`);
        form.reset();
        document.getElementById('nome').focus();
    });
});
