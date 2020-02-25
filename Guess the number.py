# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:30:05 2019

@author: pfenger
"""

# Write a program where the computer randomly generates a number between 0 and 
# 20. The user needs to guess what the number is. If the user guesses wrong, 
# tell them their guess is either too high, or too low. 
# This will get you started with the random library if you haven't already used it.

import random

while True:

  a = random.randint(1,20)
  b = int(input('Zgadnij liczbe od 1 do 20: '))
  print("")

  if (a == b):
    print('Zloty strzAL!')
  else:
      while a != b:
        if (a > b):
          print('To nie ta liczba. Jest za mala.')
        if (a < b):
          print('To nie ta liczba. Jest za duza.')
        b = int(input('Wprowadz inna liczbe: '))
        if (a == b):
          print('ZNakomicie! Wygrales')
          break

  want = input('Czy chcesz grać dalej Tak/Nie: ')
  print("")
  if want in ['T', 'Tak', 'TAK', 't', 'tak']:
    pass
  else:
    break
                
    
  