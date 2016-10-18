import time
from subprocess import call
import random


def drunk(text):
	drunk_talk = intoxacation(text)
	for color in('12', '45', 'F0', '2E', '0F'):
		call('cls', shell = True)
		call('color ' + color, shell = True)
		print(drunk_talk)
		time.sleep(0.3)



def intoxacation(text):
	string_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	text = "".join(i if random.randint(0,4) else random.choice(string_letters) for i in text)	

	return text

n = 0
some_text = """
ou are standing in a small hotel in London.
Your boss, Chief Inspector Jing has ordered you to take down the 
head of the London Mafia, Dr Kirill. Your sources tell 
you that he's hidden somewhere in this hotel. Find him. 
You can go west to the hotel bar, north to the 
kitchen and east to the first floor stairs."""
for n in range(0, 5):
	drunk(some_text)
	n = n + 1

"""
print ("\n\n\n\n\n\n\n\n\n\n\n                   Enter the times you need to prepare (1-10): ")

#colours (blue,gree) (red, purple) (bright white, black), (green, light yellow)
"""