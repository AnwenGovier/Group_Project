#kirril, 2 bad guys, bar man, hostages
#id, name, description, item, dialogue, can_attack, player state


npc_enemy_2nd_floor = {
	"id": "2nd floor enemy",

	"name": "Richard",

	"description": 
	"""
	Richard, despite his seemingly higher rank within the organisation, 
	is rather dimwitted and only achieved his rank due to dubious family connections to the establishment
	""",

	"dialogue": 
	"""Code me some dialogue please""",

	"can_attack": True,

	"npc_state": {"health": 100, "damage": 15, "alive": True}
}

npc_enemy_1st_floor = {
	"id": "1st floor enemy",

	"name": "Bernard",

	"description":
	"""Bernard is a common or garden lackey, capable of getting in the way and looking menacing but not much more""",

	"dialogue": 
	"""ADD""",

	"can_attack": True,

	"npc_state": {"health": 100, "damage": 10, "alive": True}
}

npc_bar_man = {
	"id": "bar tender",

	"name": "Larry",

	"description":
	"""
	Larry the bar tender is a student with an evening job, 
	and always eager to assist a patron of the bar in getting as drunk as possible
	""",

	"dialogue":
	""" ADD """,

	"can_attack": False,

	"npc_state": {}
}

npc_hostage = {
	"id": "hostage",

	"name": "Gregg", 

	"desciption": 
	"""
	Gregg isnt really sure whats happening, he was asleep in his hotel room and (not usually for him) 
	woke up bound and gagged, although he thinks there might be something different about it this time...
	""",

	"dialogue":
	""" ADD """,

	"can_attack": False,

	"npc_state": {}

}
