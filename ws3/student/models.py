from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from multiselectfield import MultiSelectField

class Scholarship(models.Model):
    PROGRAM=(('Btech','Btech'),('Mtech','Mtech'),('PHD','PHD'))
    CASTE=(('Oc','Oc'),('Obc','Obc'),('Sc','Sc'),('St','St'))
    BRANCH=(('Cse','Cse'),('Ece','Ece'),('Eee','Eee'),('Mech','Mech'),('Chem','Chem'),('Civil','Civil'),('Bio','Bio'),('Mme','Mme'))
    GENDER=(('Male','Male'),('Female','Female'),('Other','Other'))


    name = models.CharField(max_length=200)
    scholarship_profile = models.ImageField(upload_to="images")
    instructions = models.TextField(max_length=500, default=""),
    openingtime=models.DateField(blank=True, null=True)
    closingtime=models.DateField(blank=True, null=True)
    program= MultiSelectField(choices=PROGRAM,blank=True, null=True)
    caste= MultiSelectField(choices=CASTE,blank=True, null=True)
    branch= MultiSelectField(choices=BRANCH,blank=True, null=True)
    gender= models.CharField(max_length=10, choices= GENDER,blank=True, null=True)

class Student(models.Model):
    PROGRAM=(('Btech','Btech'),('Mtech','Mtech'),('PHD','PHD'),)
    CASTE=(('Oc','Oc'),('Obc','Obc'),('Sc','Sc'),('St','St'),)
    BRANCH=(('Cse','Cse'),('Ece','Ece'),('Eee','Eee'),('Mech','Mech'),('Chem','Chem'),('Civil','Civil'),('Bio','Bio'),('Mme','Mme'),)
    GENDER=(('Male','Male'),('Female','Female'),('Other','Other'))
    
    
    name = models.CharField(max_length=200) 
    email = models.CharField(max_length=200) 
    phone_no = models.CharField(max_length=200) 
    address = models.TextField(max_length=200) 
    student_profile = models.ImageField(upload_to="images") 
    course = models.CharField(max_length=100, choices= BRANCH)
    name = models.CharField(max_length=200) 
    email = models.CharField(max_length=200) 
    phone_no = models.CharField(max_length=200) 
    address = models.TextField(max_length=200) 
    student_profile = models.ImageField(upload_to="images") 
    branch = models.CharField(max_length=100, choices= BRANCH,blank=True, null=True)
    caste=models.CharField(max_length=100, choices= CASTE,blank=True, null=True)
    gender=models.CharField(max_length=100, choices=GENDER,blank=True, null=True)


class Application(models.Model):
    
 
    STATUS = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    )
    elgible=True
    user = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    scholarship=models.ForeignKey(Scholarship, on_delete=models.CASCADE, blank=True, null=True)
    Application_Status = models.TextField(max_length=100, choices=STATUS, default="Pending")
    message = models.TextField(max_length=100, default="")
 
    def __str__(self):
        return self.scholarship.name
 
    def get_absolute_url(self):
        return reverse('users')

# Create your models here.
