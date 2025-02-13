from django.db import models

# Create your models here.
class  Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=50)

class User(models.Model):
    username=models.CharField(max_length=50)
    photo=models.CharField(max_length=100)
    place=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    pin=models.BigIntegerField()
    district=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    age=models.BigIntegerField()
    phone=models.BigIntegerField()
    gender=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)

class Contact(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE,default='')
    name=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)
    relation=models.CharField(max_length=100)
    photo=models.CharField(max_length=100)

class Complaint(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=100)
    date=models.DateField(max_length=100)
    reply=models.CharField(max_length=100)


# class Reply(models.Model):
#     COMPLAINT=models.ForeignKey(Complaint,on_delete=models.CASCADE)
#     date=models.DateField(max_length=100)
#     reply=models.CharField(max_length=100)



