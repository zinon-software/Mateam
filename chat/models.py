from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    user = models.OneToOneField(User, related_name='friends', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Chat(models.Model):
    created_by = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True)
    super_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    messages = models.TextField(max_length=4000, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    customer = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return str(self.id)