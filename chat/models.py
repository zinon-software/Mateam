from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver_messages', on_delete=models.CASCADE)
    message = models.TextField()
    seen = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username
    
    
    class Meta:
        ordering = ("date_added",)

