function connect_chat(){
    let ws= new WebSocket('ws://'+window.location.host+'/'+'ws/sc/'+grp_name+'/'+pid+'/')
            ws.onopen=function(){
                console.log('websocket is open now..')
                ws.send
            }
            ws.onmessage=function(event){ 
                const data=JSON.parse(event.data)
            }
            ws.onclose=function(event){
                console.log('server disconnected...')
            } 
          
}