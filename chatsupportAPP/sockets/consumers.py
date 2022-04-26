import datetime
import json
from datetime import timezone
from unicodedata import name

from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from channels.exceptions import StopConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from chatsupportAPP.models import Chat, Queue
from usermanagerAPP.models import User1
from chatsupportAPP import views


class MyASyncConsumer(AsyncWebsocketConsumer): 
    async def connect(self):
        self.group_name=self.scope['url_route']['kwargs']['groupname']
        self.pid=self.scope['url_route']['kwargs']['pid']
        user = self.scope['user']
        if user.is_anonymous:
            await self.close()
        else:
            print('websocket connected..')
            await self.channel_layer.group_add(
                self.group_name,
                self.channel_name,
            )
            await self.accept()

            if(user.staff):
                self.group_name = self.group_name
                await self.channel_layer.group_send(
                self.group_name,
                {
                'type':'chat.message',
                'message': f"Hii agent is here how can i help you!!",
                'username':user.username,
                'updation':'no'
                }
                )
                queue_obj = await sync_to_async(Queue.objects.get)(group_name = self.group_name)
                await sync_to_async(views.remove_queue)(queue_obj)
                for i in await self.get_all_queues():
                    queue_info = await sync_to_async(views.get_queue)(i) 
                    await self.channel_layer.group_send(
                    queue_info['grp_name'],
                    {
                    'type':'chat3.message',
                    'message': f"{queue_info['queue_length']}",
                    })
            else:
                queue_len = await sync_to_async(views.create_queue)(user,self.group_name)
                await self.channel_layer.group_send(
                self.group_name,
                {
                'type':'chat2.message',
                'message': f"{queue_len}",
                'username':user.username,
                }
                )
    async def chat2_message(self,event):
        await self.send(text_data=json.dumps({
            'msg':event['message'],
            'status':'no',
            'updation':'no',
            'username':event['username'],
        }))

    async def chat_message(self,event):
        await self.send(text_data=json.dumps({
            'msg':event['message'],
            'status':'yes',
            'updation':'no',
            'username':event['username'],
        }))
    
    async def receive(self,text_data=None,bytes_data=None):
        print('message recived succesfully...',text_data)
        data=json.loads(text_data)
        message=data['msg']
        user1 = self.scope["user"]
        chat=Chat(
            user=user1,
            group=self.group_name  ,
            message=data['msg'],
            timestamp=datetime.datetime.now(timezone.utc)
        )
        await database_sync_to_async(chat.save)()
        await self.channel_layer.group_send(
            self.group_name,
            {
            'type':'chat1.message',
            'message': message,
            'username': user1.username,
            }
        )
    async def chat1_message(self,event):
        await self.send(text_data=json.dumps({
            'msg':event['message'],
            'status':'yes',
            'updation':'no',
            'username':event['username'],
        }))
    @sync_to_async
    def get_all_queues(self):
        return list(Queue.objects.all())
         
    async def disconnect(self,event):
        print('websocket disconnected...',event)
        user = self.scope['user']
        if(user.staff == False):  
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type':'chat5.message',
                    'message': "User left Please refresh Page to Chat to new user",
                    'username': user.username      
                }
            )
            await sync_to_async(views.remove_queue1)(user)
            for i in await self.get_all_queues():
                queue_info = await sync_to_async(views.get_queue)(i) 
                await self.channel_layer.group_send(
                queue_info['grp_name'],
                {
                'type':'chat3.message',
                'message': f"{queue_info['queue_length']}",
                })
    async def chat3_message(self,event):
        await self.send(text_data=json.dumps({
            'msg':event['message'],
            'status':'no',
            'updation':'yes',
        }))
    async def chat5_message(self,event):
        await self.send(text_data=json.dumps({
            'msg':event['message'],
            'username':event['username'],
        }))
        self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        raise StopConsumer
