import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync


class MyChatApp(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("Connecting...")
        await self.accept()
        
    async def receive(self, text_data):
        pass
    
    async def disconnect(self):
        pass