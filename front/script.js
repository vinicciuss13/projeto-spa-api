async function buscarUsuarios() {
    const listaUsuarios = document.getElementById("listaUsuarios");

    try {
        const resposta = await fetch("http://127.0.0.1:5000/usuarios");

        const usuarios = await resposta.json();

        listaUsuarios.innerHTML = "";

        usuarios.forEach(usuario => {
            listaUsuarios.innerHTML += `
                <div class="card">
                    <h3>${usuario.nome}</h3>
                    <p><strong>Email:</strong> ${usuario.email}</p>
                    <p><strong>Telefone:</strong> ${usuario.telefone}</p>
                </div>
            `;
        });

    } catch (erro) {
        listaUsuarios.innerHTML = "<p>Erro ao buscar usuários.</p>";
        console.error("Erro ao buscar usuários:", erro);
    }
}