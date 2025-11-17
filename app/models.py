from django.db import models


class FlowerCategory(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='flowers')

    def __str__(self):
        return self.name
    
class Flower(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(FlowerCategory, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='flowers/', null=True, blank=True)

    def __str__(self):
        return self.name
