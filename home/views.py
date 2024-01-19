from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
import time

# Create your views here.
async def home(request):
    for i in range(1,10):
        data = {"count":i}
        channel_layer = get_channel_layer()
        await (channel_layer.group_send)(
            'test_group_2',{
            'type': "send_notification",
            'value': json.dumps(data)
            }
        )
        print(i)
        time.sleep(1)
        if i==3:
            time.sleep(5)
    return render(request,'home.html')