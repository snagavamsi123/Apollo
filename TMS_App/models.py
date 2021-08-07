from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils import timezone

class signup(models.Model):
    Name = models.CharField(max_length=15,null=False,blank=False)
    Mobile = PhoneNumberField(null=False,blank=False,unique=True)
    Email = models.EmailField(null=False,blank=False,unique=True)
    EmployeeId = models.CharField(max_length=10,null=False,blank=False)
    Password = models.CharField(max_length=15,null=False,blank=False)

    def __str__(self):
        return str(self.Email)


Complaint_Type = (('electrical','ELECTRICAL'),
                  ('hvac','HVAC'),
                  ('Cleaning related','CLEANING RELATED'),
                  ('others','OTHERS'))

status_choices=(('open','OPEN'),
                ('pending','PENDING'),
                ('closed','CLOSED'))

class tickets(models.Model):

    Type = models.CharField(max_length=50,choices=Complaint_Type,null=False,blank=False)
    Floor = models.IntegerField(default=1,validators=[MaxValueValidator(10)],null=False,blank=False)
    Desk_No = models.CharField(max_length=10,null=False,blank=False)
    Description = models.TextField(null=False,blank=False)
    Status = models.CharField(max_length=50,choices=status_choices,default='OPEN')
    Admin_comments = models.TextField(null=False,blank=False)
    User= models.EmailField(null=True,blank=True,unique=False)
    connection = models.ForeignKey(signup,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.Type
