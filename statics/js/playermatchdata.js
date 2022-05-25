

function show_first_player_data(){
    const first_id = JSON.parse(document.getElementById('first_id').textContent);
    document.getElementById('player'+parseInt(first_id)).style.display='block';
    current_visible = first_id
}

show_first_player_data()


function show_player_data(){
    value = document.getElementById('players').value;
    console.log(value)
    document.getElementById('player'+parseInt(value)).style.display='block';
    document.getElementById('player'+current_visible).style.display='none';
    current_visible = value;
}