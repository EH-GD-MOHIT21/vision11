function show_user_info_data(data,main_div){
    if(data===undefined){
        main_div.innerHTML = '<h1 style="color:white;text-align:center;margin:10px auto;">No user found with provided username</h1>'
        return;
    }else{
        main_div.innerHTML = '';
    }
    const parent = document.createElement('div');
    parent.className = 'userinfo-box';
    main_div.appendChild(parent)
    console.log(data['orders'].length)

    for(var i=0;i<data['user'].length;i++){
        const fc = document.createElement('div');
        fc.className = 'all_details';
        parent.appendChild(fc);
        const heading = document.createElement('h3');
        heading.textContent = 'User Details';
        fc.appendChild(heading)
        const details = document.createElement('div');
        details.className = 'details';
        fc.appendChild(details);
        const user = document.createElement('div');
        user.textContent = `User: ${data['user'][i].username} (${data['user'][i].id})`
        details.appendChild(user)
        const mail = document.createElement('div');
        mail.textContent = `Email: ${data['user'][i].email}`;
        details.appendChild(mail)
        const age = document.createElement('div');
        age.textContent = `age: ${data['user'][i].age}`;
        details.appendChild(age);
        const aadhar_img = document.createElement('div');
        aadhar_img.textContent = `Aadhar image: ${data['user'][i].aadhar_image}`
        details.appendChild(aadhar_img);
        const count = document.createElement('div');
        count.textContent = `Country : ${data['user'][i].country}`
        details.appendChild(count);
    }

    for(var i=0;i<data['orders'].length;i++){
        const fc = document.createElement('div');
        fc.className = 'ordeers';
        parent.appendChild(fc);
        const heading = document.createElement('h3');
        heading.textContent = 'Orders';
        fc.appendChild(heading)
        const details = document.createElement('div');
        details.className = 'details';
        fc.appendChild(details);
        const id = document.createElement('div');
        id.textContent = `Id: (${data['orders'][i].id})`;
        details.appendChild(id)
        const amount = document.createElement('div');
        amount.textContent = `Amount: ${data['orders'][i].amount}`;
        details.appendChild(amount)
        const order_id = document.createElement('div');
        order_id.textContent = `order_id: ${data['orders'][i].order_id}`;
        details.appendChild(order_id);
        const currency = document.createElement('div');
        currency.textContent = `currency: ${data['orders'][i].currency}`
        details.appendChild(currency);
        const payment_capture = document.createElement('div');
        payment_capture.textContent = `payment_capture : ${data['orders'][i].payment_capture}`
        details.appendChild(payment_capture);
        const plan_benefits = document.createElement('div');
        plan_benefits.textContent = `payment_capture : ${data['orders'][i].plan_benefits}`
        details.appendChild(plan_benefits);
        const order_status = document.createElement('div');
        order_status.textContent = `order_status : ${data['orders'][i].order_status}`
        details.appendChild(order_status);
    }
    for(var i=0;i<data['contest_logs'].length;i++){
    const fc = document.createElement('div');
    fc.className = 'user_logs';
    parent.appendChild(fc);
    const heading = document.createElement('h3');
    heading.textContent = 'User Logs';
    fc.appendChild(heading)
    const details = document.createElement('div');
    details.className = 'details';
    fc.appendChild(details);
    const id = document.createElement('div');
    id.textContent = `Id: ${data['contest_logs'][i].id}`
    details.appendChild(id)
    const log = document.createElement('div');
    log.textContent = `log: ${data['contest_logs'][i].log}`;
    details.appendChild(log)
    const currency_type_user = document.createElement('div');
    currency_type_user.textContent = `currency_type_user: ${data['contest_logs'][i].currency_type_user}`;
    details.appendChild(currency_type_user);
    const currency_type_contest = document.createElement('div');
    currency_type_contest.textContent = `currency_type_contest: ${data['contest_logs'][i].currency_type_contest}`
    details.appendChild(currency_type_contest);
    const payment = document.createElement('div');
    payment.textContent = `payment : ${data['contest_logs'][i].payment}`
    details.appendChild(payment);
    const payment_add = document.createElement('div');
    payment_add.textContent = `payment_add : ${data['contest_logs'][i].payment_add}`
    details.appendChild(payment_add);
    const save_at = document.createElement('div');
    save_at.textContent = `save_at : ${data['contest_logs'][i].save_at}`
    details.appendChild(save_at);
    }
}