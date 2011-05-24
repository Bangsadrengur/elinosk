# -*- coding: utf-8 -*-
from django.shortcuts import render

def index(request):
    Befni = ("Þetta er heimasíða óperusöngkonunnar Elínar Óskar Óskarsdóttur. "
             "Hér á þessari síðu geturðu lesið um feril minn og fundið " 
             "myndir af mér hvort sem er í hlutverki á óperusviðinu og ýmsar "
             "aðrar myndir sem skýra sig sjálfar. Þú getur hlustað á "
             "tónlistina mína og horft á klippur úr nokkrum vel völdum óperum.")

    return render(request, 'base_w.html', {'Befni': Befni})
