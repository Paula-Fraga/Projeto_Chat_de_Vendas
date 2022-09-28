const url = "http://127.0.0.1:8080/";

var socket = io(url);

socket.on('messages', function (data) {
    
    /* 
        Este código vai estar sempre escutando o evento pelo lado do servidor.
        Assim que o servidor emitir uma mensagem para este evento, ele vai receber e printar
        no console.log abaixo.
    */

    console.log(data)
});

document.getElementById("btn1").addEventListener("click", () => {
    const mensagem = document.getElementById("field1").value
    //Vai enviar o json para o evento 'messages'
    socket.emit("messages", {
        "mensagem": mensagem
    });
})
