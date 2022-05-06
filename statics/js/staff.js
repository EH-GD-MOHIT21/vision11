// absdash -> Features request
// ageverdash -> age verification request




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
        let message = json["data"];
        return message;
    } else {
        alert("HTTP-Error: " + response.status);
    }
}

function show_age_ver_data(data){
    if(data.length==0){
        document.getElementById('base-dashboard').textContent = 'No pending request to show.';
        document.getElementById('base-dashboard').style.color = 'white';
        document.getElementById('base-dashboard').style.fontSize = '20px';
        document.getElementById('base-dashboard').style.fontWeight = 600;
        document.getElementById('base-dashboard').style.textAlign = 'center';
    }else{
        document.getElementById('base-dashboard').textContent = '';
    }
    for(var i=0;i<data.length;i++){
    var parent = document.getElementById('base-dashboard');
    // first child
    var fc = document.createElement('div');
    fc.setAttribute('class','staff-box');
    // first child of fc
    var maincontent = document.createElement('div');
    maincontent.setAttribute('class','main-content');
    // username div
    var username_div = document.createElement('div');
    username_div.textContent = "Email: " + data[i]['email'];
    username_div.setAttribute('class','box-topic');
    // details div
    var details_div = document.createElement('div');
    details_div.textContent = "username: "+data[i]['username']+", age: "+data[i]['age']+", country: "+data[i]['country']
    details_div.setAttribute('class','number');
    // parent of img div
    var poi = document.createElement('div');
    poi.setAttribute('class','indicator');
    var img = document.createElement('img')
    img.src = data[i]['aadhar_image'];
    poi.appendChild(img);
    // buttons div
    var btnscontainer = document.createElement('div');
    btnscontainer.setAttribute('class','links-permission');
    // var links
    var accept_link = document.createElement('a')
    accept_link.href = 'http://127.0.0.1:8000/accept_request/pid='+data[i]['id']
    accept_link.text = 'Accept Request';

    var deny_link = document.createElement('a')
    deny_link.href = 'http://127.0.0.1:8000/deny_request/pid='+data[i]['id']
    deny_link.text = 'Deny Request';

    // append sections

    btnscontainer.appendChild(accept_link);
    btnscontainer.appendChild(deny_link);

    maincontent.appendChild(username_div);
    maincontent.appendChild(details_div);
    maincontent.appendChild(poi);

    fc.appendChild(maincontent);
    fc.appendChild(btnscontainer);

    parent.appendChild(fc);
    }
}


function show_feature_request(data){
    if(data.length==0){
        document.getElementById('base-dashboard-1').textContent = 'No pending request to show.';
        document.getElementById('base-dashboard-1').style.color = 'white';
        document.getElementById('base-dashboard-1').style.fontSize = '20px';
        document.getElementById('base-dashboard-1').style.fontWeight = 600;
        document.getElementById('base-dashboard-1').style.textAlign = 'center';
    }else{
        document.getElementById('base-dashboard-1').textContent = '';
    }
    for(var i=0;i<data.length;i++){
        var parent = document.getElementById('base-dashboard-1');
        // first child
        var fc = document.createElement('div');
        fc.setAttribute('class','staff-box');
        // first child of fc
        var maincontent = document.createElement('div');
        maincontent.setAttribute('class','main-content');
        // username div
        var username_div = document.createElement('div');
        username_div.textContent = "Email: " + data[i]['user_email'];
        username_div.setAttribute('class','box-topic');
        // details div
        var details_div = document.createElement('div');
        details_div.textContent = "username: "+data[i]['user_first_name']+ " " +data[i]['user_last_name']
        details_div.setAttribute('class','number');
        // parent of img div
        var poi = document.createElement('div');
        poi.setAttribute('class','indicator');
        poi.innerHTML = "Feature title: " + data[i]["feature_title"] + "<br>" + data[i]["feature_des"]
        // buttons div
        var btnscontainer = document.createElement('div');
        btnscontainer.setAttribute('class','links-permission');
        // var links
    
        var deny_link = document.createElement('a')
        deny_link.href = 'http://127.0.0.1:8000/fr/mark_as_seen/fid='+data[i]['id']
        deny_link.text = 'mark as seen';
    
        // append sections
    
        btnscontainer.appendChild(deny_link);
    
        maincontent.appendChild(username_div);
        maincontent.appendChild(details_div);
        maincontent.appendChild(poi);
    
        fc.appendChild(maincontent);
        fc.appendChild(btnscontainer);
    
        parent.appendChild(fc);
        }
}

ids = ["ageverdash","absdash"]

document.getElementById('ageverdash').addEventListener('click',async function(){
    document.getElementById('base-dashboard-1').style.display = 'none';
    document.getElementById('base-dashboard').style.display = 'block';
    for(id of ids){
        document.getElementById(id).classList.remove('active');
    }
    if(!document.getElementById('ageverdash').classList.contains('active'))
        document.getElementById('ageverdash').classList.add('active');
    data = await get_data('/getageverificationrequests');
    show_age_ver_data(data)
})

document.getElementById('absdash').addEventListener('click', async function(){
    document.getElementById('base-dashboard').style.display = 'none';
    document.getElementById('base-dashboard-1').style.display = 'block';
    for(id of ids){
        document.getElementById(id).classList.remove('active');
    }
    if(!document.getElementById('absdash').classList.contains('active'))
        document.getElementById('absdash').classList.add('active');
    data = await get_data('/getfeaturerequests');
    show_feature_request(data)
})

if(document.URL.includes('absdash')){
    document.getElementById('absdash').click();
}else{
    document.getElementById('ageverdash').click();
}
