from django.db import models

# Create your models here.

class Persone(models.Model):
    #pk/id
    name = models.CharField("Contact name", max_length=50)

    def __str__(self):
        return self.name

class Phone(models.Model):
    phone = models.CharField("Phone", max_length=50)
    contact = models.ForeignKey(
        Persone,
        on_delete=models.CASCADE,
        related_name="phones"
    )

    def __str__(self):
        return self.phone