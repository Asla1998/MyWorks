from django.db import models

class ContactsBook(models.Model):
    firstname = models.CharField(max_length=255,blank=False,null=False)
    lastname = models.CharField(max_length=255,blank=False,null=False)
    email = models.CharField(max_length=255,blank=False,null=False)
    phonenumber = models.CharField(max_length=255,blank=False,null=False)
    address = models.CharField(max_length=255,blank=False,null=False)



    def __str__(self):
        return self.email

# Create your models here.
