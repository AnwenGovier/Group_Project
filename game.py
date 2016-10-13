#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from gameparser import *

def list_of_items(items):
	item_list=[]
	for x in items:
		#for every x in items, looks up value for variable 'name'
		item_list.append(x['name'])
	#list is joined together with a comma and space
	complete_list =', '.join(item_list)
	return complete_list

def print_room_items(rooms):
	#if there is something in the room display items
	if len(list_of_items(room['items'])) != 0:
		print('There is ' + list_of_items(room['items']) + " here.\n")

def print_inventory_items(items):
	#if there are items in your inventory print items
	if items != 0:
		print('You have ' + list_of_items(items) + '.\n')

def print_room(room):
	print('\n You are in ' + room['name'].upper() + '\n')
	print(room['description'] + '\n')
	print_room_items(room)

def exit_leads_to(exits, direction):
	return rooms[exits[direction]]['name']

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
