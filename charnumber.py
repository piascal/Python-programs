# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:06:24 2019

@author: pfenger
"""
import pprint
message = str(input("Wpisz wiadomosc: "))
licznik = {}

for i in message:
    licznik.setdefault(i, 0)
    licznik[i] = licznik[i] + 1
    #print(i, "->", licznik[i])

pprint.pprint(licznik)