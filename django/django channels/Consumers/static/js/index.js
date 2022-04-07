// const ws = new WebSocket("ws://127.0.0.1:8000/async")

const groupname = JSON.parse(document.getElementById("groupname").textContent)
console.log(groupname)

const ws = new WebSocket(
    "ws://" + window.location.host + "/async/" + groupname 
    )


ws.addEventListener("open",()=>{
    console.log("connected...")
})
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]
ws.addEventListener('message',(event)=>{
    var data = JSON.parse(event.data)
    console.log(typeof(event.data))
    // let d = JSON.parse(data)
    // document.getElementById("id").innerText = data.msg
    document.querySelector(".text").value += (data.msg + "\n")
   
})

document.getElementById("send").onclick = (event)=>{
    const message = document.getElementById("text")
    const msg = message.value
    console.log(msg)
    ws.send(JSON.stringify({"msg" : msg}))
}