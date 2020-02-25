"""
Created on Wed Nov 13 16:15:59 2019

@author: pfenger
In this game program should randomly generate a number between 1 and 6 then the 
program will print what that number is. It should then ask you if you’d like to 
roll again. For this project, you’ll need to set the min and max number that 
your dice can produce. For the average die, that means a minimum of 1 and a 
maximum of 6. You’ll also want a function that randomly grabs a number within 
that range and prints it.  

"""
import random
import matplotlib.pyplot as plt
tablica = []
print("Welcome to the roll dice simulator!")
def kostka():
    z = random.randint(1,6)
    print(z)
    tablica.append(z)

while True:
    user = str(input("Do you wanna roll the dice? [y/n] " ))
    if user in ["y", "Y", "yes", "Yes", "YES"]:
        kostka()
    else:
        break

user2 = str(input("Do you wanna print the chart? [y/n] " ))   
if user2 in ["y", "Y", "yes", "Yes", "YES"]:
    from matplotlib import style
    style.use('bmh')
    plt.plot(tablica)
# Add title and axis names
    plt.title('Your results of rolling the dice')
    plt.xlabel('Rolls')
    plt.ylabel('Values')
    

    plt.show()
