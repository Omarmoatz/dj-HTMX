from django.db import models
from django.db.models.functions import Now

class Todo(models.Model):
    task = models.CharField( max_length=50,db_defaulf='default_task')
    created_at = models.DateTimeField( db_defaulf=Now(utc=True))
    completed_at = models.DateTimeField(null=True)
    completed = models.BooleanField( db_defaulf=False)
    
    def complete(self):
        self.completed_at = Now()
        self.save()
        
    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.task
