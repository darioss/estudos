document.getElementById("infoForm").addEventListener("submit", function (event) {
       event.preventDefault();

       // Capturar os valores do formulário
       let nome = document.getElementById("nome").value;
       let idade = document.getElementById("idade").value;
       let linguagem = document.getElementById("linguagem").value;

       // Exibir a mensagem personalizada
       let mensagem = `Olá ${nome}, você tem ${idade} anos e está aprendendo ${linguagem}!`;
	document.getElementById("mensagem").style.display = "block";
       document.getElementById("infoForm").style.display = "none";
       document.getElementById("complementForm").style.display = "block";
       document.getElementById("labelPrefers").innerHTML = `Você gosta de estudar ${linguagem}?`;
       document.getElementById("mensagem").textContent = mensagem;
});

document.getElementById("yes").addEventListener("click", function (e) {
       document.getElementById("complementForm").innerHTML = "Muito bom! Continue estudando e você terá muito sucesso";
});
document.getElementById("no").addEventListener("click", function (e) {
       document.getElementById("complementForm").innerHTML = "Ahh que pena... Já tentou aprender outras linguagens?";
});


