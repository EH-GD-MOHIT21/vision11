
$(function () {
    var INDEX = 0;
    $("#chat-submit").click(function (e) {
        e.preventDefault();
        var msg = $("#chat-input").val();
        if (msg.trim() == '') {
            return false;
        }
        try{
            ws.send(JSON.stringify({
                'msg':msg
            }))   
        }
        catch(err){  
        }
        var buttons = [
            {
                name: 'Existing User',
                value: 'existing'
            },
            {
                name: 'New User',
                value: 'new'
            }
        ];

    })
    const user_id = JSON.parse(document.getElementById('user_id').textContent);
    const user_name = JSON.parse(document.getElementById('user_name').textContent);
    function connect_chat(){
        ws= new WebSocket('ws://'+window.location.host+'/'+'ws/sc/'+user_id+'/'+1+'/')
                ws.onopen=function(){
                    console.log('websocket is open now..')
                    ws.send
                }
                ws.onmessage=function(event){ 
                    const data=JSON.parse(event.data)
                    if(data['status']=='no' && data['updation']=='no'){
                        inputdom = document.getElementById('input_chat')
                        inputdom.style.display='none';
                        var ptag=document.createElement("div");
                        var queue_elem = document.createElement("div");
                        ptag.id='queue_show';
                        msg_gen = `Thank you for contacting us admin will shorly join chat please
                        don't close the chat box
                        Your are in queue:`;
                        ptag.innerHTML= msg_gen
                        queue_elem.id='queue_elm';
                        queue_elem.innerHTML=`Your in Queue no:${data['msg']}`;
                        ptag.appendChild(queue_elem);
                        document.getElementById('chat_logs').appendChild(ptag)
                    }
                    else if(data['updation']=='yes'){
                        queue_no = document.getElementById('queue_elm')
                        queue_no.innerHTML= `Your in Queue no:${data['msg']}`;   
                    }
                    else if (data['status']=='yes' && data['msg']=='Hii agent is here how can i help you!!'){
                        inputdom = document.getElementById('input_chat')
                        inputdom.style.display='';
                        var ptagg = document.getElementById('queue_show')
                        ptagg.innerHTML='';
                        if(data['username']==user_name){
                            Type_of = 'self';
                        }
                        else{
                            Type_of = 'user'; 
                        }
                        generate_message(data['msg'],Type_of)  
                    }
                    else {
                        if(data['username']==user_name){
                            Type_of = 'self';
                        }
                        else{
                            Type_of = 'user'; 
                        }
                        generate_message(data['msg'],Type_of)} 
                }
                ws.onclose=function(event){
                    console.log('server disconnected...')
                    var ptagg = document.getElementById('queue_show')
                    ptagg.remove()
                    var chat_hist = document.getElementById('chat_logs')
                    chat_hist.innerHTML='';
                } 
    }

    function generate_message(msg, type) {
        INDEX++;
        var str = "";
        str += "<div id='cm-msg-" + INDEX + "' class=\"chat-msg " + type + "\">";
        str += "          <div class=\"cm-msg-text\">";
        str += msg;
        str += "          <\/div>";
        str += "        <\/div>";
        $(".chat-logs").append(str);
        $("#cm-msg-" + INDEX).hide().fadeIn(300);
        if (type == 'self') {
            $("#chat-input").val('');
        }
        $(".chat-logs").stop().animate({ scrollTop: $(".chat-logs")[0].scrollHeight }, 1000);
    }

    function generate_button_message(msg, buttons) {
        /* Buttons should be object array 
          [
            {
              name: 'Existing User',
              value: 'existing'
            },
            {
              name: 'New User',
              value: 'new'
            }
          ]
        */
        INDEX++;
        var btn_obj = buttons.map(function (button) {
            return "              <li class=\"button\"><a href=\"javascript:;\" class=\"btn btn-primary chat-btn\" chat-value=\"" + button.value + "\">" + button.name + "<\/a><\/li>";
        }).join('');
        var str = "";
        str += "<div id='cm-msg-" + INDEX + "' class=\"chat-msg user\">";
        // str += "          <span class=\"msg-avatar\">";
        // str += "            <img src=\"https:\/\/image.crisp.im\/avatar\/operator\/196af8cc-f6ad-4ef7-afd1-c45d5231387c\/240\/?1483361727745\">";
        // str += "          <\/span>";
        str += "          <div class=\"cm-msg-text\">";
        str += msg;
        str += "          <\/div>";
        str += "          <div class=\"cm-msg-button\">";
        str += "            <ul>";
        str += btn_obj;
        str += "            <\/ul>";
        str += "          <\/div>";
        str += "        <\/div>";
        $(".chat-logs").append(str);
        $("#cm-msg-" + INDEX).hide().fadeIn(300);
        $(".chat-logs").stop().animate({ scrollTop: $(".chat-logs")[0].scrollHeight }, 1000);
        $("#chat-input").attr("disabled", true);
    }

    $(document).delegate(".chat-btn", "click", function () {
        var value = $(this).attr("chat-value");
        var name = $(this).html();
        $("#chat-input").attr("disabled", false);
        generate_message(name, 'self');
    })

    $("#chat-circle").click(function () {
        $("#chat-circle").toggle('scale');
        $(".chat-box").toggle('scale');
        connect_chat()
    })

    $(".chat-box-toggle").click(function () {
        $("#chat-circle").toggle('scale');
        $(".chat-box").toggle('scale');
        try{
            ws.close()  
        }
        catch(err){   
        }
    })

});