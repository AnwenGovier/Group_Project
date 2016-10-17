import os
from msvcrt import getch
import random

Times = 0
Action = 0
TimesLow = 1
TimesHigh = 10

HeroPlayer = [5, 15, 100, 0.05, 5]

HeroPlayerLowAttack = 5
HeroPlayerHighAttack = 15
HeroPlayerHealth = 100
HeroPlayerCriticalChance = 0.05
HeroPlayerArmor = 5

MonsterRichardLowAttack = 10
MonsterRichardHighAttack = 15
MonsterRichardHealth = 120
MonsterRichardCriticalChance = 0.20
MonsterRichardArmor = 10

HeroPlayerStats = [HeroPlayerLowAttack, HeroPlayerHighAttack, HeroPlayerHealth, HeroPlayerCriticalChance, HeroPlayerArmor]
MonsterRichardStats = [MonsterRichardLowAttack, MonsterRichardHighAttack, MonsterRichardHealth, MonsterRichardCriticalChance, MonsterRichardArmor]

##################################################################################################

print ("\n\n You have faced Richard and you must defeat him!")
print ("\n\n But you need some time to prepare for the battle in order to win!")
print ("\n So far. . . you are. . .")
print ("    averagely built character that has the decent base health - 100")
print ("    and armor - 5, does physical damage, 5.0% critical chance,")
print ("    attacks are affected by armor")
print ("\n Take wise decisions, because Richard is way more powerful than you think!")

print ("\n\n\n           Press any key to continue with character customization")
getch()
os.system("cls")

##################################################################################################

while Times not in range(TimesLow, TimesHigh+1):
	print ("\n\n\n\n\n\n\n\n\n\n\n                   Enter the times you need to prepare (5-10): ")
	#need loop that asks for valid integer value
	Times = int(input("                                     "))
	os.system("cls")

##################################################################################################

HeroPlayerLowAttack = HeroPlayerStats[0]
HeroPlayerHighAttack = HeroPlayerStats[1]
HeroPlayerHealth = HeroPlayerStats[2]
HeroPlayerCriticalChance = HeroPlayerStats[3]
HeroPlayerArmor = HeroPlayerStats[4]

##################################################################################################

def TimesF(Time):
	print ("STATS: ")
	print (" Health:", HeroPlayerHealth)
	print (" Armor:", HeroPlayerArmor)
	print (" Attack:", HeroPlayerLowAttack, "-", HeroPlayerHighAttack)
	print (" Critical Chance:", '{0:.3g}'.format(HeroPlayerCriticalChance*100), "%")
	
	print (" \n You can prepare " + str(Times) + " times.")
	print (" \n Choice your task: ")
	print (" \n 1. Train your Attack - Increase Attack by 2-2.")
	print (" 2. Forge your Armor - Increase Armor by 2.")
	print (" 3. Rest - Incerase Health by 15.")
	print (" 4. Pray - Increase the chance of doing double damage by 5%.")
	print (" 5. None - Does nothing.")

#################################################################################################

def Hit (HeroPlayerLowAttack, HeroPlayerHighAttack, HeroPlayerArmor, Armor1):
	Miss = random.randint(0,101)                            
	Critical = random.randint(0,101)
	Attack = random.randint(HeroPlayerLowAttack, HeroPlayerHighAttack)
	Armor1 = HeroPlayerArmor

	global Damage
	if (Miss >= 10):
				   
		if (Critical >= 10):
			print("\n\n Successful hit!") 
			Damage = Attack - Armor1

			if (Damage <= 0):  
				Damage = 0
				print (" Armor has blocked the incoming damage completely!")
		else:                               
			print("\n\n Critical hit!")                       
			Damage = 2*Attack - Armor1
				
			if (Damage <= 0): 
					Damage = 0
					print (" Armor has blocked the incoming damage completely!")
		
	else:
			print("\n\n Miss!")
			Damage = 0

def HitMonster(HeroPlayerLowAttack, MonsterRichardHighAttack, MonsterRichardArmor, Armor2):
	Miss = random.randint(0,101)                            
	Critical = random.randint(0,101)
	Attack = random.randint(MonsterRichardLowAttack, MonsterRichardHighAttack)
	Armor2 = MonsterRichardArmor
	
	global Damage
	if (Miss >= 10):
					
		if (Critical >= 10):
			print("\n\n Successful hit!") 
			Damage = Attack - Armor2
				
			if (Damage <= 0):  
				Damage = 0
				print (" Armor has blocked the incoming damage completely!")

		else:                               
			print("\n\n Critical hit!")       
			Damage = 2*Attack - Armor2
				
			if (Damage <= 0):  
				Damage = 0
				print (" Armor has blocked the incoming damage completely!")
		#----------------------------------------------------------------------------#    
	else:
			print("\n\n Miss!")
			Damage = 0

#########################################################################################

for Time in range(1,Times+1):                                 
	TimesF(Time)                                       
	Action = int(input("\n Enter your action: "))             
	os.system("cls")                                        
	
	if (Action == 1):                                       
		print("\n You've chosen to Train (+2-2 Attack)")
		HeroPlayerLowAttack = HeroPlayerLowAttack + 2
		HeroPlayerHighAttack = HeroPlayerHighAttack + 2

	elif (Action == 2):                                     
		print("\n You've chosen to Forge Armor (+2 Armor)")
		HeroPlayerArmor = HeroPlayerArmor + 2

	elif (Action == 3):                                     
		print("\n You've chosen to Rest (+15 Health)")
		HeroPlayerHealth = HeroPlayerHealth + 15

	elif (Action == 4):
		print("\n You've chosen to Pray (+5% Critical Chance)")
		HeroPlayerCriticalChance = HeroPlayerCriticalChance + HeroPlayerCriticalChance*0.05

	elif (Action == 5):
		print("\n You've chosen to do nothing")

	else:                                                   
		print("\n Please input your choice again.")

##############################################################################################

def Ending(HeroPlayerHealth):
	if (HeroPlayerHealth <= 0):
		os.system("cls")
		print("\n You have taken a fatal blow!")
		print(" You didn't manage to defeat Richard")
		print(" Game over!")
		print("\n\n\n\n\n Press any key to continue. . . ")
		getch()
		os.system("cls")
		while True:
			print ("Do you want to play again? (Y/N)")
			user_input = input().lower() 
			if user_input == "y":
				os.system("game.py")
			elif user_input == "n":
				exit()
			else: 
				os.system("cls")
				return False
		
	else:
		os.system("cls")
		print("\n You are victorious!")
		print(" You are the one who survived the battle with Richard")
		print (" Congratulations!!! You won the game!!!")
		print("\n\n\n\n\n Press any key to continue. . . ")
		getch()
		os.system("cls")

##################################################################################################

while (HeroPlayerHealth > 0 and MonsterRichardHealth > 0):

	Hit(HeroPlayerLowAttack, HeroPlayerHighAttack, HeroPlayerCriticalChance, MonsterRichardArmor)
	
	if (Damage>0):
		MonsterRichardHealth = MonsterRichardHealth - Damage
	
	if (MonsterRichardHealth <= 0):
		MonsterRichardHealth = 0
		
	print(" Richard has been damaged for ", Damage, " his health is ", MonsterRichardHealth)
	input("\n__________________________________________________________________")

	if (MonsterRichardHealth <= 0):
		Ending(HeroPlayerHealth)
		break
	
	
	HitMonster(MonsterRichardLowAttack, MonsterRichardHighAttack, MonsterRichardCriticalChance, HeroPlayerArmor)

	if (Damage>0):
		HeroPlayerHealth = HeroPlayerHealth - Damage

	if (HeroPlayerHealth <= 0): 
		HeroPlayerHealth = 0
		
	print(" You have been damaged for ", Damage, " your health is ", HeroPlayerHealth)
	input("\n__________________________________________________________________")

	if (HeroPlayerHealth <= 0):
		Ending(HeroPlayerHealth)

		break