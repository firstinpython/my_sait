import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import MessageDB

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.GroupName = self.scope['url_route']['kwargs']['room_name']
        print(self.GroupName)
        self.roomGroupName = f"chat_{self.GroupName}"
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel.name.group_discard(
            self.roomGroupName,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        sync_to_async(MessageDB.objects.create(
            name_room = self.GroupName,
            message = message,
            user=username
        ))
        await self.channel_layer.group_send(
            self.roomGroupName, {
                "type": "sendMessage",
                "message": message,
                "username": username,
            })

    async def sendMessage(self, event):
        message = event["message"]
        username = event["username"]
        await self.send(text_data=json.dumps({"message": message, "username": username}))
