from django.db import models

# Create your models here.
class Login(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Type = models.CharField(max_length=15)

class User(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)



class Category(models.Model):
    categoryname = models.CharField(max_length=100)



class Complaint(models.Model):
    Date = models.CharField(max_length=100)
    complaint = models.CharField(max_length=500)
    Reply = models.CharField(max_length=500)
    Status = models.CharField(max_length=100)

    USER = models.ForeignKey(User, on_delete=models.CASCADE)

class Subcategory(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    Date = models.CharField(max_length=100)
    CATEGORY = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategoryname = models.CharField(max_length=100)

class Reminder(models.Model):
    Date = models.DateField()
    Time=models.TimeField()
    SUBCATEGORY= models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    fphoto = models.CharField(max_length=100)
    bphoto = models.CharField(max_length=100)
    status = models.CharField(max_length=100,default='')
    amount = models.FloatField()


class feedback(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    Date = models.DateField(default='2023-11-11')
    feedback = models.CharField(max_length=500)
    Rating = models.FloatField()

class Notification(models.Model):
    REMINDER = models.ForeignKey(Reminder, on_delete=models.CASCADE)
    Date = models.DateField(default='2023-11-11')
    Time = models.CharField(max_length=100)


