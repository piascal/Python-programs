# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:36:03 2019

@author: pfenger
"""

import random

outcomes = { 'heads':0, 'tails':0, }
sides = ["heads", "tails"]

print("heads: ", outcomes["heads"])
print("tails: ", outcomes["tails"])
z = int(input("How many times to flip the coin? Enter an integer: "))
print("random choice: ", z ,  " tries")

for i in range(z):
  outcomes[random.choice(sides)] += 1
  
print("heads: ", outcomes["heads"])
print("tails: ", outcomes["tails"])

#stworzyc wykres z dystrybucja rzutow moneta
