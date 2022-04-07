from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import os
import datetime
from datetime import timezone
import json
from usermanagerAPP.models import User1
from .models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def remove_queue(user_obj):
    queue_obj = Queue.objects.get(user=user_obj)
    queue_obj.delete()

def create_queue(user_obj):
    new_queue = Queue(
        user = user_obj,
        joined_at = datetime.datetime.now(timezone.utc)
    )
    new_queue.save()
    queue_length = new_queue.id-Queue.objects.first().id
    return queue_length
        

