#!/usr/bin/python3

from game_map import room
from user import *
from items import *
from filter_inputs import *
import random
import os

def create_a_list_of_items(items):
	"""
	The following function takes a list of items from a seperate py document items.py
	and returns a string to the user. Each word is seperated by a comma and a space.
	e.g.
	>>> create_a_list_of_items([item_room5_key, item_tablets, item_broom])
	'a key for room 5, tablets, a broom'
	>>> create_a_list_of_items([item_pistol, item_biscuit])
	'a pistol, a biscuit'
	>>> create_a_list_of_items([item_second_level_key, item_secret_key, item_alcohol])
	'a key for the second level, a secret key, an alcoholic drink'

	"""
	list_of_items = []
	for i in items:
		#for every x in items, looks up value for variable 'name'
		list_of_items.append(i["name"])
	#list is joined together with a comma and space
	complete_list =', '.join(list_of_items)
	return complete_list

def print_a_list_of_room_items(rooms):
	"""
	The following function takes a room as an input and displayes the correspoding list
	of items that can be found. It then prints a blank line
	Nothing is printed if there are no items in the room. The list of items for each room 
	is located in the game_map.py amd the definition and name is located in the items.py file.
	The items are displayed in a list where each item is seperated using a comma and a space.
	e.g.
	>>>print_a_list_of_items(rooms["Bar"])
	There is a biscuit, an alcoholic drink here in the room.
	<BLANKLINE>
	>>>print_a_list_of_items(rooms["Alley"])
	(no output)
	>>>print_a_list_of_items(rooms["Kitchen"])
	There is a kitchen knife here in the room.
	<BLANKLINE>

	"""
	if len(create_a_list_of_items(rooms['items'])) != 0:
		print('There is ' + create_a_list_of_items(rooms['items']) + " here in the room.\n")

def print_a_list_of_inventory_items(items):
	"""
	The following code in this function displays the users inventory items exactly how the 
	items are displayed in the room in print_a_list_of_room_items(rooms).
	The difference is the words that are printed with the items.
	e.g.
	>>> print_a_list_of_inventory_items(inventory)
	(no output)
    """
	if items != 0:
		print('You are carrying ' + create_a_list_of_items(items) + '.\n')

def print_description_current_room(room):
	"""
	This function displays the description and name that corresponds to the users
	current room. The name of the room is printed in capitals with a blank line before 
	and after it. The description of the room is displayed next with a blank line 
	following afterwards. Finally a list of the items in the room is displayed with a 
	blank line afterwards.
	e.g.
	>>>print_description_current_room(rooms["Alley"])
	<BLANKLINE>
    THE BACK ALLEY
    <BLANKLINE>
    You are now standing in a back alley behind the hotel.
	Dustbins line the street giving off a foul odour of waste and decay. 
	You can go south to go back to the Laundry room.
    <BLANKLINE>
    
    >>>print_description_current_room(rooms["Room 1"])
	<BLANKLINE>
    ROOM ONE
    <BLANKLINE>
    You are now standing in a deserted bedroom. Clothes are dtrung everywhere, furniture knocked over. 
	Whoever stayed here left in a hurry...
    <BLANKLINE>
    There is a pistol, a key for the second level here in the room.

    >>>print_description_current_room(rooms["Further in"])
	<BLANKLINE>
    FURTHER IN
    <BLANKLINE>
    A plaster board wall blocks your path. 
	You can go south to go back.
    <BLANKLINE>
	"""
	
	print('\nYou are currently in ' + room['name'].upper() + "\n" + room['description'] + "\n" + str(print_a_list_of_room_items(room)))
	

def exit_entered_leads_to(exits, direction):
	"""
	This function uses a dictionary of exits and a direction (an exit made avaliable
	to the user). It returns the name of the room that they will go to next.
	e.g.
	>>>exit_entered_leads_to["Lobby"]["exits"], "west"
	"the hotel bar"
	>>>exit_entered_leads_to["Laundry"]["exits"], "north"
	"the back alley"
	>>>exit_entered_leads_to["Stairs to the roof"]["exits"], "east"
	"roof"
	"""
	return room[exits[direction]]["name"]

def print_the_exits_avaliable_to_user(direction, leads_to):
	"""
	The code in this function prints a menu of exits that are avaliable
	to the user. It uses a direction and the name of the room to do this.
	They should be printed like this:
	GO <EXIT NAME> to <leads to>.
	e.g.
	>>>print_the_exits_avaliable_to_user("east", "Lobby")
	GO EAST to the hotel lobby.
	>>>print_the_exits_avaliable_to_user("north", "Laundry")
	GO EAST to the laundry room.
	>>>print_the_exits_avaliable_to_user("west", "Room 1")
	GO WEST to room one.
	"""
	print('Go ' + direction.upper() + ' to ' + leads_to + '.')

def print_menu_of_items_and_exits(exits, room_items, inventory_items):
	"""
	Please add test
	"""

	print("You can:")
	#show available exits to the user
	for direction in exits:
		#print the exit name and where it leads to
		print_the_exits_avaliable_to_user(direction, exit_entered_leads_to(exits, direction))

	#show available items that the user can take from room
	for items in current_room['items']:
		print('TAKE ' + items['id'].upper() + ' to take ' + items['name'] + '.')
	
	#show items that can be dropped by the user
	for items in inventory_items:
		items_list = create_a_list_of_items(inventory_items).split(', ')
		for x in items_list:
			item_name = items['name']
			if x == item_name:
				print('DROP ' + items['id'].upper() + ' to drop ' + items['name'] + '.')

def is_inputs_a_valid_exit(exits, chosen_exit):
	"""
	ADD TEST
	"""
	return chosen_exit in exits

def go(direction):
	"""This function allows the player to traverse the world by inputting 
	a direction"""
	global current_room
	if is_inputs_a_valid_exit(current_room['exits'], direction):
		current_room_check = room[current_room['exits'][direction]]
		
		#checks to see if another program needs to be executed
		execute_program(current_room)

		#checks to see if the room is locked
		room_status = locked(current_room_check)
		if room_status == 'False':
			print("The room is locked and you didn't answer the question correctly!")
			break
		if current_room == room["The roof"]:
			#runs another program
			os.system("battle.py")
			#exits program - player died and chose not to continue
			exit()
		if current_room == room["Stairs to first floor"]:
			os.system("stairwellbattle.py")
			return current_room
	else:
		print("You cannot go there!")


def question(current_room):
	"""This function will ask the user a question that will need to be answered 
	correctly to unlock the room."""
	if current_room == room["the stairs to the first floor"]:
		#This question is number 1 
		print("What colour is the chef's hat?")
		print("Red \n", "Purple\n", "Green\n", "White\n", "To exit question enter: EXIT")
		return answer(1, current_room)

	elif current_room == room["room three"]:
		#This question is number 2
		print("What item is found in the ally?")
		print("Biscuit\n", "Broom\n", "kitchen-knife\n", "Phone\n", "To exit question enter: EXIT")
		return answer(2, current_room)

	elif current_room == room["room five"]:
		#This question is number 3
		print("What is the name of the bar tender?")
		print("Walter\n", "Ben\n", "Gerald\n", "Larry\n", "To exit question enter: EXIT")
		return answer(3, current_room)

	elif current_room == room["room six"]:
		#This question is number 4
		print("What colour is the drink being served in the bar?")
		print("Pink\n", "Blue\n", "Brown\n", "To exit question enter: EXIT")
		return answer(4, current_room)

	elif current_room == room["the stairs to the second floor"]:
		#This question is number 5
		print("What is Mickeys favourite colour?")
		print("Red\n", "Purple\n", "Yellow\n", "Pink\n", "To exit question enter: EXIT")
		return answer(5, current_room)

	elif current_room == room["the secret door"]:
		#This question is number 6
		print("What is in the laundry?")
		print("Spagetti\n", "Shoes\n", "Bucket\n", "Shirts\n", "To exit question enter: EXIT")
		return answer(6, current_room)

def answer(question_number, current_room):
	if question_number == '1':
		while True:
			user_ans = input(">>")
			user_ans = user_input_normalisation(user_ans)
			if user_ans == 'purple':
				return True
				break
			elif user_ans == 'exit':
				break
			else:
				print("That is the wrong answer, try again!")

	elif question_number == '2':
		while True:
			user_ans = input(">>")
			user_ans = user_input_normalisation(user_ans)
			if user_ans == 'biscuit':
				return True
				break
			elif user_ans == 'exit':
				break

	elif question_number == '3':
		while True:
			user_ans = input(">>")
			user_ans = user_input_normalisation(user_ans)
			if user_ans == 'larry':
				return True
				break
			elif user_ans == 'exit':
				break

	elif question_number == '4':
		while True:
			user_ans = input(">>")
			user_ans = user_input_normalisation(user_ans)
			if user_ans == 'blue':
				return True
				break
			elif user_ans == 'exit':
				break

	elif question_number == '5':
		while True:
			user_ans = input(">>")
			user_ans = user_input_normalisation(user_ans)
			if user_ans == 'red':
				return True
				break
			elif user_ans == 'exit':
				break

	elif question_number == '6':
		while True:
			user_ans = input(">>")
			user_ans = user_input_normalisation(user_ans)
			if user_ans == 'spagetti':
				return True
				break
			elif user_ans == 'exit':
				break


def locked(current_room):
	"""This function checks if the room is locked or not"""

	for x in current_room:
		if x == 'locked':
			if current_room['locked'] == True:
				if question(current_room):
					current_room['locked'] == False
				else:
					return False


def execute_program(current_room):
	"""This function will exectute another program if a certain room is entered. If there is 
	no program attatched to that room nothing will be executed and the current room is 
	returned."""

	


def take_an_item(item_id):
	"""This function allows the user to take an item from the
	current room"""

	#small note:- i dont think the 'you cannot take this' works 

	for item in current_room['items']:
		if item_id != item['id'] and current_room['items']:
			pass
		elif item_id == item['id']:
			current_room['items'].remove(item)
			inventory.append(item)
			print(item['name'] + " added to your inventory.")
		else:
			print("You cannot take that.")


def drop_an_item(item_id):
	"""This function allows the user to drop an item in their inventory
	in the room that they're currently in."""
	for item in inventory:
		if item_id != item['id'] and current_room['items']:
			pass
		elif item_id == item['id']:
			inventory.remove(item)
			current_room['items'].append(item)
			print("You dropped " + item['name'] + ".")
		else:
			print("You cannot drop that.")


def use_item(item_id):
	"""NEED TO FIGURE OUT CODE FOR THIS"""




#add this
pass


def execute_command(command):
	"""This function takes a command and, depending on the type of 
	action, executes either execute_GO, TAKE, DROP, USE."""
	if 0 == len(command):
		return

	if command[0] == 'go':
		if len(command) > 1:
			go(command[1])
		else:
			print("Go where?")

	elif command[0] == 'take':
		if len(command) > 1:
			take_an_item(command[1])
		else:
			print("Take what?")

	elif command[0] == 'drop':
		if len(command) > 1:
			drop_an_item(command[1])
		else:
			print("Drop what?")

	elif command[0] == 'use':
		if len(command) > 1:
			use_item(command[1])
		else:
			print("Use what?")

	else:
		print("This is an invalid command.")

def take_damage_player(player, damage):
	"""This function deals damage to the player and updates their player stats.
	If the player's health goes below 0 they will die and a message will appear
	indicating this."""
	player["health"] = player["health"] - damage
	if player["health"] < 0:
		player["health"] = 0
		player["alive"] = False
		print("You have died!")
	else:
		print("You have taken " + str(damage) + " damage.")


def damage_dealt_by_npc(room):
	"""This function takes the npc's name and see how much damage they deal.
	The value returned is the amount of damage that has been dealt."""
	
	npc_damage = ''
	for y in room:
		npc_list = room[y]['npc']
		for x in npc_list:
			npc_state = x['npc_state']
			for q in npc_state:
				npc_damage = q['damage']
				return npc_damage

def npc_name(room):
	"""This function returns the npc dictionary for an npc in a particular room.
	This looks in rooms, looks at npc's in room, looks at npcs attributes and 
	returns their name."""

	
	npc_name= ''
	npc_list= ''
	for y in room:
		npc_list = room[y]['npc']
		for x in npc_list:
			npc_name = x['name']
			return npc_name
	
def item_damage(item_id):
	"""This function returns the damage value for an item."""
	for x in items:
		if item_id == items['id']:
			print(x)


def intoxication(text):
	"""
	This function causes each character to have a 1/5 chance of being replaced by a random letter from the string of letters


	INSERT DOCTEST HERE
	"""
	string_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	text = "".join(i if random.randint(0,4) else random.choice(string_letters) for i in text)	

	return text

def menu(exits, room_items, inventory_items):
	"""This function calls the function """

	#display menu
	print_menu_of_items_and_exits(exits, room_items, inventory_items)

	#read the player's input
	user_input = input(">> ")

	#normalise the input
	normalised_user_input = user_input_normalisation(user_input)

	return(normalised_user_input)


def move_to_another_room(exits, direction):
	"""This function returns the room into which the player 
	will move to."""
	return room[exits[direction]]

def stats(player, input_name):
	"""This function displays the players stats."""
	print(" " + "_" * 25)
	for x in player_stats:
		if x == 'Name':
			player['Name'] = input_name
		print("| " + x + ": " + str(player[x]) + (" " * (22 - (len(x) + len(str(player[x]))))) + "|")
	
	print("|" + "_" * 25 + "|")
	print(input("Press the enter key to continue."))


def main():
	prompt_user = input("Please enter your name: ")
	stats(player, prompt_user)

	#main game loop
	while True:
		#display game status (room description, inventory etc)
		print_description_current_room(current_room)
		print_a_list_of_inventory_items(inventory)

		#show the menu with possible actions and ask the player what they want to do
		command = menu(current_room['exits'], current_room['items'], inventory)

		#execute the player's command
		execute_command(command)

if __name__ == "__main__":
	main()
