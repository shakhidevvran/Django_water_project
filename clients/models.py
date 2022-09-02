from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    active = models.BooleanField(default=True, verbose_name='является активным покупателем')
    bottle_ordered = models.IntegerField(default=1)
    photo = models.ImageField(verbose_name='Фото',
                              upload_to='photos',
                              null=True,
                              blank=True
                              )
