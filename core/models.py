from django.db import models
class Car(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField(default=0.0)
    cost = models.FloatField(default=0.0)

    def str(self):
        return '{} - {}'.format(self.pk, self.name)