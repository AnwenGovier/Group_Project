from items import *
from game_map import room

#contains all the items that the user is carrying at any one time
inventory = []

#contains the status of the player, their health etc.
player = {"Name": "Change to input", "Health": 100, "Alive": True, "Intoxicated": False}

#this is used to print the dictionary in order
player_stats = ["Name", "Health", "Alive", "Intoxicated"]

#completed fights
completed_fights = {"first stairs fight": False, "fight": False, "second stairs fight": False}


#the room that the user is currently situated in
current_room = room["Lobby"]
