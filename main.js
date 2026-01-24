async function enviarIdea() {
    const texto = document.getElementById("idea").value;

    await fetch("/ideas", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({texto})
    });

    document.getElementById("idea").value = "";
    cargarIdeas();
}

async function cargarIdeas() {
    const res = await fetch("/ideas");
    const ideas = await res.json();

    const lista = document.getElementById("lista");
    lista.innerHTML = "";

    ideas.forEach(i => {
        const li = document.createElement("li");
        li.textContent = i;
        lista.appendChild(li);
    });
}

cargarIdeas();
