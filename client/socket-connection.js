const url = "http://127.0.0.1:8080";

var socket = io(url);

socket.on('messages', function (data) {
    
    /* 
        Este código vai estar sempre escutando o evento pelo lado do servidor.
        Assim que o servidor emitir uma mensagem para este evento, ele vai receber e printar
        no console.log abaixo.
    */

        var now = new Date;
        var horario = now.getDate() + '/' + (now.getMonth() + 1) + ' ' + now.getHours() + ':' + now.getMinutes();
        var elemento = document.createElement('li');
        elemento.innerHTML = "<li class='d-flex mb-4'>"+
                "<img src='img/bot.png' alt='avatar' class='rounded-circle d-flex align-self-start me-3 shadow-1-strong' width='60'>"+
                "<div class='card mask-custom w-100'>"+
                    "<div class='card-header justify-content-between d-flex p-3' style='border-bottom: 1px solid rgba(255,255,255,.3);'>"+
                        "<p class='text-light small mb-0'>"+ horario +"</p>"+
                        "<p class='fw-bold mb-0'>Robô</p>"+
                    "</div>"+
                    "<div class='card-body'>"+
                        "<p class='mb-0'>"+
                            data+
                        "</p>"+
                    "</div>"+
                "</div>"+
            "</li>";
        document.querySelector('.lista ul').append(elemento);
        var scroll = document.querySelector(".lista");
        scroll.scrollTop = scroll.scrollHeight;
});

document.addEventListener("DOMContentLoaded", function(event) {
    
    var now = new Date;
    var mensagem;
    if(now.getHours() < 12) {
        mensagem = 'Bom dia';
    } else if (now.getHours() < 18) {
        mensagem = 'Boa tarde';
    } else if (now.getHours() >= 18) {
        mensagem = 'Boa noite';
    }

    chamado(mensagem);
});

document.getElementById("botaoEnviar").addEventListener("click", () => {

    const mensagem = document.getElementById("campoMensagem").value

    if(mensagem.trim() == '') {

        alert("Escreva o que deseja da nossa loja.");

    } else {

        var now = new Date;
        var horario = now.getDate() + '/' + (now.getMonth() + 1) + ' ' + now.getHours() + ':' + now.getMinutes();
        var elemento = document.createElement('li');
        elemento.innerHTML = "<li class='d-flex mb-4'>"+
                "<div class='card mask-custom w-100'>"+
                    "<div class='card-header justify-content-between d-flex p-3' style='border-bottom: 1px solid rgba(255,255,255,.3);'>"+
                        "<p class='fw-bold mb-0'>Você</p>"+
                        "<p class='text-light small mb-0'>"+horario+"</p>"+
                    "</div>"+
                    "<div class='card-body'>"+
                        "<p class='mb-0'>"+
                            mensagem+
                        "</p>"+
                    "</div>"+
                "</div>"+
                "<img src='img/usuario.png' alt='avatar' class='rounded-circle d-flex align-self-start ms-3 shadow-1-strong' width='60'>"+
            "</li>";

        document.querySelector('.lista ul').append(elemento);
        var scroll = document.querySelector(".lista");
        scroll.scrollTop = scroll.scrollHeight;
        document.getElementById("campoMensagem").value = '';
        chamado(mensagem);
    }
});

function chamado(mensagem) {
    
    //Vai enviar o json para o evento 'messages'
    socket.emit("messages", {
        "mensagem": mensagem
    });
}