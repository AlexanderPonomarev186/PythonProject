from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField(default=0.0)
    cost = models.FloatField(default=0.0)

    def str(self):
        return '{} - {}'.format(self.pk, self.name)


class Profession(models.Model):
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='img')

    def __str__(self):
        return '{} - {}'.format(self.pk, self.description)


class Image(models.Model):
    image = models.ImageField(upload_to='img')
    name = models.CharField(max_length=200)
    def __str__(self):
        return f'ProfessionImage-{self.pk}'