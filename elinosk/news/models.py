# -*- coding: UTF-8 -*-
from django.db import models

class  News(models.Model):
    headline = models.CharField(u"Fyrisögn", max_length=255)
