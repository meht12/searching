# api_integration/models.py
from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date_registered = models.DateTimeField()

    def __str__(self):
        return self.name
