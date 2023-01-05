from django.db import models
from django.utils import timezone

# Create your models here.
class ContactUser(models.Model):
    fullname = models.TextField(max_length=100)
    email = models.EmailField()
    subject = models.TextField(max_length=100)
    message = models.TextField(max_length=100)
    success = models.BooleanField(default=False)
    delivered= models.BooleanField(default=False)
    
    

    def __str__(self):
        return self.fullname
    
class Visitor(models.Model):
    visitor = models.IntegerField(default=0)
    time= models.DateTimeField(default=timezone.now)

    os = models.TextField(default="No")
    browser = models.TextField(default="No")
    device= models.TextField(default="No")

    mobile= models.BooleanField(default=False)
    tablet= models.BooleanField(default=False)
    touch_capable= models.BooleanField(default=False)
    pc= models.BooleanField(default=False)
    bot= models.BooleanField(default=False)



    #def __str__(self):
        #return self.visitor
    