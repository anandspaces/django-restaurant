from django.db import models
from datetime import datetime
# Create your models here.
class Customer(models.Model):
    datetime = models.DateTimeField(default=datetime.now)
    no_of_diners = models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    phone_no = models.PositiveIntegerField(null=True)
    reference_no = models.CharField(max_length=20,unique=True,null=True)

    def __str__(self):
        return f"{self.datetime}  {self.no_of_diners}  {self.name}  {self.email}  {self.phone_no}"