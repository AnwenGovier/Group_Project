from items import *
from game_map import room

#contains all the items that the user is carrying at any one time
inventory = [item_pistol]
#contains the status of the player, their health etc.
player = {"Name": "Change to a user input name", "Health": 100, "Alive": True, "Intoxicated": False}


#the room that the user is currently situated in
current_room = room["Lobby"]