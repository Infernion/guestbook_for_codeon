from django.db import models

class GuestBookModel(models.Model):
    user_name = models.CharField(max_length=250)
    content = models.TextField(max_length=600)
    created = models.DateTimeField(auto_now=True)