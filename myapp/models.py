from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField(unique=True)
    phoneNo = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20, default='user')

    def __str__(self):
        return f"{self.fname} {self.lname}"
