from django.db import models
from django.db.models.functions import Now

class Todo(models.Model):
    task = models.CharField( max_length=50,db_default='default_task')
    created_at = models.DateTimeField( db_default=Now(utc=True))
    completed = models.BooleanField( db_default=False)
        
    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.task
