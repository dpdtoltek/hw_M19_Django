from django.db import models


# Create your models here.
class Buyer(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    balance = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    age = models.IntegerField()

    def __str__(self):
        return self.username


class Game(models.Model):
    title = models.CharField(max_length=256, unique=True)
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    size = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField(blank=True)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(to=Buyer, related_name='games')

    def __str__(self):
        return self.title
