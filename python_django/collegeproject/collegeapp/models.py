from django.db import models


class teacher(models.Model):
    firstname=models.CharField(max_length=255,blank=False,null=False)
    lastname=models.CharField(max_length=255,blank=False,null=False)
    email=models.CharField(max_length=255,blank=False,null=False)
    department=models.CharField(max_length=255,blank=False,null=False)
    phoneno=models.CharField(max_length=255,blank=False,null=False)
    gender=models.CharField(max_length=255,blank=False,null=False)   
    dob=models.CharField(max_length=255,blank=False,null=False)
    qualification=models.CharField(max_length=255,blank=False,null=False)
    address=models.CharField(max_length=255,blank=False,null=False)
    pin=models.CharField(max_length=255,blank=False,null=False)
    state=models.CharField(max_length=255,blank=False,null=False)
    country=models.CharField(max_length=255,blank=False,null=False)
    status=models.CharField(max_length=255,blank=False,null=False)




    def __str__(self):
        return self.email





# Create your models here.
