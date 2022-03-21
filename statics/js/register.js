var inputs = document.querySelectorAll('.wrap-input100');
var inputelms = document.querySelectorAll(".wrap-input100 input");
var lengths = inputs.length;
var inputelmslength = inputelms.length;
var showcontent = 2;
var start = 0;
var finish = showcontent;
document.getElementById('prevbtn').style.display = 'none';
var emailstatus = undefined;
var usernamestatus = undefined;

for(var i=showcontent;i<lengths;i++){
    inputs[i].style.display = 'none';
}


function hidedisplay(sindex,showcontent,inputelmslength){
    for(var i=sindex;i<sindex+showcontent;i++){
        if(i>=inputelmslength)
            return
        inputs[i].style.display = 'none';
    }
}

function showdisplay(sindex,showcontent,inputelmslength){
    for(var i=sindex;i<sindex+showcontent;i++){
        if(i>=inputelmslength)
            return
        inputs[i].style.display = 'block';
    }
}


function elm(index){
    return inputelms[index]
}

function is_null(element){
    return element.value == ''
}

function next(start,finish){
    if(finish<inputelmslength){
        
    }
}

function showerror(id,message=1,custommsg="This Field is required!!"){
    if(message==1)
    document.getElementById("msg-error-"+(id+1)).innerText = custommsg;
    else
    document.getElementById("msg-error-"+(id+1)).innerText = "";
}

document.getElementById('nextbtn').addEventListener('click',function(){
    for(var i=start;i<finish;i++){
        showerror(i,message=0);
    }

    if(finish==4){
        // particular checks
        // showerror takes id-1 as input as it coverts id to id+1 
        if(emailstatus===undefined){
            showerror(2,message=1,custommsg="Invalid mail or already taken!!!")
            return;
        }
        if(usernamestatus === undefined){
            showerror(3,message=1,custommsg="Invalid username or already taken!!!")
            return;
        }
    }
    else{
        // default check for null
        for(var i=start;i<finish;i++){
            if(is_null(elm(i))){
                showerror(i);
                return;
            }
        }
    }
    if(finish==inputelmslength){
        document.getElementById('nextbtn').style.display = 'none'
        document.getElementById('prevbtn').style.display = 'none';
        inputs[lengths-2].style.display = 'block';
        document.querySelector('#btns-container-pn').style.display = 'block';
    }
    for(var i=start;i<finish;i++){
        showerror(i,message=0);
    }
    hidedisplay(start,showcontent,inputelmslength)
    start = finish;
    finish += showcontent;
    if(finish<=inputelmslength)
        document.getElementById('prevbtn').style.display = 'block';
    showdisplay(start,showcontent,inputelmslength)
})

document.getElementById('prevbtn').addEventListener('click',function(){
    if(finish==showcontent){
        return
    }
    for(var i=start;i<finish;i++){
        showerror(i,message=0);
    }
    hidedisplay(start,showcontent,inputelmslength)
    finish = start;
    start -= showcontent;
    showdisplay(start,showcontent,inputelmslength)
    if(finish==showcontent){
        document.getElementById('prevbtn').style.display = 'none';
    }
})

document.getElementById('signupform').style.display = 'block';

// axios post -> username
document.getElementById("id_username").addEventListener("input", function() {
    var uname = document.getElementById("id_username").value;
    axios.post('/check/username', {
            'username': uname,
        })
        .then(res => {
            let unamestatus = res['data']['message'];
            if (res['data']['message'] == 'Username Available.') {
                document.getElementById("msg-error-4").textContent = unamestatus;
                document.getElementById("msg-error-4").style.color = "green";
                usernamestatus = true;
            } else {
                document.getElementById("msg-error-4").textContent = unamestatus;
                document.getElementById("msg-error-4").style.color = "crimson";
                usernamestatus = undefined;
            }

        });
});

// axios post -> email
document.getElementById("id_email").addEventListener("input", function() {
    var email = document.getElementById("id_email").value;
    axios.post('/check/email', {
            'email': email,
        })
        .then(res => {
            unamestatus = res['data']['message'];
            if (res['data']['message'] == 'Email Available.') {
                document.getElementById("msg-error-3").textContent = unamestatus;
                document.getElementById("msg-error-3").style.color = "green";
                emailstatus = true;
            } else {
                document.getElementById("msg-error-3").textContent = unamestatus;
                document.getElementById("msg-error-3").style.color = "crimson"
                emailstatus = undefined;
            }

        });
});

document.getElementById('boyimg').addEventListener('click',function(){
    document.getElementById('id_gender_type').value = 'Male';
    document.getElementById('boyimg').style.border = "1px solid blue";
    document.getElementById('girlimg').style.border = "none";
})


document.getElementById('girlimg').addEventListener('click',function(){
    document.getElementById('id_gender_type').value = 'Female';
    document.getElementById('girlimg').style.border = "1px solid blue";
    document.getElementById('boyimg').style.border = "none";
})

document.getElementById('boyimg').style.border = "1px solid blue";