from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    owner = models.ForeignKey('auth.user', related_name='tasks', on_delete=models.CASCADE,null=True,blank=True )
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']