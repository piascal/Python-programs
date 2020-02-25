# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:47:29 2019

@author: pfenger
"""
import random
length = int(input('Jaka ma byc dlugosc hasla? Podaj cyfre lub liczbe: '))
znaki = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's',
         't', 'u', 'w', 'z', 'x', 'y', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
if (length < 6):
    print('Haslo jest za krotkie. Minimalna liczba znakow wynosi 6.')
else:
    for i in range(length):
        password = random.choice(znaki)
        print(password, end ='')
