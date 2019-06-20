from django.db import models

# Create your models here.
class Input(models.Model):
    name        = models.CharField(max_length=250)
    category    = models.CharField(max_length=250)
    value       = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name