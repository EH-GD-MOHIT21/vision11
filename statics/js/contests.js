function show_public(){
    class_list = document.getElementById('public_contest').classList
    class_list.add("active");
    class_list1 = document.getElementById('private_contest').classList
    class_list1.remove('active')
    class_list2 = document.getElementById('create_contest').classList
    class_list2.remove('active')
    document.getElementById('public').style.display='block';
    document.getElementById('private').style.display='none';
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
    document.getElementById('private').style.display='block';
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
    document.getElementById('private').style.display='none';
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
    var c_name = document.getElementById('contest_name').value;
    var c_length = document.getElementById('contest_max_mem').value;
    var c_type = document.getElementById('type_conteste').value;
    var password = document.getElementById('contest_pass_create').value;
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
            'name': c_name,
            'length': c_length,
            'type': c_type,
            'match_id': document.URL.split('=')[1],
            'password': password
        })
    })
    if (response.ok) {
        let json = await response.json();
        let message = json["message"];
        if(message=='success'){
            window.location.href = '/contest/match='+document.URL.split('=')[1]
        }else{
            alert(message);
        }
    } else {
        alert("HTTP-Error: " + response.status);
    }
})