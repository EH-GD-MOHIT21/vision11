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
}

function add_wk(id){
    new_id = parseInt(id.slice(10))
    if(total_wicketkeeper<=2){
    document.getElementById(id).style.display='none';
    document.getElementById('wk_batminus'+new_id).style.display='';
    document.getElementById('Wk_bat'+new_id).style.background='lightgray';
    get_credit = document.getElementById('wkcredits'+new_id).textContent
    total_credits = document.getElementById('total_credits').textContent
    document.getElementById('total_credits').textContent = parseFloat(total_credits) - parseFloat(get_credit)
    total_wicketkeeper = total_wicketkeeper+1
}

    else{
        document.getElementById('wkmsg'+new_id).style.display='';
    }
}

function rem_wk(id){
    new_id = parseInt(id.slice(11))
    document.getElementById(id).style.display='none';
    document.getElementById('wk_batplus'+new_id).style.display='';
    document.getElementById('Wk_bat'+new_id).style.background='white';
    get_credit = document.getElementById('wkcredits'+new_id).textContent
    total_credits = document.getElementById('total_credits').textContent
    document.getElementById('total_credits').textContent = parseFloat(total_credits) + parseFloat(get_credit)
    total_wicketkeeper = total_wicketkeeper - 1
}

function add_bat(id){
    new_id = parseInt(id.slice(7))
    if(total_batsman<=6){
    document.getElementById(id).style.display='none';
    document.getElementById('batminus'+new_id).style.display='';
    document.getElementById('bat'+new_id).style.background='lightgray';
    get_credit = document.getElementById('batcredits'+new_id).textContent
    total_credits = document.getElementById('total_credits').textContent
    document.getElementById('total_credits').textContent = parseFloat(total_credits) - parseFloat(get_credit)
    total_batsman = total_batsman + 1
}
    else{
        document.getElementById('batmsg'+new_id).style.display='';
    }
}

function rem_bat(id){
    new_id = parseInt(id.slice(8))
    document.getElementById(id).style.display='none';
    document.getElementById('batplus'+new_id).style.display='';
    document.getElementById('bat'+new_id).style.background='white';
    get_credit = document.getElementById('batcredits'+new_id).textContent
    total_credits = document.getElementById('total_credits').textContent
    document.getElementById('total_credits').textContent = parseFloat(total_credits) + parseFloat(get_credit)
    total_batsman = total_batsman - 1
}

function add_round(id){
    new_id = parseInt(id.slice(7))
    if(total_allrounder<=4){
    document.getElementById(id).style.display='none';
    document.getElementById('allminus'+new_id).style.display='';
    document.getElementById('all_round'+new_id).style.background='lightgray';
    get_credit = document.getElementById('allcredits'+new_id).textContent
    total_credits = document.getElementById('total_credits').textContent
    document.getElementById('total_credits').textContent = parseFloat(total_credits) - parseFloat(get_credit)
    total_allrounder = total_allrounder + 1
}
    else{
        document.getElementById('allmsg'+new_id).style.display='';
    }
}

function rem_round(id){
    new_id = parseInt(id.slice(8))
    document.getElementById(id).style.display='none';
    document.getElementById('allplus'+new_id).style.display='';
    document.getElementById('all_round'+new_id).style.background='white';
    get_credit = document.getElementById('allcredits'+new_id).textContent
    total_credits = document.getElementById('total_credits').textContent
    document.getElementById('total_credits').textContent = parseFloat(total_credits) + parseFloat(get_credit)
    total_allrounder = total_allrounder - 1
}

function add_bowl(id){
    new_id = parseInt(id.slice(8))
    if(total_bowler<=6){
    document.getElementById(id).style.display='none';
    document.getElementById('bowlminus'+new_id).style.display='';
    document.getElementById('bowl'+new_id).style.background='lightgray';
    get_credit = document.getElementById('bowlcredits'+new_id).textContent
    total_credits = document.getElementById('total_credits').textContent
    document.getElementById('total_credits').textContent = parseFloat(total_credits) - parseFloat(get_credit)
    total_bowler = total_bowler + 1
}
    else{
        document.getElementById('bowlmsg'+new_id).style.display='';
    }
}

function rem_bowl(id){
    new_id = parseInt(id.slice(9))
    document.getElementById(id).style.display='none';
    document.getElementById('bowlplus'+new_id).style.display='';
    document.getElementById('bowl'+new_id).style.background='white';
    get_credit = document.getElementById('bowlcredits'+new_id).textContent
    total_credits = document.getElementById('total_credits').textContent
    document.getElementById('total_credits').textContent = parseFloat(total_credits) + parseFloat(get_credit)
    total_bowler = total_bowler - 1
}
