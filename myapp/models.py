from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserRegisterModel(models.Model):
    username = models.CharField(max_length = 56)
    first_name = models.CharField(max_length = 56)
    last_name = models.CharField(max_length = 56)
    email = models.EmailField()

class AbstractBaseModel(models.Model):
    gear_choice= [
        ('Manual', 'M'),
        ('Auto', 'A')
    ]
    name = models.CharField(max_length = 56)
    year = models.IntegerField()
    color = models.CharField(max_length = 18)
    gear = models.CharField(max_length= 9, choices= gear_choice)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    class Meta:
        abstract = True

    # def __str__(self) -> str:
    #     return self.name


class MalibuModel(AbstractBaseModel):
    pass

class GentraModel(AbstractBaseModel):
    pass

class CobaltModel(AbstractBaseModel):
    pass

class NexiaModel(AbstractBaseModel):
    pass


