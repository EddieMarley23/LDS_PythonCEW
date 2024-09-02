from django.db import models
from django.core.validators import FileExtensionValidator # type: ignore


class Car(models.Model):

    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    plate = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    createdby = models.IntegerField()
    like = models.IntegerField()
    photo = models.ImageField(upload_to='img',validators=[FileExtensionValidator(['.png', '.jpg', '.jpeg'])])

    def __str__(self):
        return self.name

# Create your models here.
