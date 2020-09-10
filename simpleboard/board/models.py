from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    b_title = models.CharField(max_length=200)
    b_note = models.TextField()
    date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.date=timzone.now()
        self.save()
    def __str__(self):
        return self.title