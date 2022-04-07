from channels.generic.websocket import AsyncWebsocketConsumer,AsyncJsonWebsocketConsumer
import asyncio
from time import sleep

"""
Generic Consumers : 1 websocketConsumer
                    2 AsyncWebsocketConsumer

                    --> No need to use json dumps or loads it autometically work <--
                    3 JsonWebsocketConsumer
                    4 AsyncJsonWebsocketConsumer
"""
class MyAsync(AsyncWebsocketConsumer):
    async def connect(self):                #call while connection requeset
        print("connected...")
        await self.accept()                 #fro accepting the connection
    
    async def receive(self,text_data):      #call when the data is received from the client
        print("receive...",text_data)       #the data sent by the client receives in the text_data attribute there is also byte_data for send bytes
        
        for i in range(11):
            await self.send(text_data=str(i))     #for send the data to the client
            await asyncio.sleep(1)
            
        # await self.close()                #for close the connection forcfully

    async def disconnect(self, code):       #call when the connection is disconnected 
        print("disconnected...")


#AsyncJsonWebsocketConsumer
class MyJsonAsync(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive_json(self, content):
        print("message....",content)
        self.send_json({'msg' : 'hellow world'})
