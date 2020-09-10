from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    id= models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    note = models.TextField()
    date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.date=timzone.now()
        self.save()
    def __str__(self):
        return self.title