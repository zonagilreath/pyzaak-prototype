from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_by = models.ForeignKey(User, on_delete="PROTECT")
    date_added = models.DateTimeField(auto_now_add=True)
