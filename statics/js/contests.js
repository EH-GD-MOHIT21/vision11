function show_public(){
    class_list = document.getElementById('public_contest').classList
    class_list.add("active");
    class_list1 = document.getElementById('private_contest').classList
    class_list1.remove('active')
    class_list2 = document.getElementById('create_contest').classList
    class_list2.remove('active')
    document.getElementById('public').style.display='block';
    document.getElementById('private_parent').style.display='none';
    document.getElementById('create_cont').style.display='none';
}

function show_private(){
    class_list = document.getElementById('public_contest').classList
    class_list.remove("active");
    class_list1 = document.getElementById('private_contest').classList
    class_list1.add('active')
    class_list2 = document.getElementById('create_contest').classList
    class_list2.remove('active')
    document.getElementById('public').style.display='none';
    document.getElementById('private_parent').style.display='block';
    document.getElementById('create_cont').style.display='none';
}

function show_createcontest(){
    class_list = document.getElementById('public_contest').classList
    class_list.remove("active");
    class_list1 = document.getElementById('private_contest').classList
    class_list1.remove('active')
    class_list2 = document.getElementById('create_contest').classList
    class_list2.add('active')
    document.getElementById('public').style.display='none';
    document.getElementById('private_parent').style.display='none';
    document.getElementById('create_cont').style.display='block';
}

function myFunction(){
    var x = document.getElementById("type_conteste").value;
    if(x == 'private'){
        document.getElementById('contest_pass_create').style.display='block';
    }
    else{
        document.getElementById('contest_pass_create').style.display='none';
    }
}

function getCookie(name) {
    if (!document.cookie) {
        return null;
    }
    
    const xsrfCookies = document.cookie.split(';')
        .map(c => c.trim())
        .filter(c => c.startsWith(name + '='));
    
    if (xsrfCookies.length === 0) {
        return null;
    }
    return decodeURIComponent(xsrfCookies[0].split('=')[1]);
}

document.getElementById('create_con').addEventListener('click', async function(){
    var c_name = document.getElementById('contest_price').value;
    var c_length = document.getElementById('contest_max_mem').value;
    var c_type = document.getElementById('type_conteste').value;
    var password = document.getElementById('contest_pass_create').value;
    var team = document.getElementById('user_team').value;
    let response = await fetch("/createcontestapi", {
        credentials: 'include',
        method: 'POST',
        mode: 'same-origin',
        headers: {
            'X-CSRFToken': getCookie('X-CSRFToken'),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'entry_fee': c_name,
            'length': c_length,
            'type': c_type,
            'match_id': document.URL.split("#")[0].split('=')[1],
            'password': password,
            "team": team
        })
    })
    if (response.ok) {
        let json = await response.json();
        let message = json["message"];
        let id = json["contest_id"];
        if(message=='success'){
            window.location.href = '/view/contest='+ id+'/match='+document.URL.split("#")[0].split('=')[1]
        }else{
            alert(message);
        }
    } else {
        alert("HTTP-Error: " + response.status);
    }
})

function show_user_team(){
    team = document.getElementById("user_team").value;
    window.open(
        '/userteam/match='+team,
        '_blank'
      );
}


document.getElementById('search_con').addEventListener('click', async function(){
    var c_name = document.getElementById('contest_id').value;
    var password = document.getElementById('contest_pass').value;
    let response = await fetch("/searchcontestapi", {
        credentials: 'include',
        method: 'POST',
        mode: 'same-origin',
        headers: {
            'X-CSRFToken': getCookie('X-CSRFToken'),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'contest_id': c_name,
            'match_id': document.URL.split("#")[0].split('=')[1],
            'password': password
        })
    })
    if (response.ok) {
        let json = await response.json();
        let message = json["message"];
        if(message=='success'){
            let data = json["data"];
            document.getElementById('prizeprivate').textContent = data['price_fee'];
            document.getElementById('entryfeeprivate').textContent = data['entry_fee'] + " " + data["fee_type"];
            document.getElementById('private_spot_left1').textContent = parseInt(data["length"])-data["user"].length + " Spots left";
            document.getElementById('private_total_spots1').textContent = data["length"] + " Spots"
            document.getElementById('private_prog1').value = (data["user"].length/data["length"])*100
        }
        if(message=='success'){
            document.getElementById('privatesearchresult').style.display = 'block';
        }else{
            alert(message);
        }
    } else {
        alert("HTTP-Error: " + response.status);
    }
})


async function joinc(contest_id){
    var team_id = document.getElementById('user_default_team_id').value;

    let response = await fetch("/joincontestapi", {
        credentials: 'include',
        method: 'POST',
        mode: 'same-origin',
        headers: {
            'X-CSRFToken': getCookie('X-CSRFToken'),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'team_id': team_id,
            'contest_id': contest_id,
        })
    })
    if (response.ok) {
        let json = await response.json();
        let message = json["message"];
        let id = json["contest_id"];
        if(message=='success'){
            window.location.href = '/view/contest='+ id+'/match='+document.URL.split("#")[0].split('=')[1]
        }else{
            alert(message);
        }
    } else {
        alert("HTTP-Error: " + response.status);
    }
}