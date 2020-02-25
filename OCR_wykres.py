# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:33:30 2019

@author: pfenger
"""

import random
import matplotlib    

wynik = {'heads': 0, 'tails': 0}
moneta = ['heads', 'tails']
wykres = []
x = [0]
y = [0]

while True:
    n = int(input('Ile rzutow chcesz wykonac? Podaj liczbe calkowita: '))
    for i in range(n):
        wynik[random.choice(moneta)] += 1
        x.append(wynik['heads'])
        y.append(wynik['tails'])

    
    
    print('Orzel: ', wynik['heads'])
    print('Reszka: ', wynik['tails'])
    from matplotlib import pyplot as plt
    from matplotlib import style
    style.use('bmh')
    plt.scatter(x,y)
    plt.show()
    #print(x) print tylko z ciekawosci do sprawdzenia dla chetnych
    #print(y)

    init = str(input('Czy chcesz grac jeszcze? t/n: '))
    if init in ['t','tak','T', 'TAK', 'Y', 'y', 'yes', 'YES', 'Yes']:
        pass
    else:
        break


