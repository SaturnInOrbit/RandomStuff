import random
import time
import os
game = True

os.system('cls')
print("Welcome to the guess the number game!")
print("")
time.sleep(1)
print("In this game, you must enter a number between 1-100 and try")
print("to have your answer be the same as the randomly generated one")
time.sleep(2)
print("Go ahead, try it out!")
print("")
input("Enter anything to continue...")
os.system('cls')

ran = (random.randint(1,100))
while game:
	ans = int(input("Guess the number: "))
	if ans == ran:
		print("")
		print("Well I'll be, you got it!")
		time.sleep(2)
		print("That's pretty much it, take care!")
		break
	else:
		print("")
		print("WRONG, TRY AGAIN!")
		continue