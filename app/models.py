from django.db import models

class Flower(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='flowers/', null=True, blank=True)

    def __str__(self):
        return self.name
