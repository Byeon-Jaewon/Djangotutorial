from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=200)
    note = models.TextField()
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title