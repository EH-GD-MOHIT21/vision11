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


function show_live_matches_data(data){
    console.log(data);
    for(var i=0;i<data.length;i++){
        const match_card = document.createElement("div");
            match_card.className = 'match_card';
            const span_match_card = document.createElement("span");
            span_match_card.textContent = `Match id : ${data[i].id}`;
            span_match_card.id = `${i}`;
            match_card.appendChild(span_match_card)
            const match_heading = document.createElement("h3");
            match_heading.textContent = `${data[i].name}`;
            match_card.appendChild(match_heading);
            const teams = document.createElement("div");
            teams.className ='teams';
            match_card.appendChild(teams)
            const team1info = document.createElement("div");
            team1info.className ='team1info';
            teams.appendChild(team1info);
            const team1_img = document.createElement("img");
            team1_img.src = `${data[i].team1_img}`;
            team1info.appendChild(team1_img);
            const team1_label = document.createElement("label");
            team1_label.textContent = `${data[i].team1}`;
            team1info.appendChild(team1_label);
            const vs = document.createElement("div")
            vs.className='vs';
            vs.textContent ='VS';
            teams.appendChild(vs);
            const team2info = document.createElement("div");
            team2info.className ='team2info';
            teams.appendChild(team2info);
            const team2_img = document.createElement("img");
            team2_img.src = `${data[i].team2_img}`;
            team2info.appendChild(team2_img);
            const team2_label = document.createElement("label");
            team2_label.textContent = `${data[i].team2}`;
            team2info.appendChild(team2_label);
            const element = document.getElementById("livematches_container");
            const create_button = document.createElement("div");
            create_button.className = 'createbutton';
            match_card.appendChild(create_button)
            const a_but = document.createElement("a")
            a_but.textContent = 'Match Ended'
            a_but.setAttribute("onclick","set_match_end('"+data[i].id+"')")
            create_button.appendChild(a_but);
            element.appendChild(match_card);
    }

}



ids = ["ageverdash","absdash","livematches","userinfo"]
mids = ["base-dashboard","base-dashboard-1","livematches_container","userinfodetails"]

document.getElementById('ageverdash').addEventListener('click',async function(){
    for(id of mids){
        document.getElementById(id).style.display = 'none';
    }
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
    for(id of mids){
        document.getElementById(id).style.display = 'none';
    }
    document.getElementById('base-dashboard-1').style.display = 'block';
    for(id of ids){
        document.getElementById(id).classList.remove('active');
    }
    if(!document.getElementById('absdash').classList.contains('active'))
        document.getElementById('absdash').classList.add('active');
    data = await get_data('/getfeaturerequests');
    show_feature_request(data)
})

document.getElementById('livematches').addEventListener('click', async function(){
    for(id of mids){
        document.getElementById(id).style.display = 'none';
    }
    document.getElementById('livematches_container').style.display = 'block';
    for(id of ids){
        document.getElementById(id).classList.remove('active');
    }
    if(!document.getElementById('livematches').classList.contains('active'))
        document.getElementById('livematches').classList.add('active');
    data = await get_data('/getlivematches');
    show_live_matches_data(data)
})

document.getElementById('userinfo').addEventListener('click', async function(){
    for(id of mids){
        document.getElementById(id).style.display = 'none';
    }
    document.getElementById('userinfodetails').style.display = 'block';
    for(id of ids){
        document.getElementById(id).classList.remove('active');
    }
    if(!document.getElementById('userinfo').classList.contains('active'))
        document.getElementById('userinfo').classList.add('active');
})

async function dothisforsearchuser(){
    var username = document.getElementById('user_name_search_field').value;
    if (username == '' || username.length < 1){
        return
    }
    data = await get_data('/get_user_info/user='+username);
    const main_div = document.getElementById('userinfodetails')
    show_user_info_data(data,main_div);
}

document.getElementById('user_name_search_field').addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        dothisforsearchuser()
    }
});

document.getElementById('finduserico').addEventListener('click',dothisforsearchuser)

if(document.URL.includes('absdash')){
    document.getElementById('absdash').click();
}else if(document.URL.includes('livematches')){
    document.getElementById('livematches').click();
}else if(document.URL.includes('userinfo')){
    document.getElementById('userinfo').click();
}
else{
    document.getElementById('ageverdash').click()
}


async function is_match_end(url){
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
        let message = await json["message"];
        return message;
    } else {
        alert("HTTP-Error: " + response.status);
    }
}


function set_match_end(id){
    let isExecuted = confirm("Are you sure to match is ended ?");
    if (isExecuted) {
        url = '/is_match_end_true/match='+id;
        msg =is_match_end(url)
        console.log(msg)
      } 
}
