from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os
import random
# Create your models here.


class Menu(models.Model):
    kate_Cho = [("Makanan","Makanan"),
                ("Minuman","Minuman"),
                ("Side Dish","Side Dish"),]
    nama_menu = models.CharField(max_length=100)
    gambar = models.ImageField(upload_to="image/")
    stok = models.IntegerField(default=0)
    deskripsi = models.TextField()
    kategori = models.CharField(null=False, blank=True, choices=kate_Cho, max_length=30)

    def __str__(self):
        return self.nama_menu


# Hapus gambar dari penyimpanan media saat model dihapus
@receiver(pre_delete, sender=Menu)
def hapus_gambar(sender, instance, **kwargs):

    if instance.gambar:
        if os.path.isfile(instance.gambar.path):
            os.remove(instance.gambar.path)

