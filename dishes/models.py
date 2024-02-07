from django.db import models
from datetime import datetime
# Create your models here.
class Customer(models.Model):
    datetime = models.DateTimeField(default=datetime.now)
    no_of_diners = models.PositiveIntegerField(default=1)
    first_name = models.CharField(max_length=50,default='FirstName')
    last_name = models.CharField(max_length=50,default='LastName')
    email = models.EmailField(default='example@example.com')
    phone_no = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"{self.datetime}  {self.no_of_diners}  {self.first_name}  {self.last_name}  {self.email}  {self.phone_no}"