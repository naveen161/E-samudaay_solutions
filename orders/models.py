# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Orders(models.Model):
    name = models.CharField(max_length=20)
    quanitiy = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
    


# Create your models here.
