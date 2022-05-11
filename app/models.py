from xmlrpc.client import boolean
from django.contrib.auth.models import User
from django.db import models


class designation(models.Model):
    designation = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.designation


class batch(models.Model): 
    batch = models.CharField(max_length=100)
    fromtime = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    totime = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
            return self.batch


class user_registration(models.Model):
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING,
                                    related_name='userregistrationdesignation', null=True, blank=True)
    fullname = models.CharField(max_length=240, null=True)
    fathername = models.CharField(max_length=240, null=True)
    mothername = models.CharField(max_length=240, null=True)
    dateofbirth = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    gender = models.CharField(max_length=240, null=True)
    pincode = models.CharField(max_length=240, null=True)
    district = models.CharField(max_length=240, null=True)
    state = models.CharField(max_length=240, null=True)
    country = models.CharField(max_length=240, null=True)
    permanentaddress1 = models.CharField(max_length=240, null=True)
    permanentaddress2 = models.CharField(max_length=240, null=True)
    permanentaddress3 = models.CharField(max_length=240, null=True)
    mobile = models.CharField(max_length=240, null=True)
    alternativeno = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    height = models.CharField(max_length=240, null=True)
    weight = models.CharField(max_length=240, null=True)
    idproof = models.FileField(upload_to='images/', null=True, blank=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    joiningdate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    startdate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    enddate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    status = models.CharField(max_length=240, null=True, default='')
    rate = models.CharField(max_length=200, null=True, default='')
    Trainer_id = models.IntegerField(default='0', null=True, blank=True)

    def __str__(self):
        return self.fullname


class workout(models.Model):
    workout_name = models.CharField(max_length=100)
    description = models.CharField(max_length=225)
    image = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return self.workout_name


class tutorial(models.Model):
    Workout = models.ForeignKey(workout, on_delete=models.CASCADE, related_name='subjects')
    video = models.FileField(upload_to="images/", blank=True, null=True)


class Machine(models.Model):
    machine_name=models.CharField(max_length=50)
    machine_details=models.CharField(max_length=200)
    machine_image=models.ImageField(upload_to="images/", null=True)
    machine_description=models.TextField(max_length=200)

    def _str_(self):
       return self.machine_name
       

class Category(models.Model):
    cate_type=models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='machinenames')
    cate_name=models.CharField(max_length=200)
    cate_details=models.CharField(max_length=200)
    cate_image=models.ImageField(upload_to="images/", null=True)
    cate_description=models.TextField(max_length=200)

    def _str_(self):
       return self.Name        


class expense(models.Model):
    payee= models.CharField(max_length=100)
    payacnt=models.CharField(max_length=100)
    paymethod= models.CharField(max_length=100)
    paydate=models.CharField(max_length=100)
    refno=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    tax=models.CharField(max_length=100)
    total=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    description=models.CharField(max_length=100)      


class payment(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,null=True, blank=True)                        
    date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    payment = models.CharField(max_length=240, null=True)
    bank = models.CharField(max_length=240, null=True)
    accountnumber = models.CharField(max_length=240, null=True)
    ifse = models.CharField(max_length=240, null=True)     


class Achievement(models.Model):
    Achievement_title= models.CharField(max_length=100,blank=True,null=True)
    Achievement_description= models.TextField(null=True,blank=True)
    Achievement_image= models.ImageField(upload_to='images/', blank=True, null=True)
    def __str__(self):
        return self.name