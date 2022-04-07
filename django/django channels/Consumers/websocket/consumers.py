#This file like views.py. allows to write async and sync funtions
import asyncio
import json
from tokenize import group
from channels.consumer import SyncConsumer,AsyncConsumer#for Asynchrounous functons
# from channels.consumer import SyncConsumer#for sync hrounous functons
from time import sleep
from .models import Chat,Group
from channels.db import database_sync_to_async

#AsyncConsumer
class MyAsync(AsyncConsumer):
    async def websocket_connect(self,event):
        print('connected...')
        print('channel layer...',self.channel_layer)
        print('channel Name...',self.channel_name)
        groupname = self.scope['url_route']['kwargs']['groupname']
        print('group name .....',groupname)

        await self.channel_layer.group_add(groupname,self.channel_name)
        await self.send({
            'type' : 'websocket.accept'
        })
        

    @database_sync_to_asyn
    def get_name(self):
        groupname = self.scope['url_route']['kwargs']['groupname']
        return Group.objects.get(name=groupname)


    async def websocket_receive(self,event):
        print('recived...',event)
        print('recived...',event['text'])
        msg = json.loads(event['text'])
        print('message.....',msg['msg'])
        groupname = self.scope['url_route']['kwargs']['groupname']
        print(groupname)

        


        await self.channel_layer.group_send(groupname,{
            'type' : 'chat.message',
            'message' : event['text']
        })

#sending method
        # await self.send({
        #     'type' : 'websocket.send',
        #     'text' : json.dumps({'data' : event['text']})

        # })

        # for i in range(20):
        #     await self.send({
        #         'type' : 'websocket.send',
        #         'text' : json.dumps({'data' : i})
        #     })
        #     await asyncio.sleep(1)
        
    async def chat_message(self,event):
        print(event['message'])
        await self.send({
            'type' : 'websocket.send',
            'text' : event['message']
        })

    async def websocket_disconnect(self,event):
        print('channel layer...',self.channel_layer)
        print('channel Name...',self.channel_name)
        groupname = self.scope['url_route']['kwargs']['groupname']
        self.channel_layer.group_discard(groupname,self.channel_layer)
        print('disconnected...')







#AsyncConsumer
class MySync(SyncConsumer):
    def websocket_connect(self,event):
        print('connected...')
        self.send({
            'type' : 'websocket.accept'
        })
        
    def websocket_receive(self,event):
        print('recived...')
        for i in range(20):
            self.send({
                'type' : 'websocket.send',
                'text' : str(i)
            })
            sleep(1)

    def websocket_disconnect(self,event):
        print('disconnected...')
