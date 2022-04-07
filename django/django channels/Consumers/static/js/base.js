// let ws = new WebSocket("ws://127.0.0.1:8000/async")
// ws.onopen = function () {
//     console.log("conneted");
//     // ws.send("hellow")
// }

// ws.onmessage = function(event){
//     console.log(event['data']);
// }
// ws.onerror = function(event){
//     console.log(event);
// }
// ws.onclose = function(event){
//     console.log("disconneted",event);
// }

// with events
// ws.addEventListener('open',()=>{
//     console.log("conneted");
// })

// ws.addEventListener('message',(event)=>{
//     var data = JSON.parse(event.data)
//     document.getElementById("id").innerText
// })

// document.getElementById("btn").onclick = function(event){
//     const message = document.getElementById('input_message')
//     const mes = message.value
//     console.log(typeof(mes))
//     // ws.send(mes)
// }