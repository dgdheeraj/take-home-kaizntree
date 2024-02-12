from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    sku = models.CharField(name="SKU",max_length=255, unique=True)
    name = models.CharField(max_length=255)
    tags = models.ManyToManyField(to=Tag, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    in_stock = models.FloatField()
    available_stock = models.FloatField()
    date = models.DateField(auto_now=True)