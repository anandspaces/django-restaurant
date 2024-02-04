from django.db import models

# Create your models here.
class Customer(models.Model):
    booking = models.TextField()

    def __str__(self):
        return self.text[:50]