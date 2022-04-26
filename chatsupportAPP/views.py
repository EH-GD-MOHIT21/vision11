from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.conf import settings
import os
import datetime
from datetime import timezone
import json
from usermanagerAPP.models import User1
from .models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def remove_queue(queue_obj1):
    queue_obj = Queue.objects.get(id = queue_obj1.id)
    queue_obj.delete()

def remove_queue1(user_obj):
    try:
        queue_obj = Queue.objects.get(user = user_obj)
        queue_obj.delete()
    except:
        pass

def create_queue(user_obj,grp_name):
    new_queue = Queue(
        user = user_obj,
        group_name = grp_name,
        joined_at = datetime.datetime.now(timezone.utc)
    )
    new_queue.save()
    queue_length = new_queue.id-Queue.objects.first().id
    return queue_length

def get_queue(queue_obj):
    user_obj = queue_obj.user
    user_o = Queue.objects.get(user= user_obj)
    queue_length = user_o.id-Queue.objects.first().id
    grp_name = user_o.group_name
    dict_info ={
        'queue_length':queue_length,
        'grp_name':grp_name,
    }
    return dict_info

def RenderAdminChat(request):
    if request.user.is_authenticated:
        if(request.user.staff):
            try:
                all_queues = Queue.objects.first()
                id_queue = all_queues.group_name
                return render(request, 'admin_chatbox.html',{'queues':all_queues,'queue_id':id_queue}) 
            except:
                return redirect('/')
    return redirect('/') 

