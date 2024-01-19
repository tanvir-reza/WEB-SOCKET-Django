from django.db import models
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

# Create your models here.
class Notification(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):
        channel_layer = get_channel_layer()
        noti = Notification.objects.filter(is_read=False).count()
        data = {"count":noti,'current_notification':self.title}
        async_to_sync(channel_layer.group_send)(
            'test_group_2',{
            'type': "send_notification",
            'value': json.dumps(data)
            }
            
        )


        super(Notification,self).save(*args,**kwargs)