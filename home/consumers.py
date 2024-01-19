from channels.generic.websocket import WebsocketConsumer,AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
import json

class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "test_room"
        self.room_group_name = "test_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data="Hello World!")

    def receive(self, text_data):
        print(text_data)
        self.send(text_data="WE GOT YOUR MESSAGE!")



    def disconnect(self, *args, **kwargs):
        print("DISCONNECTED")
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        self.send(text_data="Goodbye World!")
        self.close()

    def send_notification(self,event):
        data = json.loads(event.get('value'))
        da = json.dumps({'payload':data})
        self.send(text_data=da)


class NewConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = "new_consumer"
        self.group_name = "test_group_2"
        

        await (self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        await self.accept()

        await self.send(text_data=json.dumps({"Status":"Connected"}))

    async def receive(self,text_data):
        print(text_data)
        await self.send("WE GOT YOUR MESSAGE")

    async def disconnect(self,*args, **kwargs):
        await self.close()

    async def send_notification(self,event):
        data = json.loads(event.get('value'))
        da = json.dumps({'payload':data})
        self.send(text_data=da)





