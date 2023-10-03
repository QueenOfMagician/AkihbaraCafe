from django.db import models
import random
# Create your models here.
def randomin():
    random.randint(12345,98765)

class Masuk(models.Model):
    id = models.IntegerField(default=randomin, unique=True, primary_key=True, null=False, blank=False)
    jam_masuk = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.id}"