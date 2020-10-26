from django.db import models

class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    price = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.ticker
        return self.price