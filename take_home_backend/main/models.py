from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Inventory(models.Model):
    sku = models.CharField(name="SKU",max_length=255, unique=True)
    name = models.CharField(max_length=255)
    tags = models.ManyToManyField(to=Tag, related_name="posts", blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    in_stock = models.FloatField()
    available_stock = models.FloatField()
