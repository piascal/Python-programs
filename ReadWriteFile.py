# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 14:08:10 2019

@author: pfenger
"""

import os

os.chdir('C:\\Users\\pfenger\\Desktop\\Python')
#words = []
licznik = 0
def reader(file):
    with open(file) as plik1:
    
    max_len = len(max(words, key = len))
    for word in words:
        if len(word) == max_len:
            return print(word)
        
                words = plik1.read().split()
        for i in words:
            if i == ',':
                licznik += 1
            elif i == '.':
                licznik += 1
            
print(licznik)
reader('text.txt')
    