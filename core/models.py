from django.db import models # type: ignore

class Car(models.Model):

    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    plate = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    like = models.IntegerField(default=0)
    photo = models.FileField(upload_to='img')

    def __str__(self):
        return self.name



# Create your models here.
