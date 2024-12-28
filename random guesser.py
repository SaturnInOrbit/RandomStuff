import random
import time
import os
game = True
tries = 0
guesses = []

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
	ans = int(input("Guess the number (Enter '0' to see your past guesses): "))
	if ans == 0:
			os.system('cls')
			print("Here's your list of guesses in this session!")
			print(guesses)
			continue
	elif ans == ran:
		print("")
		print("Well I'll be, you got it!")
		time.sleep(2)
		print("")
	
		if tries <= 10:
			print(f"And it only took you {tries} attempts! You're a god at this.")
		elif tries <= 30:
			print(f"And it only took you {tries} attempts! Not bad!")
		elif tries <= 60:
			print(f"And it only took you {tries} attempts! Could be better but still good.")
		elif tries <= 99:
			print(f"And it took you {tries} attempts! Took awhile but you stuck through.")
		elif tries == 100: 
			print(f"It took you {tries} tries! You basically went through every number before guessing it.")
		elif tries >= 101:
			print(f"It took you {tries} attempts! How'd you manage to guess more than a hundred before getting it?")
			time.sleep(3)
			print("")
			print("Wow.")
			print("")
			time.sleep(1)
			print("Just wow.")
		else:
			print("Huh?")
		time.sleep(2)
		print("")
		print("Anyways, that's pretty much it, take care!")
		print("")
		
		break
	else:
		os.system('cls')
		print("WRONG, PLEASE ENTER A DIFFERENT NUMBER AND TRY AGAIN!")
		print("")
		guesses.append(ans)
		guesses.sort()
		tries += 1
		continue