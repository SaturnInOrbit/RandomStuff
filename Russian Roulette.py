# Russian Roulette Simulator

import random
import time
import os

os.system('cls')
print('Welcome to a game of Russian Roulette!')
time.sleep(2)
print()
time.sleep(1)
print('Two die will be rolled and if they land on the same number, you die!')

print("Try your luck and see how long 'till you die!")
print()
time.sleep(2)
print("Or if you're lucky, try and last 15 times then you win! Should be easy for you")
print()
time.sleep(1)
print('Ready?')
print()
time.sleep(1)
input('Enter anything to continue: ')
os.system('cls')

life = 1
gun = True
while gun:
    rr = random.randint(1,6)
    die = random.randint(1,6)
    print('The first dice rolled...')
    time.sleep(2)
    print(f'{rr}!')
    print()
    time.sleep(1)
    print('The second dice rolled...')
    time.sleep(2)
    print(f'{die}!')
    print()
    time.sleep(2)
    if rr == die:
        os.system('cls')
        print('Oops')
        print()
        time.sleep(1)
        print('You died')
        print()
        time.sleep(1)
        print(f'You at least lived {life} times though before succumbing!')
        time.sleep(1)
        print()
        print('Thanks for playing!')
        gun = False
    else:
        life += 1
        cont = input('Continue? (Y/N): ')
        if cont.lower() == 'n':

            break
            
        else:
            continue
