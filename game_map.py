from items import *
from npc import *

#ground floor rooms
room_lobby = {
	"name" : "the hotel lobby",
	"description" : """
You are standing in a small hotel in London.
Your boss, Chief Inspector Jing has ordered you to take down the 
head of the London Mafia, Dr Kirill. Your sources tell 
you that he's hidden somewhere in this hotel. Find him. 
You can go west to the hotel bar, north to the 
kitchen and east to the first floor stairs.""",
	"exits" : {"west" : "Bar", "north" : "Kitchen", "east" : "Stairs to first floor"},
	"items" : [],
	"locked" : False,
	"npc": []
}

room_kitchen = {
	"name": "the hotel kitchen",
	"description" : """
You are standing in the hotel kitchen. 
Chefs and waiters work busily around you, preparing dishes
for the day. No one stops to notice you. The head chef is wearing a purple hat.
You can go north to the laundry room, south to go back to the 
lobby or west to the bar.""",
	"exits" : {"north" : "Laundry", "west" : "Bar", "south" : "Lobby"},
	"items" : [item_kitchen_knife],
	"locked" : False,
	"npc": []
}

room_bar = {
	"name": "the hotel bar",
	"description" : """
You are now standing by the hotel's bar. Its deserted. 
A waiter stands polishing glasses behind the bar, humming to 
an old radio. 
You can go east to the lobby, north to the kitchen or you 
could talk to the waiter. """,
	"exits" : {"east" : "Lobby", "north" : "Kitchen"},
	"items" : [item_biscuit, item_alcohol],
	"locked" : False,
	"npc": [npc_bar_man]
}

stairs_to_first = {
	"name": "the stairs to the first floor",
	"description" : """
The stairs ahead will take you to the first floor.
One of the Python's men is guarding the stairs and will 
not let you pass. 
You can go west to go back to the lobby or you could 
confront the bad guy by going east.""",
	"exits" : {"west" : "Lobby", "east" : "Hallway"},
	"items" : [],
	"locked" : True,
	"npc": []
}

room_laundry = {
	"name": "the laundry room",
	"description" : """
You are now standing in the laundry room in the hotel. 
Tumble dryers spin around you. No one is here.
You can go north to the back alley or south to the kitchen. """,
	"exits" : {"north" : "Alley", "south" : "Kitchen"},
	"items" : [item_broom],
	"locked" : False,
	"npc": []
}

room_alley = {
	"name": "the back alley",
	"description" : """
You are now standing in a back alley behind the hotel.
Dustbins line the street giving off a foul odour of waste and decay. 
You can go south to go back to the Laundry room. """,
	"exits" : {"south" : "Laundry"},
	"items" : [],
	"locked" : False,
	"npc": []
}

#first floor rooms
first_floor_hallway = {
	"name": "the first floor hallway",
	"description" : """
You are now on the first floor which contains six rooms. Fake potted 
plants sit outside each door. You can hear muffled noises coming from one on the rooms.
You can go east to go to the first floor stairs or east to go to the second floor stairs.
You can also go an investigate the rooms by going north.""",
	"exits" : {"west" : "Stairs to first floor", "east" : "Stairs to second floor", "north" : "Rooms 1 and 2" },
	"items" : [],
	"locked" : False,
	"npc": []
}

rooms_1_and_2 = {
	"name": "outside rooms one and 2",
	"description" : """
You are standing outside rooms 1 and 2.
You can go west to go to room 1, east to room 2 or south to go back 
to the begining of the hallway. You can also go north to look at rooms 3 and 4. """,
	"exits" : {"west" : "Room 1", "east" : "Room 2", "south" : "Hallway", "north" : "Rooms 3 and 4"},
	"items" : [],
	"locked" : False,
	"npc": []
}

room_1 = {
	"name": "room one",
	"description" : """
You are now standing in a deserted bedroom. Clothes are dtrung everywhere, furniture knocked over. 
Whoever stayed here left in a hurry... """,
	"exits" : {"east" : "Rooms 1 and 2" },
	"items" : [item_pistol, item_second_level_key],
	"locked" : False,
	"npc": []
}

room_2 = {
	"name": "room two",
	"description" : """
You now stand in an empty ensuite bedroom. The bathroom is locked. The room contains little more 
than a bed, nightstand and a chest of drawers. 
You decide to search the room anyway - the occupant may have left something behind.""",
	"exits" : {"west" : "Rooms 1 and 2"},
	"items" : [item_room3_key],
	"locked" : False,
	"npc": []

}

rooms_3_and_4 = {
	"name": "outside rooms three and four",
	"description" : """
You are standing outside rooms 3 and 4.
You can go west to go to room 3, east to room 4 or south to go back 
to rooms 1 and 2. You can also go north to look at rooms 5 and 6. """,
	"exits" : {"west" : "Room 3", "east" : "Room 4", "south" : "Rooms 1 and 2", "north" : "Rooms 5 and 6"},
	"items" : [],
	"locked" : False,
	"npc": []
}

room_3 = {
	"name": "room three",
	"description" : """
You enter this room to find 4 hostages - tied up with rope, their mouths stuffed with towels. 
A men stands guard over them, his gun pointed at them. A keycard hangs from man's belt
You can go east back to the hallway or you can figh the man and save the hostages """,
	"exits" : {"east" : "Rooms 3 and 4"},
	"items" : [item_secret_key],
	"locked" : True,
	"npc": []
}

room_4 = {
	"name": "room four",
	"description" : """
You are now standing in another abandoned bedroom. A first aid kit lies under the bed, inside are some tablets.
You can go east back to the hallway outside or search the room.""",
	"exits" : {"west" : "Rooms 3 and 4"},
	"items" : [item_tablets, item_room5_key],
	"locked" : False,
	"npc": []
}

rooms_5_and_6 = {
	"name": "outside rooms five and six",
	"description" : """
You are standing outside rooms 5 and 6.
You can go west to go to room 5, east to room 6 or south to go back 
to rooms 3 and 4. """,
	"exits" : {"west" : "Room 5", "east" : "Room 6", "south" : "Rooms 3 and 4"},
	"items" : [],
	"locked" : False,
	"npc": []
}

room_5 = {
	"name": "room five",
	"description" : """
You are now standing in one of the final bedrooms on this floor. A maids cart lies abandoned in the room, the towels missing. 
A keycard hangs off a landyard attached to the cart """,
	"exits" : {"east" : "Rooms 5 and 6"},
	"items" : [],
	"locked" : True,
	"npc": []
}

room_6 = {
	"name": "room six",
	"description" : """This room is locked. You cannot get in. """,
	"exits" : {"west" : "Rooms 5 and 6"},
	"items" : [],
	"locked" : True,
	"npc": []
}

stairs_to_second = {
	"name": "the stairs to the second floor",
	"description" : """ 
You are now standing in front of a set of stairs blocked by a door. The only way to access them is to use a keycard.
Go west and use the keycard to get to the next floor or go east to go back to the first floor hallway.""",
	"exits" : {"east" : "Hallway", "west" : "Maze start"},
	"items" : [],
	"locked" : True,
	"npc": []
}

#second floor rooms
maze_start = {
	"name": "the second floor",
	"description" : """
You are now standing on the second floor of the hotel which is under construction. 
Building materials, boxes of equipment and plaster board walls lie ahead, obstructing you view.
You need to find your way through this maze to try and find your target.
You can go east to go back to the second floor stairs or north to enter the maze like structure""",
	"exits" : {"east" : "Stairs to second floor", "north" : "Into the maze"},
	"items" : [],
	"locked" : False,
	"npc": []
}

secret_door = {
	"name": "the secret door",
	"description" : """
In front of you, lies an entrance to a ventilation system which could help you cut through the maze. 
It has what appears to be a keycard scanner.""",
	"exits" : {"north" : "Stairs to the roof"},
	"items" : [],
	"locked" : True,
	"npc": []
}

maze_1 = {
	"name": "Into the maze",
	"description" : """
You have begun to search the maze.
You can go west or west to go into the maze or south to back to the start of the third floor. """,
	"exits" : {"west" : "Further into the maze", "east" : "Deeper into the maze", "south" : "Maze start"},
	"items" : [],
	"locked" : False,
	"npc": []
}

maze_2 = {
	"name": "Further into the maze",
	"description" : """
You have reached a dead end. Debris blocks your path.
Go east to go back. """,
	"exits" : {"east" : "Into the maze"},
	"items" : [],
	"locked" : False,
	"npc": []
}

maze_3 = {
	"name": "Deeper into the maze",
	"description" : """
You are now deeper into the maze.
You can go further in by going north or south, or closer to the beginning by going west.""",
	"exits" : {"north" : "Deeper again", "south" : "Into more maze", "west" : "Into the maze"},
	"items" : [],
	"locked" : False,
	"npc": []
}

maze_4 = {
	"name": "Into more maze",
	"description" : """
You have reached another dead end.
You can go north to go back into the maze. """,
	"exits" : {"north" : "Deeper into the maze"},
	"items" : [],
	"locked" : False,
	"npc": []
}

maze_5 = {
	"name": "Deeper again",
	"description" : """
You have reached a junction, you can only turn west or go back south.""",
	"exits" : {"west" : "Into even more maze", "south" : "Deeper into the maze"},
	"items" : [],
	"locked" : False,
	"npc": []
}

maze_6 = {
	"name": "Into even more maze",
	"description" : """
You have now reached a junction.
You can go north, south or west as well as east to retrace your previous steps.""",
	"exits" : {"north" : "Even deeper into the maze -like floor", "south" : "Even further into this floor", "east" : "Further into the third floor" , "west" : "Deeper again"},
	"items" : [],
	"locked" : False,
	"npc": []
}

maze_7 = {
	"name": "Even further into this floor",
	"description" : """
Again you have reached a dead end.
You can go north to retrace your last steps. """,
	"exits" : {"north" : "Into even more maze"},
	"items" : [],
	"locked" : False,
	"npc": []
}

maze_8 = {
	"name": "Even deeper into the maze -like floor",
	"description" : """
You have reached another junction, you can only go east to go forwards or south to go back.""",
	"exits" : {"south": "Into even more maze", "east" : "Even deeper"},
	"items" : [],
	"locked" : False,
	"npc": []
}

maze_9 = {
	"name": "Even deeper",
	"description" : """
You can see the exit not too far ahead of you. You can go north towards the exit or west to back into the maze. """,
	"exits" : {"north" : "Stairs to the roof", "west" : "Even deeper into the maze -like floor"},
	"items" : [],
	"locked" : False,
	"npc": []
}

maze_10 = {
	"name": "Further into the third floor",
	"description" : """
You arrive at a 4-point cross road.
You can go north, south and west to go further into the maze or east to go back to where you just were.""",
	"exits" : {"north" : "Further in", "south" : "Even further in", "east" : "Into even more maze", "west" : "Even further in"},
	"items" : [],
	"locked" : False,
	"npc": []
}

maze_11 = {
	"name": "Further in",
	"description" : """
A plaster board wall blocks your path. 
You can go south to go back.""",
	"exits" : {"south" : "Further into the third floor"},
	"items" : [],
	"locked" : False,
	"npc": []
}

maze_12 = {
	"name": "Even further in",
	"description" : """
Fallen debris from the ceiling blocks your path.
You can go north to go back into the maze.""",
	"exits" : {"north" : "Further into the third floor"},
	"items" : [],
	"locked" : False,
	"npc": []
}

maze_13 = {
	"name": "Deeper into the maze again",
	"description" : """ 
You have arrived at a T junction.
Going either north or south will take you deeper into the maze, going east will take you back to the last place you were.""",
	"exits" : {"north" : "Even deeper into the third floor", "south" : "More of the maze", "east" : "Further into the third floor"},
	"items" : [],
	"locked" : False,
	"npc": []
}

maze_14 = {
	"name": "Even deeper into the third floor",
	"description" : """
You have reached a dead end. The walls of the building block you from three sides.
You can only go south.""",
	"exits" : {"south" : "Deeper into the maze again"},
	"items" : [],
	"locked" : False,
	"npc": []
}

maze_15 = {
	"name": "More of the maze",
	"description" : """
You have reached a dead end. The walls of the building block all ways except the way you came from.""",
	"exits" : {"north" : "Deeper into the maze again"},
	"items" : [],
	"locked" : False,
	"npc": []
}

stairs_to_roof = {
	"name": "the stairs to the roof",
	"description" : """
To your right lies a door that will take you to the roof, the only other option to where the target is hiding.
Go east to go through the door or go south to go back into the third floor maze.""",
	"exits" : {"east" : "The roof", "south" : "Even deeper"},
	"items" : [],
	"locked" : False,
	"npc": []
}

#the roof
room_roof = {
	"name": "the roof",
	"description" : """
You are now standing on the roof on the hotel. 
One man stands in front of you alone, your target Dr Kirill. He doesn't look happy to see you.
You can confront him or you can go back down to the third floor.""",
	"exits" : {"west" : "Stairs to the roof"},
	"items" : [],
	"locked" : False,
	"npc": []
}

room = {
	"Lobby": room_lobby,
	"Kitchen" : room_kitchen,
	"Bar" : room_bar,
	"Stairs to first floor" : stairs_to_first,
	"Laundry" : room_laundry,
	"Alley" : room_alley,
	"Hallway" : first_floor_hallway,
	"Rooms 1 and 2" : rooms_1_and_2,
	"Room 1" : room_1,
	"Room 2" : room_2,
	"Rooms 3 and 4" : rooms_3_and_4,
	"Room 3" : room_3,
	"Room 4" : room_4,
	"Rooms 5 and 6" : rooms_5_and_6,
	"Room 5" : room_5,
	"Room 6" : room_6,
	"Stairs to second floor" : stairs_to_second,
	"Maze start" : maze_start,
	"Into the maze" : maze_1,
	"Further into the maze" : maze_2,
	"Deeper into the maze" : maze_3,
	"Into more maze" : maze_4,
	"Deeper again" : maze_5,
	"Into even more maze" : maze_6,
	"Even further into this floor" : maze_7,
	"Even deeper into the maze -like floor" : maze_8,
	"Even deeper" : maze_9,
	"Further into the third floor" : maze_10,
	"Further in" : maze_11,
	"Even further in" : maze_12,
	"Deeper into the maze again" : maze_13,
	"Even deeper into the third floor" : maze_14,
	"More of the maze" : maze_15,
	"Secret door" : secret_door,
	"Stairs to the roof" : stairs_to_roof,
	"The roof" : room_roof
}