from django.db import models

# Create your models here.


class jrny(models.Model):
    start = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    time = models.CharField(max_length=12)
    number = models.IntegerField()
    date = models.CharField(max_length=12)

    def __str__(self):
        return self.start
