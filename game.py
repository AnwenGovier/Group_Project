#!/usr/bin/python3

from game_map import rooms
from user import *
from items import *
from filter_inputs import *

def create_a_list_of_items(items):
	"""
	"""
	list_of_items=[]
	for i in items:
		#for every x in items, looks up value for variable 'name'
		list_of_items.append(i["name"])
	#list is joined together with a comma and space
	complete_list =', '.join(item_list)
	return complete_list

def print_a_list_of_room_items(rooms):
	#if there is something in the room display items
	if len(create_a_list_of_items(room['items'])) != 0:
		print('There is ' + create_a_list_of_items(room['items']) + " here for you to pick up.\n")

def print_a_list_of_inventory_items(items):
	#if there are items in your inventory print items
	if items != 0:
		print('You are carrying ' + create_a_list_of_items(items) + '.\n')

def print_decription_current_room(room):
	print()
	print('You are currently in ' + room['name'].upper())
	print()
	print(room['description'])
	print()
	print_a_list_of_room_items(room)

def exit_leads_to(exits, direction):
	return rooms[exits[direction]]["name"]

def print_exit(direction, leads_to):
	print('Go ' + direction.upper() + ' to ' + leads_to + '.')

def print_menu(exits, room_items, inv_items):


def is_valid_exit(exits, chosen_exit):


def execute_go(direction):


def execute_take(item_id):


def execute_drop(item_id):


def execute_command(command):


def intoxication(text):
	#This function encrypts the description of the room if the player is intoxicated
	


def menu(exits, room_items, inv_items):


def move(exits, direction):


def main():


if __name__ == "__main__":
	main()
