/* Calling api part */

const live_mathc_api_url =
	"/getlivematches";

const upcoming_match_api_url = '/getupcomingmatches';

const completed_match_api_url = "/getcompletedmatches";

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
        for (let i = 0; i < res_len; i++) {
            console.log('completed_matches')
            const match_card = document.createElement("div");
            match_card.className = 'match_card';
            const span_match_card = document.createElement("span");
            span_match_card.textContent = `${match_data[i].time}`;
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
            a_but.href = '/createteam/match='+match_data[i].id
            create_button.appendChild(a_but);
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

