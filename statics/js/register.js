var inputs = document.querySelectorAll('.wrap-input100');
var inputelms = document.querySelectorAll(".wrap-input100 input");
var lengths = inputs.length;
var inputelmslength = inputelms.length;
var showcontent = 2;
var start = 0;
var finish = showcontent;
document.getElementById('prevbtn').style.display = 'none';

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

function showerror(id,message=1){
    if(message==1)
    document.getElementById("msg-error-"+(id+1)).innerText = "This Field is required!!";
    else
    document.getElementById("msg-error-"+(id+1)).innerText = "";
}

document.getElementById('nextbtn').addEventListener('click',function(){
    for(var i=start;i<finish;i++){
        showerror(i,message=0);
    }
    for(var i=start;i<finish;i++){
        if(is_null(elm(i))){
            showerror(i);
            return;
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