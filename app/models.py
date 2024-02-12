from django.db import models

# Create your models here.

class Profile(models.Model):
    first_name=models.CharField(max_length=100)
    sur_name=models.CharField(max_length=100)
    age=models.IntegerField()
    mobile=models.CharField(max_length=100)
    date_birth=models.DateField()
    email=models.EmailField()

    def __str__(self):
        return str(self.first_name +' '+ self.sur_name)
