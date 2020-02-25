# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 11:47:31 2019

@author: pfenger
"""
import random
user_win = 0
comp_win = 0
print('Welcome to the Rock, Paper, Scissors game!')

def choose_option(str):
    userchoice = input('Please choose between Rock, Paper, Scissors: ')
    if userchoice in ['Rock', 'rock', 'ro', 'rokc', 'r', 'roc', 'rok']:
        userchoice = 'Rock'
    elif userchoice in ['Paper', 'paper', 'pap', 'p', 'ppr','papr' ]:
        userchoice = 'Paper'
    elif userchoice in ['Scissors', 'scissors', 'scsrs','s','sci','scsors','sss','ss']:
        userchoice = 'Scissors'
    else:
        print("I don't understand. Try again")
        choose_option(str)
    return userchoice


def comp_option():
    a = random.randint(0,2)
    b = ['Rock', 'Paper', 'Scissors']
    compchoice = b[a]
    return compchoice
            
    print("")
    

while True:
    print("")
    userchoice = choose_option(str)
    compchoice = comp_option()
    
    if (userchoice == 'Rock'):
        if (compchoice == 'Rock'):
            print("Damn it man! It's a tie!")
        elif (compchoice == 'Paper'):
            print ("Fuck this. You loose with your rock agains paper.")
            comp_win += 1
        elif (compchoice == 'Scissors'):
            print ("Oh yeah baby! You win agains scissors.")
            user_win += 1
            
    elif (userchoice == 'Paper'):
        if (compchoice == 'Rock'):
            print("Oh yeah! It's a win!")
            user_win += 1
        elif (compchoice == 'Paper'):
            print ("Sheeesh. This is a tie")
        elif (compchoice == 'Scissors'):
            print ("Oh no. The AI wins!")
            comp_win += 1
            
    elif (userchoice == 'Scissors'):
        if (compchoice == 'Rock'):
            print("Fuck this. Computer hammers you with its rock")
            comp_win += 1
        elif (compchoice == 'Paper'):
            print('Hell yeah! You cut his fucking papers in half')
            user_win += 1
        elif (compchoice == 'Scissors'):
            print('What a fucking joke. TIE this')
            
    print("")
    
    want = input('Do you want to play again y/n ')
    
    if want in ['Yes', 'Y', 'y', 'yes']:
        pass
    elif want in ['No', 'no', 'n', 'N']:
        break
    else:
        break
print("")
print("")
print('Game over')
print("User wins = ", user_win)
print("Computer wins = ", comp_win)
    
            
            
            
            
            
            
            
            
            
            
            
            
