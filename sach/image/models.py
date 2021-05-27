from django.db import models

# Create your models here.

class Hinh(models.Model):

    hinh = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.hinh