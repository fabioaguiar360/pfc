import sys
sys.path.append("..")
from django.db import models
from categories.models import Category

# Create your models here.
class Output(models.Model):
    name        = models.CharField(max_length=250)
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    value       = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name