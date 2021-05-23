from django.db import models

# Create your models here.

class Calculation(models.Model):
    operation = models.CharField(max_length=3)
    arg_a = models.FloatField()
    arg_b = models.FloatField()
    result = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.operation} ({self.arg_a}, {self.arg_b})"