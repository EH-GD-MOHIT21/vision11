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