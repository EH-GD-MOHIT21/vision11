team1_name = JSON.parse(document.getElementById('team1').textContent);
team2_name = JSON.parse(document.getElementById('team2').textContent);
user_team_data=[]
individual_player_data = {}

const team_players_api  =
	"/gettodayssquadlist";

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

async function player_api_data(api_url) {
    const csrfToken = getCookie('X-CSRFToken');
    let response = await fetch(api_url, {
        credentials: 'include',
        method: 'POST',
        mode: 'same-origin',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({
            "team1": team1_name,
            "team2": team2_name
        })
    })
    if (response.ok) {
        let json = await response.json();
        team1_player_data = json['team1']
        team2_player_data = json['team2']
        /*-------team1 players -----*/
        team1_len = team1_player_data.length;
        team2_len = team2_player_data.length;

        for (let i = 0; i < team1_len; i++){
            if(team1_player_data[i].player_type=="WICKET KEEPER"){
                const player_img_url = team1_player_data[i].player_pic.slice(7)
                const exact_img_url = player_img_url.replace("%3A",":/")
                const main_div = document.getElementById("Wk_batting")
                const wkbatsman = document.createElement('div');
                wkbatsman.className = 'wkbat';
                wkbatsman.id = `Wk_bat${team1_player_data[i].pid}`;
                main_div.appendChild(wkbatsman);
                const player_info = document.createElement('div');
                player_info.className = 'player_info';
                wkbatsman.appendChild(player_info);
                const wkbatsman_img = document.createElement('img');
                wkbatsman_img.src = `${exact_img_url}`;
                wkbatsman_img.id = `playerimg${team1_player_data[i].pid}`;
                player_info.appendChild(wkbatsman_img);
                const player_name = document.createElement('span');
                player_name.className = 'player_name';
                player_name.id = `playername${team1_player_data[i].pid}`;
                const player_role = document.createElement('span');
                player_role.className = 'player_role';
                player_role.id = `playerrole${team1_player_data[i].pid}`;
                player_name.textContent=`${team1_player_data[i].player_name}`;
                player_role.textContent = `${team1_player_data[i].player_type}`;
                player_info.appendChild(player_name);
                player_info.appendChild(player_role);
                const credits = document.createElement('div');
                credits.className = 'credits';
                wkbatsman.appendChild(credits);
                const credit_span = document.createElement('span');
                credit_span.id = `wkcredits${team1_player_data[i].pid}`;
                credit_span.textContent = `${team1_player_data[i].player_points}`; 
                credits.appendChild(credit_span);
                const addbtn = document.createElement('div');
                addbtn.className = 'addbtn';
                wkbatsman.appendChild(addbtn);
                const plus = document.createElement('button');
                plus.className = 'plus';
                plus.id = `wk_batplus${team1_player_data[i].pid}`
                str_plus_id = String(plus.id)
                const minus = document.createElement('button');
                minus.className = 'minus';
                minus.id = `wk_batminus${team1_player_data[i].pid}`
                str_minus_id = String(minus.id)
                addbtn.appendChild(plus);
                addbtn.appendChild(minus);
                const icon_plus = document.createElement('i');
                icon_plus.className = "fa fa-plus-circle";
                icon_plus.style.fontSize = "25px";
                plus.appendChild(icon_plus)
                const icon_minus = document.createElement('i');
                icon_minus.className = "fa fa-minus-circle";
                icon_minus.style.fontSize = "25px";
                minus.appendChild(icon_minus);
                plus.setAttribute('onclick', "add_wk('"+str_plus_id+"')");
                minus.setAttribute('onclick', "rem_wk('"+str_minus_id+"')");
                const msg_div = document.createElement('div');
                msg_div.className = 'overmsg';
                msg_div.id = `wkmsg${team1_player_data[i].pid}`;
                msg_div.textContent = 'You Cannot Select more than four Wk-Batsman';
                main_div.appendChild(msg_div)
            }
            else if(team1_player_data[i].player_type=="BATSMEN"){
                const player_img_url = team1_player_data[i].player_pic.slice(7)
                const exact_img_url = player_img_url.replace("%3A",":/")
                const main_div = document.getElementById("batting")
                const wkbatsman = document.createElement('div');
                wkbatsman.className = 'batsman';
                wkbatsman.id = `bat${team1_player_data[i].pid}`;
                main_div.appendChild(wkbatsman);
                const player_info = document.createElement('div');
                player_info.className = 'player_info';
                wkbatsman.appendChild(player_info);
                const wkbatsman_img = document.createElement('img');
                wkbatsman_img.src = `${exact_img_url}`;
                wkbatsman_img.id = `playerimg${team1_player_data[i].pid}`;
                player_info.appendChild(wkbatsman_img);
                const player_name = document.createElement('span');
                player_name.id = `playername${team1_player_data[i].pid}`;
                player_name.className = 'player_name';
                const player_role = document.createElement('span');
                player_role.className = 'player_role';
                player_role.id = `playerrole${team1_player_data[i].pid}`;
                player_name.textContent=`${team1_player_data[i].player_name}`;
                player_role.textContent = `${team1_player_data[i].player_type}`;
                player_info.appendChild(player_name);
                player_info.appendChild(player_role);
                const credits = document.createElement('div');
                credits.className = 'credits';
                wkbatsman.appendChild(credits);
                const credit_span = document.createElement('span');
                credit_span.id = `batcredits${team1_player_data[i].pid}`;
                credit_span.textContent = `${team1_player_data[i].player_points}`; 
                credits.appendChild(credit_span);
                const addbtn = document.createElement('div');
                addbtn.className = 'addbtn';
                wkbatsman.appendChild(addbtn);
                const plus = document.createElement('button');
                plus.className = 'plus';
                plus.id = `batplus${team1_player_data[i].pid}`
                str_plus_id = String(plus.id)
                const minus = document.createElement('button');
                minus.className = 'minus';
                minus.id = `batminus${team1_player_data[i].pid}`
                str_minus_id = String(minus.id)
                addbtn.appendChild(plus);
                addbtn.appendChild(minus);
                const icon_plus = document.createElement('i');
                icon_plus.className = "fa fa-plus-circle";
                icon_plus.style.fontSize = "25px";
                plus.appendChild(icon_plus)
                const icon_minus = document.createElement('i');
                icon_minus.className = "fa fa-minus-circle";
                icon_minus.style.fontSize = "25px";
                minus.appendChild(icon_minus);
                plus.setAttribute('onclick', "add_bat('"+str_plus_id+"')");
                minus.setAttribute('onclick', "rem_bat('"+str_minus_id+"')");
                const msg_div = document.createElement('div');
                msg_div.className = 'overmsg';
                msg_div.id = `batmsg${team1_player_data[i].pid}`;
                msg_div.textContent = 'You Cannot Select more than Six Batsman';
                main_div.appendChild(msg_div)
            }
            else if(team1_player_data[i].player_type=="ALL ROUNDER"){
                const player_img_url = team1_player_data[i].player_pic.slice(7)
                const exact_img_url = player_img_url.replace("%3A",":/")
                const main_div = document.getElementById("all_rounding")
                const wkbatsman = document.createElement('div');
                wkbatsman.className = 'allround';
                wkbatsman.id = `all_round${team1_player_data[i].pid}`;
                main_div.appendChild(wkbatsman);
                const player_info = document.createElement('div');
                player_info.className = 'player_info';
                wkbatsman.appendChild(player_info);
                const wkbatsman_img = document.createElement('img');
                wkbatsman_img.src = `${exact_img_url}`;
                wkbatsman_img.id = `playerimg${team1_player_data[i].pid}`;
                player_info.appendChild(wkbatsman_img);
                const player_name = document.createElement('span');
                player_name.className = 'player_name';
                player_name.id = `playername${team1_player_data[i].pid}`;
                const player_role = document.createElement('span');
                player_role.className = 'player_role';
                player_role.id = `playerrole${team1_player_data[i].pid}`;
                player_name.textContent=`${team1_player_data[i].player_name}`;
                player_role.textContent = `${team1_player_data[i].player_type}`;
                player_info.appendChild(player_name);
                player_info.appendChild(player_role);
                const credits = document.createElement('div');
                credits.className = 'credits';
                wkbatsman.appendChild(credits);
                const credit_span = document.createElement('span');
                credit_span.id = `allcredits${team1_player_data[i].pid}`;
                credit_span.textContent = `${team1_player_data[i].player_points}`; 
                credits.appendChild(credit_span);
                const addbtn = document.createElement('div');
                addbtn.className = 'addbtn';
                wkbatsman.appendChild(addbtn);
                const plus = document.createElement('button');
                plus.className = 'plus';
                plus.id = `allplus${team1_player_data[i].pid}`
                str_plus_id = String(plus.id)
                const minus = document.createElement('button');
                minus.className = 'minus';
                minus.id = `allminus${team1_player_data[i].pid}`
                str_minus_id = String(minus.id)
                addbtn.appendChild(plus);
                addbtn.appendChild(minus);
                const icon_plus = document.createElement('i');
                icon_plus.className = "fa fa-plus-circle";
                icon_plus.style.fontSize = "25px";
                plus.appendChild(icon_plus)
                const icon_minus = document.createElement('i');
                icon_minus.className = "fa fa-minus-circle";
                icon_minus.style.fontSize = "25px";
                minus.appendChild(icon_minus);
                plus.setAttribute('onclick', "add_round('"+str_plus_id+"')");
                minus.setAttribute('onclick', "rem_round('"+str_minus_id+"')");
                const msg_div = document.createElement('div');
                msg_div.className = 'overmsg';
                msg_div.id = `allmsg${team1_player_data[i].pid}`;
                msg_div.textContent = 'You Cannot Select more than four All-Rounder';
                main_div.appendChild(msg_div)
            }

            else if(team1_player_data[i].player_type=="BOWLER"){
                const player_img_url = team1_player_data[i].player_pic.slice(7)
                const exact_img_url = player_img_url.replace("%3A",":/")
                const main_div = document.getElementById("bowling")
                const wkbatsman = document.createElement('div');
                wkbatsman.className = 'bowler';
                wkbatsman.id = `bowl${team1_player_data[i].pid}`;
                main_div.appendChild(wkbatsman);
                const player_info = document.createElement('div');
                player_info.className = 'player_info';
                wkbatsman.appendChild(player_info);
                const wkbatsman_img = document.createElement('img');
                wkbatsman_img.src = `${exact_img_url}`;
                wkbatsman_img.id = `playerimg${team1_player_data[i].pid}`;
                player_info.appendChild(wkbatsman_img);
                const player_name = document.createElement('span');
                player_name.className = 'player_name';
                player_name.id = `playername${team1_player_data[i].pid}`;
                const player_role = document.createElement('span');
                player_role.className = 'player_role';
                player_role.id = `playerrole${team1_player_data[i].pid}`;
                player_name.textContent=`${team1_player_data[i].player_name}`;
                player_role.textContent = `${team1_player_data[i].player_type}`;
                player_info.appendChild(player_name);
                player_info.appendChild(player_role);
                const credits = document.createElement('div');
                credits.className = 'credits';
                wkbatsman.appendChild(credits);
                const credit_span = document.createElement('span');
                credit_span.id = `bowlcredits${team1_player_data[i].pid}`;
                credit_span.textContent = `${team1_player_data[i].player_points}`; 
                credits.appendChild(credit_span);
                const addbtn = document.createElement('div');
                addbtn.className = 'addbtn';
                wkbatsman.appendChild(addbtn);
                const plus = document.createElement('button');
                plus.className = 'plus';
                plus.id = `bowlplus${team1_player_data[i].pid}`
                str_plus_id = String(plus.id)
                const minus = document.createElement('button');
                minus.className = 'minus';
                minus.id = `bowlminus${team1_player_data[i].pid}`
                str_minus_id = String(minus.id)
                addbtn.appendChild(plus);
                addbtn.appendChild(minus);
                const icon_plus = document.createElement('i');
                icon_plus.className = "fa fa-plus-circle";
                icon_plus.style.fontSize = "25px";
                plus.appendChild(icon_plus)
                const icon_minus = document.createElement('i');
                icon_minus.className = "fa fa-minus-circle";
                icon_minus.style.fontSize = "25px";
                minus.appendChild(icon_minus);
                plus.setAttribute('onclick', "add_bowl('"+str_plus_id+"')");
                minus.setAttribute('onclick', "rem_bowl('"+str_minus_id+"')");
                const msg_div = document.createElement('div');
                msg_div.className = 'overmsg';
                msg_div.id = `bowlmsg${team1_player_data[i].pid}`;
                msg_div.textContent = 'You Cannot Select more than Six Bowlers';
                main_div.appendChild(msg_div)
            }
        }

        for (let i = 0; i < team2_len; i++){
            if(team2_player_data[i].player_type=="WICKET KEEPER"){
                const player_img_url = team2_player_data[i].player_pic.slice(7)
                const exact_img_url = player_img_url.replace("%3A",":/")
                const main_div = document.getElementById("Wk_batting")
                const wkbatsman = document.createElement('div');
                wkbatsman.className = 'wkbat';
                wkbatsman.id = `Wk_bat${team2_player_data[i].pid}`;
                main_div.appendChild(wkbatsman);
                const player_info = document.createElement('div');
                player_info.className = 'player_info';
                wkbatsman.appendChild(player_info);
                const wkbatsman_img = document.createElement('img');
                wkbatsman_img.src = `${exact_img_url}`;
                wkbatsman_img.id = `playerimg${team2_player_data[i].pid}`;
                player_info.appendChild(wkbatsman_img);
                const player_name = document.createElement('span');
                player_name.className = 'player_name';
                player_name.id = `playername${team2_player_data[i].pid}`;
                const player_role = document.createElement('span');
                player_role.className = 'player_role';
                player_role.id = `playerrole${team2_player_data[i].pid}`;
                player_name.textContent=`${team2_player_data[i].player_name}`;
                player_role.textContent = `${team2_player_data[i].player_type}`;
                player_info.appendChild(player_name);
                player_info.appendChild(player_role);
                const credits = document.createElement('div');
                credits.className = 'credits';
                wkbatsman.appendChild(credits);
                const credit_span = document.createElement('span');
                credit_span.id = `wkcredits${team2_player_data[i].pid}`;
                credit_span.textContent = `${team2_player_data[i].player_points}`; 
                credits.appendChild(credit_span);
                const addbtn = document.createElement('div');
                addbtn.className = 'addbtn';
                wkbatsman.appendChild(addbtn);
                const plus = document.createElement('button');
                plus.className = 'plus';
                plus.id = `wk_batplus${team2_player_data[i].pid}`
                str_plus_id = String(plus.id)
                const minus = document.createElement('button');
                minus.className = 'minus';
                minus.id = `wk_batminus${team2_player_data[i].pid}`
                str_minus_id = String(minus.id)
                addbtn.appendChild(plus);
                addbtn.appendChild(minus);
                const icon_plus = document.createElement('i');
                icon_plus.className = "fa fa-plus-circle";
                icon_plus.style.fontSize = "25px";
                plus.appendChild(icon_plus)
                const icon_minus = document.createElement('i');
                icon_minus.className = "fa fa-minus-circle";
                icon_minus.style.fontSize = "25px";
                minus.appendChild(icon_minus);
                plus.setAttribute('onclick', "add_wk('"+str_plus_id+"')");
                minus.setAttribute('onclick', "rem_wk('"+str_minus_id+"')");
                const msg_div = document.createElement('div');
                msg_div.className = 'overmsg';
                msg_div.id = `wkmsg${team2_player_data[i].pid}`;
                msg_div.textContent = 'You Cannot Select more than four Wk-Batsmans';
                main_div.appendChild(msg_div)
            }
            else if(team2_player_data[i].player_type=="BATSMEN"){
                const player_img_url = team2_player_data[i].player_pic.slice(7)
                const exact_img_url = player_img_url.replace("%3A",":/")
                const main_div = document.getElementById("batting")
                const wkbatsman = document.createElement('div');
                wkbatsman.className = 'batsman';
                wkbatsman.id = `bat${team2_player_data[i].pid}`;
                main_div.appendChild(wkbatsman);
                const player_info = document.createElement('div');
                player_info.className = 'player_info';
                wkbatsman.appendChild(player_info);
                const wkbatsman_img = document.createElement('img');
                wkbatsman_img.src = `${exact_img_url}`;
                wkbatsman_img.id = `playerimg${team2_player_data[i].pid}`;
                player_info.appendChild(wkbatsman_img);
                const player_name = document.createElement('span');
                player_name.className = 'player_name';
                player_name.id = `playername${team2_player_data[i].pid}`;
                const player_role = document.createElement('span');
                player_role.className = 'player_role';
                player_role.id = `playerrole${team2_player_data[i].pid}`;
                player_name.textContent=`${team2_player_data[i].player_name}`;
                player_role.textContent = `${team2_player_data[i].player_type}`;
                player_info.appendChild(player_name);
                player_info.appendChild(player_role);
                const credits = document.createElement('div');
                credits.className = 'credits';
                wkbatsman.appendChild(credits);
                const credit_span = document.createElement('span');
                credit_span.id = `batcredits${team2_player_data[i].pid}`;
                credit_span.textContent = `${team2_player_data[i].player_points}`; 
                credits.appendChild(credit_span);
                const addbtn = document.createElement('div');
                addbtn.className = 'addbtn';
                wkbatsman.appendChild(addbtn);
                const plus = document.createElement('button');
                plus.className = 'plus';
                plus.id = `batplus${team2_player_data[i].pid}`
                str_plus_id = String(plus.id)
                const minus = document.createElement('button');
                minus.className = 'minus';
                minus.id = `batminus${team2_player_data[i].pid}`
                str_minus_id = String(minus.id)
                addbtn.appendChild(plus);
                addbtn.appendChild(minus);
                const icon_plus = document.createElement('i');
                icon_plus.className = "fa fa-plus-circle";
                icon_plus.style.fontSize = "25px";
                plus.appendChild(icon_plus)
                const icon_minus = document.createElement('i');
                icon_minus.className = "fa fa-minus-circle";
                icon_minus.style.fontSize = "25px";
                minus.appendChild(icon_minus);
                plus.setAttribute('onclick', "add_bat('"+str_plus_id+"')");
                minus.setAttribute('onclick', "rem_bat('"+str_minus_id+"')");
                const msg_div = document.createElement('div');
                msg_div.className = 'overmsg';
                msg_div.id = `batmsg${team2_player_data[i].pid}`;
                msg_div.textContent = 'You Cannot Select more than Six Batsmans';
                main_div.appendChild(msg_div)
            }
            else if(team2_player_data[i].player_type=="ALL ROUNDER"){
                const player_img_url = team2_player_data[i].player_pic.slice(7)
                const exact_img_url = player_img_url.replace("%3A",":/")
                const main_div = document.getElementById("all_rounding")
                const wkbatsman = document.createElement('div');
                wkbatsman.className = 'allround';
                wkbatsman.id = `all_round${team2_player_data[i].pid}`;
                main_div.appendChild(wkbatsman);
                const player_info = document.createElement('div');
                player_info.className = 'player_info';
                wkbatsman.appendChild(player_info);
                const wkbatsman_img = document.createElement('img');
                wkbatsman_img.src = `${exact_img_url}`;
                wkbatsman_img.id = `playerimg${team2_player_data[i].pid}`;
                player_info.appendChild(wkbatsman_img);
                const player_name = document.createElement('span');
                player_name.className = 'player_name';
                player_name.id = `playername${team2_player_data[i].pid}`;
                const player_role = document.createElement('span');
                player_role.className = 'player_role';
                player_role.id = `playerrole${team2_player_data[i].pid}`;
                player_name.textContent=`${team2_player_data[i].player_name}`;
                player_role.textContent = `${team2_player_data[i].player_type}`;
                player_info.appendChild(player_name);
                player_info.appendChild(player_role);
                const credits = document.createElement('div');
                credits.className = 'credits';
                wkbatsman.appendChild(credits);
                const credit_span = document.createElement('span');
                credit_span.id = `allcredits${team2_player_data[i].pid}`;
                credit_span.textContent = `${team2_player_data[i].player_points}`; 
                credits.appendChild(credit_span);
                const addbtn = document.createElement('div');
                addbtn.className = 'addbtn';
                wkbatsman.appendChild(addbtn);
                const plus = document.createElement('button');
                plus.className = 'plus';
                plus.id = `allplus${team2_player_data[i].pid}`
                str_plus_id = String(plus.id)
                const minus = document.createElement('button');
                minus.className = 'minus';
                minus.id = `allminus${team2_player_data[i].pid}`
                str_minus_id = String(minus.id)
                addbtn.appendChild(plus);
                addbtn.appendChild(minus);
                const icon_plus = document.createElement('i');
                icon_plus.className = "fa fa-plus-circle";
                icon_plus.style.fontSize = "25px";
                plus.appendChild(icon_plus)
                const icon_minus = document.createElement('i');
                icon_minus.className = "fa fa-minus-circle";
                icon_minus.style.fontSize = "25px";
                minus.appendChild(icon_minus);
                plus.setAttribute('onclick', "add_round('"+str_plus_id+"')");
                minus.setAttribute('onclick', "rem_round('"+str_minus_id+"')");
                const msg_div = document.createElement('div');
                msg_div.className = 'overmsg';
                msg_div.id = `allmsg${team2_player_data[i].pid}`;
                msg_div.textContent = 'You Cannot Select more than four All Rounders';
                main_div.appendChild(msg_div)
            }

            else if(team2_player_data[i].player_type=="BOWLER"){
                const player_img_url = team2_player_data[i].player_pic.slice(7)
                const exact_img_url = player_img_url.replace("%3A",":/")
                const main_div = document.getElementById("bowling")
                const wkbatsman = document.createElement('div');
                wkbatsman.className = 'bowler';
                wkbatsman.id = `bowl${team2_player_data[i].pid}`;
                main_div.appendChild(wkbatsman);
                const player_info = document.createElement('div');
                player_info.className = 'player_info';
                wkbatsman.appendChild(player_info);
                const wkbatsman_img = document.createElement('img');
                wkbatsman_img.src = `${exact_img_url}`;
                wkbatsman_img.id = `playerimg${team2_player_data[i].pid}`;
                player_info.appendChild(wkbatsman_img);
                const player_name = document.createElement('span');
                player_name.className = 'player_name';
                player_name.id = `playername${team2_player_data[i].pid}`;
                const player_role = document.createElement('span');
                player_role.className = 'player_role';
                player_role.id = `playerrole${team2_player_data[i].pid}`;
                player_name.textContent=`${team2_player_data[i].player_name}`;
                player_role.textContent = `${team2_player_data[i].player_type}`;
                player_info.appendChild(player_name);
                player_info.appendChild(player_role);
                const credits = document.createElement('div');
                credits.className = 'credits';
                wkbatsman.appendChild(credits);
                const credit_span = document.createElement('span');
                credit_span.id = `bowlcredits${team2_player_data[i].pid}`;
                credit_span.textContent = `${team2_player_data[i].player_points}`; 
                credits.appendChild(credit_span);
                const addbtn = document.createElement('div');
                addbtn.className = 'addbtn';
                wkbatsman.appendChild(addbtn);
                const plus = document.createElement('button');
                plus.className = 'plus';
                plus.id = `bowlplus${team2_player_data[i].pid}`
                str_plus_id = String(plus.id)
                const minus = document.createElement('button');
                minus.className = 'minus';
                minus.id = `bowlminus${team2_player_data[i].pid}`
                str_minus_id = String(minus.id)
                addbtn.appendChild(plus);
                addbtn.appendChild(minus);
                const icon_plus = document.createElement('i');
                icon_plus.className = "fa fa-plus-circle";
                icon_plus.style.fontSize = "25px";
                plus.appendChild(icon_plus)
                const icon_minus = document.createElement('i');
                icon_minus.className = "fa fa-minus-circle";
                icon_minus.style.fontSize = "25px";
                minus.appendChild(icon_minus);
                plus.setAttribute('onclick', "add_bowl('"+str_plus_id+"')");
                minus.setAttribute('onclick', "rem_bowl('"+str_minus_id+"')");
                const msg_div = document.createElement('div');
                msg_div.className = 'overmsg';
                msg_div.id = `bowlmsg${team2_player_data[i].pid}`;
                msg_div.textContent = 'You Cannot Select more than Six Bowlers';
                main_div.appendChild(msg_div)
            }
        }
    }
}

player_api_data(team_players_api)

total_wicketkeeper = 0;
total_batsman = 0;
total_bowler = 0;
total_allrounder = 0;

function show_wkbat(){
    class_list = document.getElementById('Wk_Bat').classList
    class_list.add("active")
    class_list1 = document.getElementById('Bat').classList
    class_list1.remove('active')
    class_list2 = document.getElementById('All_Round').classList
    class_list2.remove('active')
    class_list3 = document.getElementById('Bowl').classList
    class_list3.remove('active')
    document.getElementById('Wk_batting').style.display='';
    document.getElementById('batting').style.display='none';
    document.getElementById('all_rounding').style.display='none';
    document.getElementById('bowling').style.display='none';
    document.getElementById('player_numbers').innerText = 'You have to select 1-4 Wk-Bastmans';
}

function show_bat(){
    class_list = document.getElementById('Bat').classList
    class_list.add("active")
    class_list1 = document.getElementById('Wk_Bat').classList
    class_list1.remove('active')
    class_list2 = document.getElementById('All_Round').classList
    class_list2.remove('active')
    class_list3 = document.getElementById('Bowl').classList
    class_list3.remove('active')
    document.getElementById('Wk_batting').style.display='none';
    document.getElementById('batting').style.display='block';
    document.getElementById('all_rounding').style.display='none';
    document.getElementById('bowling').style.display='none';
    document.getElementById('player_numbers').innerText = 'You have to select 3-6 Bastmans';

}

function show_allround(){
    class_list = document.getElementById('All_Round').classList
    class_list.add("active")
    class_list1 = document.getElementById('Bat').classList
    class_list1.remove('active')
    class_list2 = document.getElementById('Wk_Bat').classList
    class_list2.remove('active')
    class_list3 = document.getElementById('Bowl').classList
    class_list3.remove('active')
    document.getElementById('Wk_batting').style.display='none';
    document.getElementById('batting').style.display='none';
    document.getElementById('all_rounding').style.display='block';
    document.getElementById('bowling').style.display='none';
    document.getElementById('player_numbers').innerText = 'You have to select 1-4 All Rounders';

}

function show_bowl(){
    class_list = document.getElementById('Bowl').classList
    class_list.add("active")
    class_list1 = document.getElementById('Bat').classList
    class_list1.remove('active')
    class_list2 = document.getElementById('All_Round').classList
    class_list2.remove('active')
    class_list3 = document.getElementById('Wk_Bat').classList
    class_list3.remove('active')
    document.getElementById('Wk_batting').style.display='none';
    document.getElementById('batting').style.display='none';
    document.getElementById('all_rounding').style.display='none';
    document.getElementById('bowling').style.display='block';
    document.getElementById('player_numbers').innerText = 'You have to select 3-6 Wk-Bastmans';

}

function add_wk(id){
    new_id = parseInt(id.slice(10))
    get_credit = document.getElementById('wkcredits'+new_id).textContent
    total_credits = document.getElementById('total_credits').textContent
    total_players = total_wicketkeeper+total_batsman+total_allrounder+total_bowler
    if((total_wicketkeeper<=3 && (parseFloat(total_credits) - parseFloat(get_credit))>0) && (total_players<11)){
    document.getElementById(id).style.display='none';
    document.getElementById('wk_batminus'+new_id).style.display='inline';
    document.getElementById('Wk_bat'+new_id).style.background='lightgray';
    document.getElementById('total_credits').textContent = parseFloat(total_credits) - parseFloat(get_credit)
    total_wicketkeeper = total_wicketkeeper+1;
    individual_player_data[new_id] = [
    individual_player_data['player_name'] = document.getElementById('playername'+new_id).innerText,
    individual_player_data['player_pic'] = document.getElementById('playerimg'+new_id).src,
    individual_player_data['player_points'] = parseFloat(document.getElementById('wkcredits'+new_id).innerText),
    individual_player_data['player_type'] = document.getElementById('playerrole'+new_id).innerText
    ]
    if(total_players+1==11){
        document.getElementById('proc_btn').disabled = false;
        document.getElementById('proc_btn').style.cursor = 'pointer'
    }
}
    else if((parseFloat(total_credits) - parseFloat(get_credit))<0){
        document.getElementById('wkmsg'+new_id).innerText = 'Your Credit limit exceeds'
        document.getElementById('wkmsg'+new_id).style.display='block';
        timeout = setTimeout(function(){ document.getElementById('wkmsg'+new_id).style.display='none'; }, 2000);   
    }
    else if(total_players==11){
        document.getElementById('wkmsg'+new_id).innerText = 'Max numbers of players reached'
        document.getElementById('wkmsg'+new_id).style.display='block';
        timeout = setTimeout(function(){ document.getElementById('wkmsg'+new_id).style.display='none'; }, 2000);   
    }

    else{
        document.getElementById('wkmsg'+new_id).style.display='block';
        timeout = setTimeout(function(){ document.getElementById('wkmsg'+new_id).style.display='none'; }, 2000);
    }
}

function rem_wk(id){
    new_id = parseInt(id.slice(11))
    document.getElementById(id).style.display='none';
    document.getElementById('wk_batplus'+new_id).style.display='inline';
    document.getElementById('Wk_bat'+new_id).style.background='white';
    get_credit = document.getElementById('wkcredits'+new_id).textContent
    total_credits = document.getElementById('total_credits').textContent
    document.getElementById('total_credits').textContent = parseFloat(total_credits) + parseFloat(get_credit)
    total_wicketkeeper = total_wicketkeeper - 1
    total_players = total_wicketkeeper+total_batsman+total_allrounder+total_bowler
    for(key in individual_player_data){
        if(key == new_id){
        delete individual_player_data[key]
        }
    }
    if(total_players<11){
        document.getElementById('proc_btn').disabled = true;
        document.getElementById('proc_btn').style.cursor = 'not-allowed'
    } 
}

function add_bat(id){
    new_id = parseInt(id.slice(7))
    get_credit = document.getElementById('batcredits'+new_id).textContent
    total_credits = document.getElementById('total_credits').textContent
    total_players = total_wicketkeeper+total_batsman+total_allrounder+total_bowler
    if((total_batsman<=5 && (parseFloat(total_credits) - parseFloat(get_credit))>0) && (total_players<11)){
    document.getElementById(id).style.display='none';
    document.getElementById('batminus'+new_id).style.display='inline';
    document.getElementById('bat'+new_id).style.background='lightgray';
    document.getElementById('total_credits').textContent = parseFloat(total_credits) - parseFloat(get_credit)
    total_batsman = total_batsman + 1
    individual_player_data[new_id] = [
        individual_player_data['player_name'] = document.getElementById('playername'+new_id).innerText,
        individual_player_data['player_pic'] = document.getElementById('playerimg'+new_id).src,
        individual_player_data['player_points'] = parseFloat(document.getElementById('batcredits'+new_id).innerText),
        individual_player_data['player_type'] = document.getElementById('playerrole'+new_id).innerText
        ]
    if(total_players+1==11){
        document.getElementById('proc_btn').disabled = false;
        document.getElementById('proc_btn').style.cursor = 'pointer'
    }    
}
    else if((parseFloat(total_credits) - parseFloat(get_credit))<0){
        document.getElementById('batmsg'+new_id).innerText = 'Your Credit limit exceeds'
        document.getElementById('batmsg'+new_id).style.display='block';
        timeout = setTimeout(function(){ document.getElementById('batmsg'+new_id).style.display='none'; }, 2000);   
    }
    else if(total_players==11){  
        document.getElementById('batmsg'+new_id).innerText = 'Max numbers of players reached'
        document.getElementById('batmsg'+new_id).style.display='block';
        timeout = setTimeout(function(){ document.getElementById('batmsg'+new_id).style.display='none'; }, 2000);   
    }
    else{
        document.getElementById('batmsg'+new_id).style.display='block';
        timeout = setTimeout(function(){ document.getElementById('batmsg'+new_id).style.display='none'; }, 2000);
    }
}

function rem_bat(id){
    new_id = parseInt(id.slice(8))
    document.getElementById(id).style.display='none';
    document.getElementById('batplus'+new_id).style.display='inline';
    document.getElementById('bat'+new_id).style.background='white';
    get_credit = document.getElementById('batcredits'+new_id).textContent
    total_credits = document.getElementById('total_credits').textContent
    document.getElementById('total_credits').textContent = parseFloat(total_credits) + parseFloat(get_credit)
    total_batsman = total_batsman - 1
    total_players = total_wicketkeeper+total_batsman+total_allrounder+total_bowler
    for(key in individual_player_data){
        if(key == new_id){
            delete individual_player_data[key]
            }
    }
    if(total_players<11){
        document.getElementById('proc_btn').disabled = true;
        document.getElementById('proc_btn').style.cursor = 'not-allowed'
    } 
}

function add_round(id){
    new_id = parseInt(id.slice(7))
    get_credit = document.getElementById('allcredits'+new_id).textContent
    total_credits = document.getElementById('total_credits').textContent
    total_players = total_wicketkeeper+total_batsman+total_allrounder+total_bowler
    if((total_allrounder<=3 && (parseFloat(total_credits) - parseFloat(get_credit))>0) && (total_players<11)){
    document.getElementById(id).style.display='none';
    document.getElementById('allminus'+new_id).style.display='inline';
    document.getElementById('all_round'+new_id).style.background='lightgray';
    document.getElementById('total_credits').textContent = parseFloat(total_credits) - parseFloat(get_credit)
    total_allrounder = total_allrounder + 1
    individual_player_data[new_id] = [
        individual_player_data['player_name'] = document.getElementById('playername'+new_id).innerText,
        individual_player_data['player_pic'] = document.getElementById('playerimg'+new_id).src,
        individual_player_data['player_points'] = parseFloat(document.getElementById('allcredits'+new_id).innerText),
        individual_player_data['player_type'] = document.getElementById('playerrole'+new_id).innerText
        ]
    if(total_players+1==11){
        document.getElementById('proc_btn').disabled = false;
        document.getElementById('proc_btn').style.cursor = 'pointer'
    }
}
    else if((parseFloat(total_credits) - parseFloat(get_credit))<0){
        document.getElementById('allmsg'+new_id).innerText = 'Your Credit limit exceeds'
        document.getElementById('allmsg'+new_id).style.display='block';
        timeout = setTimeout(function(){ document.getElementById('allmsg'+new_id).style.display='none'; }, 2000);   
    }
    else if(total_players==11){
        document.getElementById('allmsg'+new_id).innerText = 'Max numbers of players reached'
        document.getElementById('allmsg'+new_id).style.display='block';
        timeout = setTimeout(function(){ document.getElementById('allmsg'+new_id).style.display='none'; }, 2000);
    }
    else{
        document.getElementById('allmsg'+new_id).style.display='block';
        timeout = setTimeout(function(){ document.getElementById('allmsg'+new_id).style.display='none'; }, 2000);
    }
}

function rem_round(id){
    new_id = parseInt(id.slice(8))
    document.getElementById(id).style.display='none';
    document.getElementById('allplus'+new_id).style.display='inline';
    document.getElementById('all_round'+new_id).style.background='white';
    get_credit = document.getElementById('allcredits'+new_id).textContent
    total_credits = document.getElementById('total_credits').textContent
    document.getElementById('total_credits').textContent = parseFloat(total_credits) + parseFloat(get_credit)
    total_allrounder = total_allrounder - 1
    total_players = total_wicketkeeper+total_batsman+total_allrounder+total_bowler
    for(key in individual_player_data){
        if(key == new_id){
            delete individual_player_data[key]
            }
    }
    if(total_players<11){
        document.getElementById('proc_btn').disabled = true;
        document.getElementById('proc_btn').style.cursor = 'not-allowed'
    } 
}

function add_bowl(id){
    new_id = parseInt(id.slice(8))
    get_credit = document.getElementById('bowlcredits'+new_id).textContent
    total_credits = document.getElementById('total_credits').textContent
    total_players = total_wicketkeeper+total_batsman+total_allrounder+total_bowler
    if((total_bowler<=5 && (parseFloat(total_credits) - parseFloat(get_credit))>0) && (total_players<11)){
    document.getElementById(id).style.display='none';
    document.getElementById('bowlminus'+new_id).style.display='inline';
    document.getElementById('bowl'+new_id).style.background='lightgray';
    document.getElementById('total_credits').textContent = parseFloat(total_credits) - parseFloat(get_credit)
    total_bowler = total_bowler + 1
    individual_player_data[new_id] = [
        individual_player_data['player_name'] = document.getElementById('playername'+new_id).textContent,
        individual_player_data['player_pic'] = document.getElementById('playerimg'+new_id).src,
        individual_player_data['player_points'] = parseFloat(document.getElementById('bowlcredits'+new_id).innerText),
        individual_player_data['player_type'] = document.getElementById('playerrole'+new_id).innerText
        ]
    if(total_players+1==11){
        document.getElementById('proc_btn').disabled = false;
        document.getElementById('proc_btn').style.cursor = 'pointer'
    }    
}
    else if((parseFloat(total_credits) - parseFloat(get_credit))<0){
        document.getElementById('bowlmsg'+new_id).innerText = 'Your Credit limit exceeds'
        document.getElementById('bowlmsg'+new_id).style.display='block';
        timeout = setTimeout(function(){ document.getElementById('bowlmsg'+new_id).style.display='none'; }, 2000);   
    }
    else if(total_players==11){
        document.getElementById('bowlmsg'+new_id).innerText = 'Max numbers of player reached'
        document.getElementById('bowlmsg'+new_id).style.display='block';
        timeout = setTimeout(function(){ document.getElementById('bowlmsg'+new_id).style.display='none'; }, 2000);
    }
    else{
        document.getElementById('bowlmsg'+new_id).style.display='block';
        timeout = setTimeout(function(){ document.getElementById('bowlmsg'+new_id).style.display='none'; }, 2000);
    }
}

function rem_bowl(id){
    new_id = parseInt(id.slice(9))
    document.getElementById(id).style.display='none';
    document.getElementById('bowlplus'+new_id).style.display='inline';
    document.getElementById('bowl'+new_id).style.background='white';
    get_credit = document.getElementById('bowlcredits'+new_id).textContent
    total_credits = document.getElementById('total_credits').textContent
    document.getElementById('total_credits').textContent = parseFloat(total_credits) + parseFloat(get_credit)
    total_bowler = total_bowler - 1
    for(key in individual_player_data){
        if(key == new_id){
            delete individual_player_data[key]
            }
    }
    total_players = total_wicketkeeper+total_batsman+total_allrounder+total_bowler
    if(total_players<11){
        document.getElementById('proc_btn').disabled = true;
        document.getElementById('proc_btn').style.cursor = 'not-allowed'
    } 
}

function proceed_cap(){
    console.log(individual_player_data)
    total_players = total_wicketkeeper+total_batsman+total_allrounder+total_bowler;
    if(total_players==11){
        if(total_wicketkeeper>=1){
            if(total_batsman>=3){
                if(total_allrounder>=1){
                    if(total_bowler>=3){
                        document.getElementById('box').style.display='none';
                        document.getElementById('proc_btn').style.display='none';
                        document.getElementById('team_box').style.display='block';
                        var i =0;
                        for(key in individual_player_data){
                            if(i==11){
                                break;
                            }
                            i+=1;
                            const main_div =  document.getElementById('team_box');
                            const player_section = document.createElement('div');
                            player_section.className = 'player_selection';
                            player_section.id = 'player_sec';
                            main_div.appendChild(player_section)
                            const player_in = document.createElement('div');
                            player_in.className = 'player_info';
                            player_in.id = `player${key}`;
                            player_section.appendChild(player_in);
                            const player_img = document.createElement('img');
                            player_img.id = `playerimg${key}`;
                            player_img.src = individual_player_data[key][1];
                            player_in.appendChild(player_img);
                            const player_name = document.createElement('span');
                            player_name.className = 'player_name';
                            player_name.id = `playername${key}`;
                            player_name.textContent = individual_player_data[key][0];
                            const player_role = document.createElement('span');
                            player_role.className = 'player_role';
                            player_role.id = `playerrole${key}`;
                            player_role.textContent = individual_player_data[key][3];
                            player_in.appendChild(player_name);
                            player_in.appendChild(player_role);
                            const credits = document.createElement('div');
                            credits.className = 'credits';
                            const span_credits = document.createElement('span');
                            span_credits.id = `playercredit${key}`;
                            span_credits.textContent = individual_player_data[key][2];
                            player_section.appendChild(credits)
                            credits.appendChild(span_credits);
                            const addbtn = document.createElement('div');
                            addbtn.className = 'addbtn';
                            player_section.appendChild(addbtn);
                            const cap = document.createElement('button');
                            cap.className = 'cap';
                            cap.id = `cap${key}`
                            const vicecap = document.createElement('button');
                            vicecap.className = 'vicecap';
                            vicecap.id = `vicecap${key}`;
                            cap.innerText = ' C ';
                            vicecap.innerText = ' VC ';
                            cap.setAttribute('onclick', "add_cap('"+`cap${key}`+"')");
                            vicecap.setAttribute('onclick', "add_vicecap('"+`vicecap${key}`+"')");
                            addbtn.appendChild(cap);
                            addbtn.appendChild(vicecap);
                            document.getElementById('btn_pf').style.display='block'
                        }
                    }
                    else{
                        alert("Please Select atleat 3 bowlers!!")
                    }
                }
                else{
                    alert("Please Select atleat 1 All rounder!!")
                }
            }
            else{
                alert("Please Select atleat 3 batsman!!")
            }
        }
        else{
            alert("Please Select atleat 1 Wicketkeeper!!")
        }
    }
}

var captain_choosen = 0;
var vice_captain_choosen = 0;
cap_data = {}
vice_cap_data = {}
var cap_id = 0
var vice_cap_id =0

function add_cap(id){
    const new_i = id.slice(3);
    if((captain_choosen==1 && cap_id!=new_i) && (vice_cap_id!=new_i)){
        document.getElementById(id).style.background = 'green';
        document.getElementById(id).style.color = 'white';
        document.getElementById('cap'+cap_id).style.background = 'white';
        document.getElementById('cap'+cap_id).style.color = 'black';
        for(key in cap_data){
            if(key == cap_id){
                delete cap_data[key]
            }
        }
        cap_data[new_i]=[
            cap_data['player_name'] = document.getElementById('playername'+new_i).textContent,
            cap_data['player_pic'] = document.getElementById('playerimg'+new_i).src,
            cap_data['player_points'] = parseFloat(document.getElementById('playercredit'+new_i).innerText),
            cap_data['player_type'] = document.getElementById('playerrole'+new_i).innerText
        ]
        cap_id = new_i;
        if(captain_choosen+vice_captain_choosen==2){
            document.getElementById('procf_btn').style.cursor='pointer';
            document.getElementById('procf_btn').disabled=false;
        }
    }
    else if(cap_id == new_i){
        document.getElementById(id).style.background = 'gray';
        document.getElementById(id).style.color = 'black';
        captain_choosen-=1;
        cap_id=0;
        for(key in cap_data){
            if(key == new_i){
                delete cap_data[key]
            }
        }
        if(captain_choosen+vice_captain_choosen==2){
            document.getElementById('procf_btn').style.cursor='pointer';
            document.getElementById('procf_btn').disabled=false;
    
        }
    }
    else if(vice_cap_id!=new_i){
        document.getElementById(id).style.background = 'green';
        document.getElementById(id).style.color = 'white';
        captain_choosen+=1;
        for(key in individual_player_data){
            if(key == new_i){
                delete individual_player_data[key]
            }
        }
        cap_data[new_i]=[
            cap_data['player_name'] = document.getElementById('playername'+new_i).textContent,
            cap_data['player_pic'] = document.getElementById('playerimg'+new_i).src,
            cap_data['player_points'] = parseFloat(document.getElementById('playercredit'+new_i).innerText),
            cap_data['player_type'] = document.getElementById('playerrole'+new_i).innerText
        ]
        cap_id = new_i;
    }
    if(captain_choosen+vice_captain_choosen==2){
        document.getElementById('procf_btn').style.cursor='pointer';
        document.getElementById('procf_btn').disabled=false;

    }
}

function add_vicecap(id){
    const new_i = id.slice(7);
    if((vice_captain_choosen==1 && vice_cap_id!=new_i) && (cap_id!=new_i)){
        document.getElementById(id).style.background = 'yellow';
        document.getElementById(id).style.color = 'black';
        document.getElementById('vicecap'+vice_cap_id).style.background = 'white';
        document.getElementById('vicecap'+vice_cap_id).style.color = 'black';
        for(key in vice_cap_id){
            if(key == vice_cap_id){
                delete vice_cap_data[key]
            }
        }
        vice_cap_data[new_i]=[
            vice_cap_data['player_name'] = document.getElementById('playername'+new_i).textContent,
            vice_cap_data['player_pic'] = document.getElementById('playerimg'+new_i).src,
            vice_cap_data['player_points'] = parseFloat(document.getElementById('playercredit'+new_i).innerText),
            vice_cap_data['player_type'] = document.getElementById('playerrole'+new_i).innerText
        ]
        vice_cap_id = new_i;
        if(captain_choosen+vice_captain_choosen==2){
            document.getElementById('procf_btn').style.cursor='pointer';
            document.getElementById('procf_btn').disabled=false;
    
        }

    }
    else if(vice_cap_id == new_i){
        document.getElementById(id).style.background = 'gray';
        document.getElementById(id).style.color = 'black';
        vice_captain_choosen-=1;
        vice_cap_id = 0;
        for(key in vice_cap_data){
            if(key == new_i){
                delete vice_cap_data[key]
            }
        }
        if(captain_choosen+vice_captain_choosen==2){
            document.getElementById('procf_btn').style.cursor='pointer';
            document.getElementById('procf_btn').disabled=false;
    
        }
        else{
            document.getElementById('procf_btn').style.cursor='not-allowed';
            document.getElementById('procf_btn').disabled=true;
        }
    }
    else if(cap_id!=new_i){
        document.getElementById(id).style.background = 'yellow';
        document.getElementById(id).style.color = 'white';
        vice_captain_choosen+=1;
        for(key in individual_player_data){
            if(key == new_i){
                delete individual_player_data[key]
            }
        }
        vice_cap_data[new_i]=[
            vice_cap_id['player_name'] = document.getElementById('playername'+new_i).textContent,
            vice_cap_id['player_pic'] = document.getElementById('playerimg'+new_i).src,
            vice_cap_id['player_points'] = parseFloat(document.getElementById('playercredit'+new_i).innerText),
            vice_cap_id['player_type'] = document.getElementById('playerrole'+new_i).innerText
        ]
        vice_cap_id = new_i;
        if((captain_choosen+vice_captain_choosen)==2){
            document.getElementById('procf_btn').style.cursor='pointer';
            document.getElementById('procf_btn').disabled=false;
    
        }
    }
}

async function post_data(url){
    let response = await fetch(url, {
        credentials: 'include',
        method: 'POST',
        mode: 'same-origin',
        headers: {
            'X-CSRFToken': getCookie('X-CSRFToken'),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'players': individual_player_data,
            'cap_data': cap_data,
            'vice_cap_data': vice_cap_data,
            'match_id': document.URL.split('=')[1]
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
}

function proceed_final(){
    post_data('/finalizeteam')
}