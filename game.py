#!/usr/bin/python3

from game_map import room
from user import *
from items import *
from filter_inputs import *
import random
import os
import time
from subprocess import call

def create_a_list_of_items(items):
	"""
	The following function takes a list of items from a seperate py document items.py
	and returns a string to the user. Each word is seperated by a comma and a space.
	e.g.
	>>> create_a_list_of_items([item_tablets, item_broom])
	'tablets, a broom'
	>>> create_a_list_of_items([item_pistol, item_biscuit])
	'a pistol, a biscuit'
	

	"""
	list_of_items = []
	for i in items:
		#for every x in items, looks up value for variable 'name'
		list_of_items.append(i["name"])
	#list is joined together with a comma and space
	complete_list =', '.join(list_of_items)
	return complete_list

def print_a_list_of_room_items(room):
	"""
	The following function takes a room as an input and displayes the correspoding list
	of items that can be found. It then prints a blank line
	Nothing is printed if there are no items in the room. The list of items for each room 
	is located in the game_map.py amd the definition and name is located in the items.py file.
	The items are displayed in a list where each item is seperated using a comma and a space.
	e.g.
	>>> print_a_list_of_room_items(room["Bar"])
	There is an alcoholic drink here in the room.
	<BLANKLINE>

	>>> print_a_list_of_room_items(room["Alley"])
	There is a biscuit here in the room.
	<BLANKLINE>

	>>> print_a_list_of_room_items(room["Kitchen"])
	There is a kitchen knife here in the room.
	<BLANKLINE>

	"""
	list_of_items = room["items"]
	if len(list_of_items) == 0:
		return;
	else:
		print("There is " + create_a_list_of_items(room["items"]) + " here in the room.")
		print("")

def print_a_list_of_inventory_items(items):
	""" The following code in this function displays the users inventory items exactly how the 
	items are displayed in the room in print_a_list_of_room_items(rooms).
	The difference is the words that are printed with the items.
	
    """

	list_of_items_in_inventory = create_a_list_of_items(items)
	if len(list_of_items_in_inventory) == 0:
		return;
	else:
		print("You have " + create_a_list_of_items(items) +"." )
		print()
            
def print_description_current_room(room):
	"""
	This function displays the description and name that corresponds to the users
	current room. The name of the room is printed in capitals with a blank line before 
	and after it. The description of the room is displayed next with a blank line 
	following afterwards. Finally a list of the items in the room is displayed with a 
	blank line afterwards.
	For example the description for Room 1 is:
	<BLANKLINE>
    ROOM ONE
    <BLANKLINE>
    You are now standing in a deserted bedroom. Clothes are strung everywhere, furniture knocked over. 
	Whoever stayed here left in a hurry...
    <BLANKLINE>
    There is a pistol, a key for the second level here in the room.    
	"""
	n=0
	if player["Intoxicated"] == True:
		os.system("cls")
		for n in range(0, 5):
			for color in('12', '45', 'F0', '2E', '0F'):
				call('cls', shell = True)
				call('color ' + color, shell = True)
				print('\nYou are currently in ' + room['name'].upper() + "\n" + intoxication(room['description']) + "\n")
				print_a_list_of_room_items(room)
				print("\n"+"\n" + "Go home, your drunk!")
				player["Intoxicated"] = False
				time.sleep(0.3)
				n= n+1

	else:
		print('\nYou are currently in ' + room['name'].upper() + "\n" + room['description'] + "\n")
		print_a_list_of_room_items(room)

def exit_entered_leads_to(exits, direction):
	"""
	This function uses a dictionary of exits and a direction (an exit made avaliable
	to the user). It returns the name of the room that they will go to next.
	e.g.
	>>> exit_entered_leads_to(room["Lobby"]["exits"], "west")
	'the hotel bar'
	>>> exit_entered_leads_to(room["Laundry"]["exits"], "north")
	'the back alley'
	>>> exit_entered_leads_to(room["Stairs to the roof"]["exits"], "east")
	'the roof'
	"""
	return room[exits[direction]]["name"]

def print_the_exits_avaliable_to_user(direction, leads_to):
	"""
	The code in this function prints a menu of exits that are avaliable
	to the user. It uses a direction and the name of the next room to do this.
	They should be printed like this:
	GO <EXIT NAME> to <leads to>.
	e.g.
	>>> print_the_exits_avaliable_to_user("east", "Lobby")
	Go EAST to Lobby.

	>>> print_the_exits_avaliable_to_user("north", "Laundry")
	Go NORTH to Laundry.

	"""
	print('Go ' + direction.upper() + ' to ' + leads_to + '.')

def print_menu_of_items_and_exits(exits, room_items, inventory_items):
	"""
	This function displays to the user a list of avaliable exits that they can take to move
	out of their current room. It will also display all of the items in the room in the following
	manner:
	TAKE <ITEM ID> to take <item name>.
	It will also display all of the items in their inventory that they can drop using the following code:
	DROP <ITEM ID> to drop <item name>.
	It splits all of the items in the inventory so that they can be displayed individually to the user.
	e.g.
	The actions avaliable to the player in the bar are as follows:
	You can:
	GO EAST to the lobby.
	GO NORTH to the kitchen.
	TAKE BISCUIT to take a biscuit.
	TAKE ALCOHOL to take an alcoholic drink.
	DROP PISTOL to drop a pistol.
	What do you want to do?
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
	#show items that can be used by the user
	for items in inventory_items:
		items_list = create_a_list_of_items(inventory_items).split(', ')
		for x in items_list:
			item_name = items['name']
			if x == item_name:
				print('USE ' + items['id'].upper() + ' to use ' + items['name'] + '.')			

	print("What do you want to do?")

def is_inputs_a_valid_exit(exits, chosen_exit):
	"""
	The code in this function compares the players chosen exit with the exits in the
	dictionary in game_map.py. If the chosen exit exists then the exit is valid and
	Trus is returned. Else False is returned.
	It is assumed that the input has already been normalised before this function is
	run.
	e.g.
	>>> is_inputs_a_valid_exit(room["Lobby"]["exits"], "west")
	True
	>>> is_inputs_a_valid_exit(room["Kitchen"]["exits"], "east")
	False
	>>> is_inputs_a_valid_exit(room["Kitchen"]["exits"], "south")
	True
	"""
	return chosen_exit in exits

def go(direction):
	"""This function allows the player to traverse the world by inputting 
	a direction. If the direction is valid the current room is updated to reflect the
	players movement from the previous room.
	It also checks that the room is not locked. If it is then it stops the user from entering
	and displays to the user that the room is locked and they didn't answer the question correctly.
	If the room they have now entered is the roof then it will run a seperate py flie Battle.py
	which will allow the player to fight the boss.
	If the new current room is the Stairs to the first floor then again a seperate file is fun,
	stairwellbattle.py, which makes the user fight a man in order to go to the next floor.
	If any of these conditions are not met then the following is printed:
	You cannot go there!
	"""

	global current_room
	if is_inputs_a_valid_exit(current_room['exits'], direction):
		current_room_check = room[current_room['exits'][direction]]
		
		#checks to see if the room is locked
		room_status = locked(current_room_check)

		#if room_status returns True then the room has been unlocked
		if room_status:
			current_room = current_room_check
		else:
			print("Door remains locked!")
			return

		execute_program(current_room)

		#checks to see if another program needs to be executed
		#execute_program(current_room)

	
	else:
		print("You cannot go there!")


def question(current_room):
	"""This function will ask the user a question that will need to be answered 
	correctly to unlock the room"""

	if current_room['name'] == "the stairs to the first floor":
		#This question is number 1 
		print("What colour is the chef's hat?")
		print("Red", "\nPurple", "\nGreen", "\nWhite", "\nTo exit question enter: EXIT")
		return answer(1, current_room)

	elif current_room['name'] == "room three":
		#This question is number 2
		print("What item is found in the ally?")
		print("Biscuit", "\nBroom", "\nkitchen-knife", "\nPhone", "\nTo exit question enter: EXIT")
		return answer(2, current_room)

	elif current_room['name'] == "room five":
		#This question is number 3
		print("What is the name of the bar tender?")
		print("Walter", "\nBen", "\nGerald", "\nLarry", "\nTo exit question enter: EXIT")
		return answer(3, current_room)

	elif current_room['name'] == "room six":
		#This question is number 4
		print("What colour is the drink being served in the bar?")
		print("Pink", "\nBlue", "\nBrown", "\nTo exit question enter: EXIT")
		return answer(4, current_room)

	elif current_room['name'] == "the stairs to the second floor":
		#This question is number 5
		print("What is Mickeys favourite colour?")
		print("Red", "\nPurple", "\nYellow", "\nPink", "\nTo exit question enter: EXIT")
		return answer(5, current_room)

	elif current_room['name'] == "the secret door":
		#This question is number 6
		print("What is in the laundry?")
		print("Spaghetti", "\nShoes", "\nBucket", "\nShirts", "\nTo exit question enter: EXIT")
		return answer(6, current_room)

def answer(question_number, current_room):
	if question_number == 1:

		while True:
			user_ans = input(">>")
			user_ans = user_input_normalisation(user_ans)
			if user_ans == ['purple']:
				return True
				break
			elif user_ans == ['exit']:
				break
			else:
				print("That is the wrong answer, try again!")

	elif question_number == 2:
		while True:
			user_ans = input(">>")
			user_ans = user_input_normalisation(user_ans)
			if user_ans == ['biscuit']:
				return True
				break
			elif user_ans == ['exit']:
				break
			else:
				print("That is the wrong answer, try again!")

	elif question_number == 3:
		while True:
			user_ans = input(">>")
			user_ans = user_input_normalisation(user_ans)
			if user_ans == ['larry']:
				return True
				break
			elif user_ans == ['exit']:
				break
			else:
				print("That is the wrong answer, try again!")

	elif question_number == 4:
		while True:
			user_ans = input(">>")
			user_ans = user_input_normalisation(user_ans)
			if user_ans == ['blue']:
				return True
				break
			elif user_ans == ['exit']:
				break
			else:
				print("That is the wrong answer, try again!")

	elif question_number == 5:
		while True:
			user_ans = input(">>")
			user_ans = user_input_normalisation(user_ans)
			if user_ans == ['red']:
				return True
				break
			elif user_ans == ['exit']:
				break
			else:
				print("That is the wrong answer, try again!")

	elif question_number == 6:
		while True:
			user_ans = input(">>")
			user_ans = user_input_normalisation(user_ans)
			if user_ans == ['spaghetti']:
				return True
				break
			elif user_ans == ['exit']:
				break
			else:
				print("That is the wrong answer, try again!")

def locked(current_room):
	"""This function checks if the users current room is locked or not.
	If it is then it will ask the user a question else if it unlocked (False) then the
	player is allowed to enert the room."""

	for x in current_room:
		if x == 'locked':
			if current_room['locked'] == True:
				if question(current_room):
					current_room['locked'] = False
					print("\n")
					return True
				else:
					return False
	return True

def execute_program(current_room):
	"""
	This function will exectute another program if a certain room is entered. If there is 
	no program attatched to that room nothing will be executed and the current room is 
	returned"""


	if current_room == room["The roof"]:
		#runs another program
		os.system("battle.py")
		#exits program - player died and chose not to continue
		os.system(cls)
		print("Thank you for playing! :D")
		getch()

		exit()


	if current_room['name'] == "the stairs to the first floor":	
		for x in completed_fights:
			if completed_fights["first stairs fight"] == True:
				return current_room
			else:
				os.system("stairwellbattle.py")
				completed_fights["first stairs fight"] = True
				return current_room
		
	if current_room['name'] == "the stairs to the second floor":
		for x in completed_fights:
			if completed_fights["second stairs fight"] == True:
				return current_room
			else:
				os.system("2ndfloorbattle.py")
				completed_fights["second stairs fight"] = True
				return current_room

	if current_room == room["Fight"]:
		for x in completed_fights:
			if completed_fights['fight'] == True:
				return current_room
			else:
				os.system("boxers.py")
				completed_fights['fight'] = True
				return current_room

	if current_room['name'] == "Even deeper into the third floor":
		for x in completed_fights:
			if completed_fights["Maze Fight"] == True:
				return current_room
			else:
				os.system("maze_battle1.py")
				completed_fights["Maze Fight"] = True
				return current_room


	
def is_item_in_list(item, items):
    """
    This function compares the users input with the items that are currently avaliable in the room.
    If it can find then item then it returns True else it will return False.
    For example if the function checked to see if there is a biscuit in the alley then it would
    return True but if it checked that a broom is in the alley, then False would be returned.
    """
    for i in items:
        id = i["id"]
        if item == id:
            return True
    return False

def remove_item_from_current_room(item_id, items):
    """
	This function removes the requested item from the current room. 
	It will then add the item into the players inventory. 
	The changes will be displayed in the print_menu_of_items_and_exits function.
    """
    items_in_room = []
    for i in items:
        id = i["id"]
        if item_id == id:
            inventory.append(i)         
        else:
            items_in_room.append(i)
    current_room["items"] = items_in_room

    return False
       

def is_item_in_inventory(item, items):
    """
    This function compares the users input with the items that they have in their inventory.
    It it can find the requested item then True is return. Else False is returned.
	"""
    for i in items:
        id = i["id"]
        if item == id:
            return True
    return False


def remove_item_from_inventory(item_id, items):
	"""
	This function removes the requested item in the players inventory and appends it to the
	list of items in the players current room.
	The changes are displayed in the print_menu_of_items_and_exits function for the player.
	""" 
	global inventory
	items_in_inventory = []
	for i in items:
		id = i["id"]
		if item_id == id:
			current_room["items"].append(i)
		else:
			items_in_inventory.append(i)
	inventory = items_in_inventory
	return False

def take_an_item(item_id):
	"""
	This function allows the user to take an item from the current room.
	It runs two seperate functions, one to make sure the chosen item is valid and one to
	move the item from the room into the players inventory.
	If it cannot do any of these things then You cannot take that is displayed.
	"""
	global inventory
	if is_item_in_list(item_id, current_room["items"]):
		remove_item_from_current_room(item_id, current_room["items"])
		return inventory
	else:
		print("You cannot take that.")

def drop_an_item(item_id):
	"""
	This function allows the user to take an item from their inventory.
	It will again run two seperate functions like the take_an_item function but instead an item
	is moved from the inventory and into the players current room.
	Else You cannot drop that is displayed.
	"""
	if is_item_in_inventory(item_id, inventory):
		remove_item_from_inventory(item_id, inventory)
		return inventory
	else:
		print("You cannot drop that")

def use_item_in_inventory(item_id, items):
	'''
	This function allows the user to use an item that they are carrying in their inventory.
	The health assigned to the item which will either add to or subtract off the players
	health. 
	If the player uses the alcohol, then their intoxication is turned to true and the description of their 
	current room will become scrambled using intoxication function.
	If the item has no health properties then nothing happens and a message is displayed telling the user
	that it has no use to them.
	'''
	global inventory
	global player

	item_in_inventory = []
	for i in items:
		id = i["id"]
		if item_id == id:
			if i["health"] != 0:
				player["Health"] = player["Health"] + i["health"]
				if i == item_alcohol and player["Intoxicated"] == False:
					player["Intoxicated"] = True
					print("YOU ARE NOW INTOXICATED!!")
			else:
				print("This item has no use to you. It has been put back in your inventory.")
				item_in_inventory.append(i)
		else:
			item_in_inventory.append(i)
	inventory = item_in_inventory
	return False


def use_item(item_id):
	"""NEED TO FIGURE OUT CODE FOR THIS"""
	if is_item_in_inventory(item_id, inventory):
		use_item_in_inventory(item_id, inventory)
		print ("Your health is now " + str(player["Health"]))
		return inventory
		return player
	else:
		print("You cannot use this")
	

def execute_command(command):
	"""
	This function takes a command that has been returned as a list of words after being normalised
	and, depending on the type of action, executes either execute_GO, TAKE, DROP, USE.
	For example:

	'go south' would take the user to the room that is south of their current room.

	'take biscuit' would take the item from the room and move it into the players inventory.

	'drop broom' would take the item from the players inventory and add it to the current room. 
	"""
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
	"""
	This function deals damage to the player and updates their player stats.
	If the player's health goes below 0 they will die and a message will appear
	indicating this.
	For example:
	player["health"] = 0 then, You have died will be displayed.
	However if,
	player["health"] = 10 then, You have taken <damage> damage.
	"""
	player["health"] = player["health"] - damage
	if player["health"] < 0:
		player["health"] = 0
		player["alive"] = False
		print("You have died!")
	else:
		print("You have taken " + str(damage) + " damage.")


def damage_dealt_by_npc(room):
	"""
	This function takes the npc's name and see how much damage they deal.
	The value returned is the amount of damage that has been dealt.
	"""
	
	npc_damage = ''
	for y in room:
		npc_list = room[y]['npc']
		for x in npc_list:
			npc_state = x['npc_state']
			for q in npc_state:
				npc_damage = q['damage']
				return npc_damage

def npc_name(room):
	"""
	This function returns the npc dictionary for an npc in a particular room.
	This looks in rooms, looks at npc's in room, looks at npcs attributes and 
	returns their name.
	"""
	
	npc_name= ''
	npc_list= ''
	for y in room:
		npc_list = room[y]['npc']
		for x in npc_list:
			npc_name = x['name']
			return npc_name
	
def item_damage(item_id):
	"""
	This function returns the damage value for an item.
	"""
	for x in items:
		if item_id == items['id']:
			print(x)


def intoxication(text):
	"""
	This function causes each character to have a 1/5 chance of being replaced by a random letter from the string of letters.
	The string includes the description of the current room.
	
	If there is 0% chance of a random character chosen, result will be the same as input
	>>> import random
	>>> myrand = lambda x, y: 1
	>>> mychoice = lambda x: "A"
	>>> random.randint = myrand
	>>> random.choice = mychoice
	>>> intoxication("Hello World")
	'Hello World'

	If there is 100% chance of a random character chosen, result will be the same as 'AAAAAAAAAAA'
	>>> import random
	>>> myrand = lambda x, y: 0
	>>> mychoice = lambda x: "A"
	>>> random.randint = myrand
	>>> random.choice = mychoice
	>>> intoxication("Hello World")
	'AAAAAAAAAAA'

	If every second character is replaced
	>>> import random
	>>> thisone = 0
	>>> def myrand(x, y): global thisone; thisone+=1; return thisone % 2
	>>> mychoice = lambda x: "A"
	>>> random.randint = myrand
	>>> random.choice = mychoice
	>>> intoxication("Hello World")
	'HAlAoAWArAd'

	If every third character is replaced
	>>> import random
	>>> thisone = 0
	>>> def myrand(x, y): global thisone; thisone+=1; return thisone % 3
	>>> mychoice = lambda x: "A"
	>>> random.randint = myrand
	>>> random.choice = mychoice
	>>> intoxication("Hello World")
	'HeAloAWoAld'
	"""

	string_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	text = "".join(i if random.randint(0,4) else random.choice(string_letters) for i in text)	

	return text

def menu(exits, room_items, inventory_items):
	"""
	This function prints a menu of actions using the print_menu_of_items_and_exits function using
	a dictionary of valid exits in the room and a list of items that can be found there or are carried
	by the player. It will allow the player to enter a command and then normalises what they type, before 
	returning it. 
	"""
	#display menu
	print_menu_of_items_and_exits(exits, room_items, inventory_items)

	#read the player's input
	user_input = input('>> ')

	#normalise the input
	normalised_user_input = user_input_normalisation(user_input)

	return(normalised_user_input)


def move_to_another_room(exits, direction):
	"""
	This function returns the room into which the player 
	will move to if the input contains a valid exit.
	e.g.
	>>> move_to_another_room(room["Lobby"]["exits"], "north") == room["Kitchen"]
	True
	>>> move_to_another_room(room["Bar"]["exits"], "north") == room["Lobby"]
	False
	"""
	return room[exits[direction]]

def stats(player, input_name):
	"""
	This function displays the players stats for the user.
	"""
	print(" " + "_" * 25)
	for x in player_stats:
		if x == 'Name':
			player['Name'] = input_name
		print("| " + x + ": " + str(player[x]) + (" " * (22 - (len(x) + len(str(player[x]))))) + "|")

	print("|" + "_" * 25 + "|")
	print(input("Press the enter key to continue."))
		


#this function will run the entire game and will call the foundation functions. These in turn will call any other functions that they need.


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
