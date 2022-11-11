from django.db import models

class TodoTask(models.Model):
    taskname = models.CharField(max_length=255,blank=False,null=False)
    category = models.CharField(max_length=255,blank=False,null=False)
    priority = models.CharField(max_length=255,blank=False,null=False)
    date = models.DateField()



    def __str__(self):
        return self.taskname

# Create your models here.
