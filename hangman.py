#importing the time module
import time
import random

#welcoming user
    
'''
schemat programu:
1. program losuje słowo #random
2. uzytkownik podaje literke #uswer input
3. program sprawdza czy podana literka jest w slowie #if 
4. jezeli jest - wyswietla literke na pozycji w slowie
5. jezlei nie - wyswietla komunikat - prosze o ponowny wybor literki
6. ilosc prob = 6
'''

print('''Witaj w programie hangman. Gra polega na zgadnieciu slowa, poprzez zgadywanie jego
       pojedynczych literek.'''.ljust(10))
print('-'.ljust(80, '-'))
tablica = ['komputer', 'animozja', 'wojna', 'dziewica', 'zalotnik', 'ignorant', 'kolega']
slowo = random.choice(tablica)
zgaduj = []
x = 6
while True:
    for i in slowo:
        zgaduj.append(i)
        print('[_]' * len(slowo))
        print()
        literka = str(input('Zgadnij jedna literke. masz {} prob:\n'.format(x)))
        for character in slowo:
            print('[_]', end =' ')
            if character == literka:
                print(character)
            else:
                x = x - 1
                print(r'Nie zgadles :( Masz jeszcze {} prob.\n Sproboj ponownie!'.format(x))
    if x == 0:
        break
    
    




            
        


