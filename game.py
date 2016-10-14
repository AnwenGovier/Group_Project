#!/usr/bin/python3

from game_map import rooms
from user import *
from items import *
from filter_inputs import *

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
	complete_list =', '.join(item_list)
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
	if len(create_a_list_of_items(room['items'])) != 0:
		print('There is ' + create_a_list_of_items(room['items']) + " here in the room.\n")

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
	print()
	print('You are currently in ' + room['name'].upper())
	print()
	print(room['description'])
	print()
	print_a_list_of_room_items(room)

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
	return rooms[exits[direction]]["name"]

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
pass
#add this

def is_inputs_a_valid_exit(exits, chosen_exit):
pass
#add this

def go(direction):
pass
#add this

def take_an_item(item_id):
#add this
pass
def drop_an_item(item_id):
#add this
pass
def use_item(item_id):
#add this
pass
def execute_command(command):
pass
#add this
pass

def intoxication(text):
	"""This function causes each character to have a 1/5 chance of being replaced by a random letter from the string of letters
	
	INSERT DOCTEST HERE
	"""
	import random
	string_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	text = "".join(i if random.randint(0,4) else random.choice(string_letters) for i in text)	

	return text

def menu(exits, room_items, inventory_items):
pass
#add this

def move_to_another_room(exits, direction):
pass
#add this

def main_program():
pass
#add this

if __name__ == "__main__":
	main()
