async function get_data(url){
    let response = await fetch(url, {
        credentials: 'include',
        method: 'GET',
        mode: 'same-origin',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    })
    if (response.ok) {
        let json = await response.json();
        let message = json["plans"];
        let banner = json["banner"];
        return [message,banner];
    } else {
        alert("HTTP-Error: " + response.status);
    }
}



function mohit(id){
    new_val = id.textContent.split(':')
    minutes = parseInt(new_val[0]);
    seconds = parseInt(new_val[1]);
    if(seconds>0){
        seconds-=1
    }else if(minutes>0){
        seconds = 59
        minutes -= 1;
    }else{
        minutes = 0;
        seconds = 0;
        clearInterval(promise);
    }
    id.textContent = minutes+":"+seconds;
}


function show_purchase_offers(data){
    if(data.length==0){
        document.getElementById('purchase-dashboard-main-container').textContent = 'No pending request to show.';
        document.getElementById('purchase-dashboard-main-container').style.color = 'white';
        document.getElementById('purchase-dashboard-main-container').style.fontSize = '20px';
        document.getElementById('purchase-dashboard-main-container').style.fontWeight = 600;
        document.getElementById('purchase-dashboard-main-container').style.textAlign = 'center';
    }else{
        document.getElementById('purchase-dashboard-main-container').textContent = '';
    }
    for(var i=0;i<data[0].length;i++){
    var div = document.createElement('div');
    div.setAttribute('class','card')
    if(data[1][i]){
        var sdiv = document.createElement('div')
        sdiv.setAttribute('class','tag-limited-time-offer')
        sdiv.textContent = 'Expire Soon'
        div.appendChild(sdiv);
    }
    var cdiv = document.createElement('div');
    cdiv.setAttribute('class','parentplans')

    var h1 = document.createElement('h1');
    h1.setAttribute('class','title');
    h1.textContent = 'You\'ll get '+ data[0][i].vision_coins +' vision coins'
    var small = document.createElement('small');
    small.setAttribute('class','muted')
    small.textContent = 'You\'ll charged ₹'+ data[0][i].plan_price +' with '+ data[0][i].bonus_coins +' extra vision coins.'

    if(data[1][i]){
        var sp = document.createElement('p')
        sp.style.color = 'crimson';
        var span1 = document.createElement('span');
        span1.textContent='Offer ends in: ';
        var span2 = document.createElement('span');
        span2.setAttribute('id',i);
        span2.textContent = parseInt(data[1][i]/60)+":"+parseInt(data[1][i]-parseInt(data[1][i]/60)*60);
        promise = setInterval(mohit,999,span2);
        sp.appendChild(span1);
        sp.appendChild(span2);
        small.appendChild(sp);
    }
                    


    var cdivinner = document.createElement('div');
    cdivinner.setAttribute('class','btn_container')
    var btn = document.createElement('button');
    btn.setAttribute('class','btn')
    btn.setAttribute('id','pay-btn-'+data[0][i].id)
    btn.onclick = function(){window.location.href='/purchase/offer='+this.id.split('-')[this.id.split('-').length-1];}
    btn.textContent = 'Pay Now';

    cdivinner.appendChild(btn);
    cdiv.appendChild(h1);
    cdiv.appendChild(small);
    cdiv.appendChild(cdivinner);
    div.appendChild(cdiv);

    document.getElementById('purchase-dashboard-main-container').appendChild(div);
    }
}


async function show_purchase(){
    data = await get_data('/getplans');
    show_purchase_offers(data)
}



if(document.URL.includes('purchase')){
    show_purchase();
}

document.getElementById('purchase').addEventListener('click',function(){
    show_purchase();
})