from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} ({self.id})"
    

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    volume = models.CharField(max_length=10)
    description = models.CharField(max_length=30)
    images = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.id})"