from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

   

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)

    





class category(models.Model):
    product_type=models.CharField(max_length=100)
    def __str__(self):
        return self.product_type    



class AddProducts(models.Model):
    owner = models.ForeignKey(Employee,on_delete=models.CASCADE)
    product_varity=models.ForeignKey(category,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_image=models.ImageField(null=True,blank=True,upload_to="images/")
    product_quantity = models.CharField(max_length=50)
    price = models.IntegerField()

    @property
    def imageURL(self):
        try:
            url=self.product_image.url
        except:
            url=''
        return url

    def get_absolute_url(self):
        return reverse("accounts:addProducts", args=(str(self.id)))

    def __str__(self):
        return self.product_name


