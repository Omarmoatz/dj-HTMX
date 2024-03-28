from django.db import models
from django.db.models.functions import Now
from  django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(User, related_name='user_task', on_delete=models.CASCADE)
    task = models.CharField( max_length=50,db_default='default_task')
    created_at = models.DateTimeField( db_default=Now(utc=True))
    completed = models.BooleanField( db_default=False)
        
    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.task
