/* Calling api part */

const live_mathc_api_url =
	"/getlivematches";

const upcoming_match_api_url = '/getupcomingmatches';

const completed_match_api_url = "/getcompletedmatches";
upcoming_match_numbers = 0;

async function live_match_data(api_url) {
let response = await fetch(api_url, {
    credentials: 'include',
    method: 'GET',
    mode: 'same-origin',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
})
if (response.ok) {
    let json = await response.json();
    match_data = json['data']
    res_len = match_data.length;
    for (let i = 0; i < res_len; i++) {
        const match_card = document.createElement("div");
        match_card.className = 'match_card';
        const span_match_card = document.createElement("span");
        span_match_card.textContent = 'Started...';
        match_card.appendChild(span_match_card)
        const match_heading = document.createElement("h3");
        match_heading.textContent = `${match_data[i].title}`;
        match_card.appendChild(match_heading);
        const teams = document.createElement("div");
        teams.className ='teams';
        match_card.appendChild(teams)
        const team1info = document.createElement("div");
        team1info.className ='team1info';
        teams.appendChild(team1info);
        const team1_img = document.createElement("img");
        team1_img.src = `${match_data[i].team1_img}`;
        team1info.appendChild(team1_img);
        const team1_label = document.createElement("label");
        team1_label.textContent = `${match_data[i].team1}`;
        team1info.appendChild(team1_label);
        const vs = document.createElement("div")
        vs.className='vs';
        vs.textContent ='VS';
        teams.appendChild(vs);
        const team2info = document.createElement("div");
        team2info.className ='team2info';
        teams.appendChild(team2info);
        const team2_img = document.createElement("img");
        team2_img.src = `${match_data[i].team2_img}`;
        team2info.appendChild(team2_img);
        const team2_label = document.createElement("label");
        team2_label.textContent = `${match_data[i].team2}`;
        team2info.appendChild(team2_label);
        const create_button = document.createElement("div")
        create_button.className = 'createbutton';
        match_card.appendChild(create_button)
        const a_but = document.createElement("a")
        a_but.textContent = 'Check points'
        a_but.href = '/viewcontest/match='+ match_data[i].id;
        a_but.target = "blank"
        create_button.appendChild(a_but);
        const element = document.getElementById("live");
        element.appendChild(match_card);
    }
} else {
    alert("HTTP-Error: " + response.status);
}
} 


async function upcoming_match_data(api_url) {
    let response = await fetch(api_url, {
        credentials: 'include',
        method: 'GET',
        mode: 'same-origin',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
    })
    if (response.ok) {
        let json = await response.json();
        match_data = json['data']
        res_len = match_data.length;
        upcoming_match_numbers = res_len;
        for (let i = 0; i < res_len; i++) {
            const match_card = document.createElement("div");
            match_card.className = 'match_card';
            const span_match_card1 = document.createElement("span");
            span_match_card1.textContent = 'Start after: ';
            const span_match_card = document.createElement("span");
            get_time = match_timing(match_data[i].time)
            span_match_card.textContent = get_time;
            span_match_card.id = `match${i}`;
            match_card.appendChild(span_match_card1)
            match_card.appendChild(span_match_card)
            const match_heading = document.createElement("h3");
            match_heading.textContent = `${match_data[i].title}`;
            match_card.appendChild(match_heading);
            const teams = document.createElement("div");
            teams.className ='teams';
            match_card.appendChild(teams)
            const team1info = document.createElement("div");
            team1info.className ='team1info';
            teams.appendChild(team1info);
            const team1_img = document.createElement("img");
            team1_img.src = `${match_data[i].team1_img}`;
            team1info.appendChild(team1_img);
            const team1_label = document.createElement("label");
            team1_label.textContent = `${match_data[i].team1}`;
            team1info.appendChild(team1_label);
            const vs = document.createElement("div")
            vs.className='vs';
            vs.textContent ='VS';
            teams.appendChild(vs);
            const team2info = document.createElement("div");
            team2info.className ='team2info';
            teams.appendChild(team2info);
            const team2_img = document.createElement("img");
            team2_img.src = `${match_data[i].team2_img}`;
            team2info.appendChild(team2_img);
            const team2_label = document.createElement("label");
            team2_label.textContent = `${match_data[i].team2}`;
            team2info.appendChild(team2_label);
            const element = document.getElementById("upcoming");
            const create_button = document.createElement("div");
            create_button.className = 'createbutton';
            match_card.appendChild(create_button)
            const a_but = document.createElement("a")
            a_but.textContent = 'Create Team'
            const a_but1 = document.createElement("a")
            a_but1.textContent = 'Go to Contest'
            a_but1.href = '/contest/match='+match_data[i].id
            a_but.href = '/createteam/match='+match_data[i].id
            create_button.appendChild(a_but);
            create_button.appendChild(a_but1);
            element.appendChild(match_card);
        }
    } else {
        alert("HTTP-Error: " + response.status);
    }
    }    

    async function completed_match_data(api_url) {
        let response = await fetch(api_url, {
            credentials: 'include',
            method: 'GET',
            mode: 'same-origin',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
        })
        if (response.ok) {
            let json = await response.json();
            match_data = json['data']
            res_len = match_data.length;
            for (let i = 0; i < res_len; i++) {
                console.log('completed_matches')
                const match_card = document.createElement("div");
                match_card.className = 'match_card';
                const span_match_card = document.createElement("span");
                span_match_card.textContent = 'Completed';
                match_card.appendChild(span_match_card)
                const match_heading = document.createElement("h3");
                match_heading.textContent = `${match_data[i].title}`;
                match_card.appendChild(match_heading);
                const teams = document.createElement("div");
                teams.className ='teams';
                match_card.appendChild(teams)
                const team1info = document.createElement("div");
                team1info.className ='team1info';
                teams.appendChild(team1info);
                const team1_img = document.createElement("img");
                team1_img.src = `${match_data[i].team1_img}`;
                team1info.appendChild(team1_img);
                const team1_label = document.createElement("label");
                team1_label.textContent = `${match_data[i].team1}`;
                team1info.appendChild(team1_label);
                const vs = document.createElement("div")
                vs.className='vs';
                vs.textContent ='VS';
                teams.appendChild(vs);
                const team2info = document.createElement("div");
                team2info.className ='team2info';
                teams.appendChild(team2info);
                const team2_img = document.createElement("img");
                team2_img.src = `${match_data[i].team2_img}`;
                team2info.appendChild(team2_img);
                const team2_label = document.createElement("label");
                team2_label.textContent = `${match_data[i].team2}`;
                team2info.appendChild(team2_label);
                const element = document.getElementById("completed");
                const create_button = document.createElement("div");
                create_button.className = 'createbutton';
                match_card.appendChild(create_button)
                const a_but = document.createElement("a")
                a_but.textContent = 'Show Team'
                a_but.href = '/viewcontest/match='+ match_data[i].id;
                create_button.appendChild(a_but);
                element.appendChild(match_card);
            }
        } else {
            alert("HTTP-Error: " + response.status);
        }
        }    
    

completed_match_data(completed_match_api_url);
live_match_data(live_mathc_api_url);
upcoming_match_data(upcoming_match_api_url);



/* api part ends here--------------*/




function show_completed(){
    class_list = document.getElementById('completed_match').classList
    class_list.add("active")
    class_list1 = document.getElementById('live_match').classList
    class_list1.remove('active')
    class_list2 = document.getElementById('Upcoming').classList
    class_list2.remove('active')
    document.getElementById('completed').style.display='';
    document.getElementById('live').style.display='none';
    document.getElementById('upcoming').style.display='none';
}

function show_live(){
    class_list = document.getElementById('live_match').classList
    class_list.add("active")
    class_list1 = document.getElementById('completed_match').classList
    class_list1.remove('active')
    class_list2 = document.getElementById('Upcoming').classList
    class_list2.remove('active')
    document.getElementById('completed').style.display='none';
    document.getElementById('live').style.display='block';
    document.getElementById('upcoming').style.display='none';
}

function show_upcoming(){
    class_list = document.getElementById('Upcoming').classList
    class_list.add("active")
    class_list1 = document.getElementById('live_match').classList
    class_list1.remove('active')
    class_list2 = document.getElementById('completed_match').classList
    class_list2.remove('active')
    document.getElementById('completed').style.display='none';
    document.getElementById('live').style.display='none';
    document.getElementById('upcoming').style.display='block';
}

function match_timing(seconds){
    seconds = parseInt(seconds)
    var days = Math.floor(seconds / (3600*24));
    var hours = Math.floor(seconds % (3600*24) / 3600);
    var minutes = Math.floor(seconds % 3600 / 60);
    var second = Math.floor(seconds % 60);
    if(days==0){
        if(hours<10){
            hours = `0${hours}`
        }
        if(minutes<10){
            minutes = `0${minutes}`
        }
        match_time = `${hours}:${minutes}:${second}`;
    }
    else{
        if(days<10){
            days = `0${days}`
        }
        if(hours<10){
            hours = `0${hours}`
        }
        if(minutes<10){
            minutes = `0${minutes}`
        }
        match_time = `${days}:${hours}:${minutes}:${second}`;
    }
    return match_time 
}


function updateTime() {
    total_mat = upcoming_match_numbers
    for(var i=0;i< total_mat;i++){
        timing = (document.getElementById('match'+i).textContent).split(":");
        if(timing.length==3){
        hour = parseInt(timing[0]);
        minute = parseInt(timing[1]);
        sec = parseInt(timing[2]);
        if(sec > 0){
            sec-=1;
            
        }
        else if(minute>0){
            sec = 59;
            minute -=1;
            
        }
        else if(hour>0){
            sec = 59;
            minute = 60;
            hour-=1;
            
        }
        else{
            sec = 0;
            minute = 0;
            hour = 0;
        }
        if(sec < 10){
            sec = `0${sec}`
        }
        if(minute < 10){
            minute = `0${minute}`
        }
        if(hour < 10){
            hour = `0${hour}`
        }
        document.getElementById('match'+i).textContent = hour+":"+minute+":"+sec;
    }
    else{
        day = parseInt(timing[0]);
        hour = parseInt(timing[1]);
        minute = parseInt(timing[2]);
        sec = parseInt(timing[3]);
        if(sec > 0){
            sec-=1;
            
        }
        else if(minute>0){
            sec = 59;
            minute -=1;
            
        }
        else if(hour>0){
            sec = 59;
            minute = 60;
            hour-=1;
            
        }
        else if(day>0){
            day -= 1;
            hour = 24;
            minute = 59;
            sec = 59;
            
        }
        else{
            day=0;
            sec = 0;
            minute = 0;
            hour = 0;
        }
        if(sec < 10){
            sec = `0${sec}`
        }
        if(minute < 10){
            minute = `0${minute}`
        }
        if(hour < 10){
            hour = `0${hour}`
        }
        if(day < 10){
            day = `0${day}`
        }
        document.getElementById('match'+i).textContent = day+":"+hour+":"+minute+":"+sec;

    }
    }
     
}

setInterval(updateTime, 1000);