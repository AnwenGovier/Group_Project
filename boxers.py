import os
from msvcrt import getch
import random

Times = 0
Action = 0
TimesLow = 1
TimesHigh = 10

HeroPlayer = [10, 20, 100, 0.05, 5]

HeroPlayerLowAttack = 10
HeroPlayerHighAttack = 20
HeroPlayerHealth = 100
HeroPlayerCriticalChance = 0.05
HeroPlayerArmor = 5

Level1LowAttack = 5
Level1HighAttack = 10
Level1Health = 50
Level1CriticalChance = 0.01
Level1Armor = 0

Level2LowAttack = 10
Level2HighAttack = 20
Level2Health = 100
Level2CriticalChance = 0.05
Level2Armor = 5

Level3LowAttack = 15
Level3HighAttack = 30
Level3Health = 200
Level3CriticalChance = 0.10
Level3Armor = 7.5

Level4LowAttack = 20
Level4HighAttack = 40
Level4Health = 300
Level4CriticalChance = 0.20
Level4Armor = 10

Level5LowAttack = 30
Level5HighAttack = 50
Level5Health = 500
Level5CriticalChance = 0.30
Level5Armor = 20


HeroPlayerStats = [HeroPlayerLowAttack, HeroPlayerHighAttack, HeroPlayerHealth, HeroPlayerCriticalChance, HeroPlayerArmor]
Level1Stats = [Level1LowAttack, Level1HighAttack, Level1Health, Level1CriticalChance, Level1Armor]
Level2Stats = [Level2LowAttack, Level2HighAttack, Level2Health, Level2CriticalChance, Level2Armor]
Level3Stats = [Level3LowAttack, Level3HighAttack, Level3Health, Level3CriticalChance, Level3Armor]
Level4Stats = [Level4LowAttack, Level4HighAttack, Level4Health, Level4CriticalChance, Level4Armor]
Level5Stats = [Level5LowAttack, Level5HighAttack, Level5Health, Level5CriticalChance, Level5Armor]

HeroPlayerHealth1 = 100
HeroPlayerHealth2 = 150
HeroPlayerHealth3 = 200
HeroPlayerHealth4 = 250

##################################################################################################

def Preparation():
	global Times
	while Times not in range(TimesLow, TimesHigh+1):
		print ("\n\n\n\n\n\n\n\n\n\n\n                   Enter the times you need to prepare (1-10): ")
		Times = input("                                     ")
		while not (Times == ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] and Times.isdigit()):
			os.system("cls")
			print ("Please make sure that you have entered a correct number")
			print ("\n\n\n\n\n\n\n\n\n\n\n                   Enter the times you need to prepare (1-10): ")
			Times = input("                                     ")
		else:
			os.system("cls")

##################################################################################################

print ("\n You are facing a really heavy task!")
print ("\n 5 men with masks are blocking the way to the freedom you need!")
print ("\n You need to beat them down.")
print ("\n But remember! They have different power, so prepare for the worst. . .")
print ("\n With every beaten boxer, it will get harder and harder. . .")
print ("\n Make wise decisions in order to finish them all. . .")

print ("\n\n\n           Press any key to continue with character customization")
getch()
os.system("cls")
Preparation()

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
	print (" \n 1. Train your Attack - Increase Attack by 5-5.")
	print (" 2. Forge your Armor - Increase Armor by 5.")
	print (" 3. Rest - Incerase Health by 30.")
	print (" 4. Pray - Increase the chance of doing double damage by 5%.")
	print (" 5. None - Does nothing.")

#################################################################################################

def Hit (HeroPlayerLowAttack, HeroPlayerHighAttack, HeroPlayerArmor, Armor1):
	Miss = random.randint(0,50)                            
	Critical = random.randint(0,50)
	Attack = random.randint(HeroPlayerLowAttack, HeroPlayerHighAttack)
	Armor1 = HeroPlayerArmor

	global Damage
	if (Miss >= 5):
				   
		if (Critical >= 5):
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

def HitLevel1(Level1LowAttack, Level1HighAttack, Level1Armor, Armor2):
	Miss = random.randint(0,50)                            
	Critical = random.randint(0,50)
	Attack = random.randint(Level1LowAttack, Level1HighAttack)
	Armor2 = Level1Armor
	
	global Damage
	if (Miss >= 5):
					
		if (Critical >= 5):
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
	else:
			print("\n\n Miss!")
			Damage = 0

def HitLevel2(Level2LowAttack, Level2HighAttack, Level2Armor, Armor3):
	Miss = random.randint(0,50)                            
	Critical = random.randint(0,50)
	Attack = random.randint(Level2LowAttack, Level2HighAttack)
	Armor3 = Level2Armor
	
	global Damage
	if (Miss >= 5):
					
		if (Critical >= 5):
			print("\n\n Successful hit!") 
			Damage = Attack - Armor3
				
			if (Damage <= 0):  
				Damage = 0
				print (" Armor has blocked the incoming damage completely!")

		else:                               
			print("\n\n Critical hit!")       
			Damage = 2*Attack - Armor3
				
			if (Damage <= 0):  
				Damage = 0
				print (" Armor has blocked the incoming damage completely!")  
	else:
			print("\n\n Miss!")
			Damage = 0

def HitLevel3(Level3LowAttack, Level3HighAttack, Level3Armor, Armor4):
	Miss = random.randint(0,50)                            
	Critical = random.randint(0,50)
	Attack = random.randint(Level3LowAttack, Level3HighAttack)
	Armor4 = Level3Armor
	
	global Damage
	if (Miss >= 5):
					
		if (Critical >= 5):
			print("\n\n Successful hit!") 
			Damage = Attack - Armor4
				
			if (Damage <= 0):  
				Damage = 0
				print (" Armor has blocked the incoming damage completely!")

		else:                               
			print("\n\n Critical hit!")       
			Damage = 2*Attack - Armor4
				
			if (Damage <= 0):  
				Damage = 0
				print (" Armor has blocked the incoming damage completely!")    
	else:
			print("\n\n Miss!")
			Damage = 0

def HitLevel4(Level4LowAttack, Level4HighAttack, Level4Armor, Armor5):
	Miss = random.randint(0,50)                            
	Critical = random.randint(0,50)
	Attack = random.randint(Level4LowAttack, Level4HighAttack)
	Armor5 = Level4Armor
	
	global Damage
	if (Miss >= 5):
					
		if (Critical >= 5):
			print("\n\n Successful hit!") 
			Damage = Attack - Armor5
				
			if (Damage <= 0):  
				Damage = 0
				print (" Armor has blocked the incoming damage completely!")

		else:                               
			print("\n\n Critical hit!")       
			Damage = 2*Attack - Armor5
				
			if (Damage <= 0):  
				Damage = 0
				print (" Armor has blocked the incoming damage completely!")  
	else:
			print("\n\n Miss!")
			Damage = 0

def HitLevel5(Level5LowAttack, Level5HighAttack, Level5Armor, Armor6):
	Miss = random.randint(0,50)                            
	Critical = random.randint(0,50)
	Attack = random.randint(Level5LowAttack, Level5HighAttack)
	Armor6 = Level5Armor
	
	global Damage
	if (Miss >= 5):
					
		if (Critical >= 5):
			print("\n\n Successful hit!") 
			Damage = Attack - Armor6
				
			if (Damage <= 0):  
				Damage = 0
				print (" Armor has blocked the incoming damage completely!")

		else:                               
			print("\n\n Critical hit!")       
			Damage = 2*Attack - Armor6
				
			if (Damage <= 0):  
				Damage = 0
				print (" Armor has blocked the incoming damage completely!")    
	else:
			print("\n\n Miss!")
			Damage = 0
#########################################################################################

for Time in range(1,Times+1):                                 
	TimesF(Time)                                       
	Action = int(input("\n Enter your action: "))             
	os.system("cls")                                        
	
	if (Action == 1):                                       
		print("\n You've chosen to Train (+5-5 Attack)")
		HeroPlayerLowAttack = HeroPlayerLowAttack + 5
		HeroPlayerHighAttack = HeroPlayerHighAttack + 5

	elif (Action == 2):                                     
		print("\n You've chosen to Forge Armor (+5 Armor)")
		HeroPlayerArmor = HeroPlayerArmor + 5

	elif (Action == 3):                                     
		print("\n You've chosen to Rest (+30 Health)")
		HeroPlayerHealth = HeroPlayerHealth + 30

	elif (Action == 4):
		print("\n You've chosen to Pray (+5% Critical Chance)")
		HeroPlayerCriticalChance = HeroPlayerCriticalChance + HeroPlayerCriticalChance*0.05

	elif (Action == 5):
		print("\n You've chosen to do nothing")

	else:                                                   
		print("\n Please input your choice again.")

##############################################################################################

def EndingLevel1(HeroPlayerHealth):
	global HeroPlayerLowAttack, HeroPlayerHighAttack, HeroPlayerArmor, HeroPlayerHealth1
	if (HeroPlayerHealth <= 0):
		os.system("cls")
		print("\n You have taken a fatal blow!")
		print(" You didn't manage to defeat all the boxers!")
		print(" Game over!")
		print("\n\n\n\n\n Press any key to continue. . . ")
		getch()
		os.system("cls")
		
	else:
		os.system("cls")
		print("\n You are victorious!")
		print(" You are the one who survived the battle with the first boxer!")
		print (" You won the first battle, but you need to survive another four!")
		print (" As an award you receive: +100 Health, 5 Armor and 5-5 Attack")
		HeroPlayerHealth1 = HeroPlayerHealth1 + HeroPlayerHealth
		HeroPlayerLowAttack = HeroPlayerLowAttack + 5
		HeroPlayerHighAttack = HeroPlayerHighAttack + 5
		HeroPlayerArmor = HeroPlayerArmor + 5
		print("\n\n\n\n\n Press any key to continue. . . ")
		getch()
		os.system("cls")
		BattleLevel2()

##################################################################################################

def BattleLevel1():
	global HeroPlayerHealth
	global Level1Health
	while (HeroPlayerHealth > 0 and Level1Health > 0):

		Hit(HeroPlayerLowAttack, HeroPlayerHighAttack, HeroPlayerCriticalChance, Level1Armor)
	
		if (Damage>0):
			Level1Health = Level1Health - Damage
	
		if (Level1Health <= 0):
			Level1Health = 0

		print(" The first boxer has been damaged for ", Damage, " his health is ", '{0:.3g}'.format(Level1Health))
		input("\n__________________________________________________________________\n")

		print ("YOUR STATS: ")
		print ("Health:", '{0:.3g}'.format(HeroPlayerHealth))
		print ("Armor:", HeroPlayerArmor)
		print ("Attack:", HeroPlayerLowAttack, "-", HeroPlayerHighAttack)
		print ("Critical Chance:", '{0:.3g}'.format(HeroPlayerCriticalChance*100), "%" + "\n")

		print ("BOXER'S STATS: ")
		print ("Health:", '{0:.3g}'.format(Level1Health))
		print ("Armor:", Level1Armor)
		print ("Attack:", Level1LowAttack, "-", Level1HighAttack)
		print ("Critical Chance:", '{0:.3g}'.format(Level1CriticalChance*100), "%" + "\n")

		print("\n Press any key to continue. . . ")
		getch()
		os.system("cls")

		if (Level1Health <= 0):
			EndingLevel1(HeroPlayerHealth)
			break
	
		HitLevel1(Level1LowAttack, Level1HighAttack, Level1CriticalChance, HeroPlayerArmor)

		if (Damage>0):
			HeroPlayerHealth = HeroPlayerHealth - Damage

		if (HeroPlayerHealth <= 0): 
			HeroPlayerHealth = 0

		print(" You have been damaged for ", Damage, " your health is ", '{0:.3g}'.format(HeroPlayerHealth))
		input("\n__________________________________________________________________\n")

		print ("YOUR STATS: ")
		print ("Health:", '{0:.3g}'.format(HeroPlayerHealth))
		print ("Armor:", HeroPlayerArmor)
		print ("Attack:", HeroPlayerLowAttack, "-", HeroPlayerHighAttack)
		print ("Critical Chance:", '{0:.3g}'.format(HeroPlayerCriticalChance*100), "%" + "\n")

		print ("BOXER'S STATS: ")
		print ("Health:", '{0:.3g}'.format(Level1Health))
		print ("Armor:", Level1Armor)
		print ("Attack:", Level1LowAttack, "-", Level1HighAttack)
		print ("Critical Chance:", '{0:.3g}'.format(Level1CriticalChance*100), "%" + "\n")

		print("\n Press any key to continue. . . ")
		getch()
		os.system("cls")

		if (HeroPlayerHealth <= 0):
			EndingLevel1(HeroPlayerHealth)
			break

##############################################################################################

def EndingLevel2(HeroPlayerHealth):
	global HeroPlayerLowAttack, HeroPlayerHighAttack, HeroPlayerArmor, HeroPlayerHealth2
	if (HeroPlayerHealth1 <= 0):
		os.system("cls")
		print("\n You have taken a fatal blow!")
		print(" You didn't manage to defeat all the boxers!")
		print(" Game over!")
		print("\n\n\n\n\n Press any key to continue. . . ")
		getch()
		os.system("cls")
		
	else:
		os.system("cls")
		print("\n You are victorious!")
		print(" You are the one who survived the battle with the second boxer!")
		print (" You won the second battle, but you need to survive another three!")
		print (" As an award you receive: +150 Health, 10 Armor and 8-8 Attack")
		HeroPlayerHealth2 = HeroPlayerHealth2 + HeroPlayerHealth1
		HeroPlayerLowAttack = HeroPlayerLowAttack + 8
		HeroPlayerHighAttack = HeroPlayerHighAttack + 8
		HeroPlayerArmor = HeroPlayerArmor + 10
		print("\n\n\n\n\n Press any key to continue. . . ")
		getch()
		os.system("cls")
		BattleLevel3()

##################################################################################################

def BattleLevel2():
	global HeroPlayerHealth1
	global Level2Health
	while (HeroPlayerHealth1 > 0 and Level2Health > 0):

		Hit(HeroPlayerLowAttack, HeroPlayerHighAttack, HeroPlayerCriticalChance, Level2Armor)
	
		if (Damage>0):
			Level2Health = Level2Health - Damage
	
		if (Level2Health <= 0):
			Level2Health = 0

		print(" The second boxer has been damaged for ", Damage, " his health is ", '{0:.3g}'.format(Level2Health))
		input("\n__________________________________________________________________\n")

		print ("YOUR STATS: ")
		print ("Health:", '{0:.3g}'.format(HeroPlayerHealth1))
		print ("Armor:", HeroPlayerArmor)
		print ("Attack:", HeroPlayerLowAttack, "-", HeroPlayerHighAttack)
		print ("Critical Chance:", '{0:.3g}'.format(HeroPlayerCriticalChance*100), "%" + "\n")

		print ("BOXER'S STATS: ")
		print ("Health:", '{0:.3g}'.format(Level2Health))
		print ("Armor:", Level2Armor)
		print ("Attack:", Level2LowAttack, "-", Level2HighAttack)
		print ("Critical Chance:", '{0:.3g}'.format(Level2CriticalChance*100), "%" + "\n")

		print("\n Press any key to continue. . . ")
		getch()
		os.system("cls")

		if (Level2Health <= 0):
			EndingLevel2(HeroPlayerHealth1)
			break
	
		HitLevel2(Level2LowAttack, Level2HighAttack, Level2CriticalChance, HeroPlayerArmor)

		if (Damage>0):
			HeroPlayerHealth1 = HeroPlayerHealth1 - Damage

		if (HeroPlayerHealth1 <= 0): 
			HeroPlayerHealth1 = 0

		print(" You have been damaged for ", Damage, " your health is ", '{0:.3g}'.format(HeroPlayerHealth1))
		input("\n__________________________________________________________________\n")

		print ("YOUR STATS: ")
		print ("Health:", '{0:.3g}'.format(HeroPlayerHealth1))
		print ("Armor:", HeroPlayerArmor)
		print ("Attack:", HeroPlayerLowAttack, "-", HeroPlayerHighAttack)
		print ("Critical Chance:", '{0:.3g}'.format(HeroPlayerCriticalChance*100), "%" + "\n")

		print ("BOXER'S STATS: ")
		print ("Health:", '{0:.3g}'.format(Level2Health))
		print ("Armor:", Level2Armor)
		print ("Attack:", Level2LowAttack, "-", Level2HighAttack)
		print ("Critical Chance:", '{0:.3g}'.format(Level2CriticalChance*100), "%" + "\n")

		print("\n Press any key to continue. . . ")
		getch()
		os.system("cls")

		if (HeroPlayerHealth1 <= 0):
			EndingLevel2(HeroPlayerHealth1)
			break

##############################################################################################

def EndingLevel3(HeroPlayerHealth):
	global HeroPlayerLowAttack, HeroPlayerHighAttack, HeroPlayerArmor, HeroPlayerHealth3
	if (HeroPlayerHealth2 <= 0):
		os.system("cls")
		print("\n You have taken a fatal blow!")
		print(" You didn't manage to defeat all the boxers!")
		print(" Game over!")
		print("\n\n\n\n\n Press any key to continue. . . ")
		getch()
		os.system("cls")
		
	else:
		os.system("cls")
		print("\n You are victorious!")
		print(" You are the one who survived the battle with the third boxer!")
		print (" You won the third battle, but you need to survive another two!")
		print (" As an award you receive: +200 Health, 15 Armor and 10-10 Attack")
		HeroPlayerHealth3 = HeroPlayerHealth3 + HeroPlayerHealth2
		HeroPlayerLowAttack = HeroPlayerLowAttack + 10
		HeroPlayerHighAttack = HeroPlayerHighAttack + 10
		HeroPlayerArmor = HeroPlayerArmor + 15
		print("\n\n\n\n\n Press any key to continue. . . ")
		getch()
		os.system("cls")
		BattleLevel4()

##################################################################################################

def BattleLevel3():
	global HeroPlayerHealth2
	global Level3Health
	while (HeroPlayerHealth2 > 0 and Level3Health > 0):

		Hit(HeroPlayerLowAttack, HeroPlayerHighAttack, HeroPlayerCriticalChance, Level3Armor)
	
		if (Damage>0):
			Level3Health = Level3Health - Damage
	
		if (Level3Health <= 0):
			Level3Health = 0

		print(" The third boxer has been damaged for ", Damage, " his health is ", '{0:.3g}'.format(Level3Health))
		input("\n__________________________________________________________________\n")

		print ("YOUR STATS: ")
		print ("Health:", '{0:.3g}'.format(HeroPlayerHealth2))
		print ("Armor:", HeroPlayerArmor)
		print ("Attack:", HeroPlayerLowAttack, "-", HeroPlayerHighAttack)
		print ("Critical Chance:", '{0:.3g}'.format(HeroPlayerCriticalChance*100), "%" + "\n")

		print ("BOXER'S STATS: ")
		print ("Health:", '{0:.3g}'.format(Level3Health))
		print ("Armor:", Level3Armor)
		print ("Attack:", Level3LowAttack, "-", Level3HighAttack)
		print ("Critical Chance:", '{0:.3g}'.format(Level3CriticalChance*100), "%" + "\n")

		print("\n Press any key to continue. . . ")
		getch()
		os.system("cls")

		if (Level3Health <= 0):
			EndingLevel3(HeroPlayerHealth2)
			break
	
		HitLevel3(Level3LowAttack, Level3HighAttack, Level3CriticalChance, HeroPlayerArmor)

		if (Damage>0):
			HeroPlayerHealth2 = HeroPlayerHealth2 - Damage

		if (HeroPlayerHealth2 <= 0): 
			HeroPlayerHealth2 = 0

		print(" You have been damaged for ", Damage, " your health is ", '{0:.3g}'.format(HeroPlayerHealth2))
		input("\n__________________________________________________________________\n")

		print ("YOUR STATS: ")
		print ("Health:", '{0:.3g}'.format(HeroPlayerHealth2))
		print ("Armor:", HeroPlayerArmor)
		print ("Attack:", HeroPlayerLowAttack, "-", HeroPlayerHighAttack)
		print ("Critical Chance:", '{0:.3g}'.format(HeroPlayerCriticalChance*100), "%" + "\n")

		print ("BOXER'S STATS: ")
		print ("Health:", '{0:.3g}'.format(Level3Health))
		print ("Armor:", Level3Armor)
		print ("Attack:", Level3LowAttack, "-", Level3HighAttack)
		print ("Critical Chance:", '{0:.3g}'.format(Level3CriticalChance*100), "%" + "\n")

		print("\n Press any key to continue. . . ")
		getch()
		os.system("cls")

		if (HeroPlayerHealth2 <= 0):
			EndingLevel3(HeroPlayerHealth2)
			break

##############################################################################################

def EndingLevel4(HeroPlayerHealth):
	global HeroPlayerLowAttack, HeroPlayerHighAttack, HeroPlayerArmor, HeroPlayerHealth4
	if (HeroPlayerHealth3 <= 0):
		os.system("cls")
		print("\n You have taken a fatal blow!")
		print(" You didn't manage to defeat all the boxers!")
		print(" Game over!")
		print("\n\n\n\n\n Press any key to continue. . . ")
		getch()
		os.system("cls")
		
	else:
		os.system("cls")
		print("\n You are victorious!")
		print(" You are the one who survived the battle with the fourth boxer!")
		print (" You won the fourth battle, but you need to survive the last one!")
		print (" As an award you receive: +250 Health, 30 Armor and 20-20 Attack")
		HeroPlayerHealth4 = HeroPlayerHealth4 + HeroPlayerHealth3
		HeroPlayerLowAttack = HeroPlayerLowAttack + 20
		HeroPlayerHighAttack = HeroPlayerHighAttack + 20
		HeroPlayerArmor = HeroPlayerArmor + 30
		print("\n\n\n\n\n Press any key to continue. . . ")
		getch()
		os.system("cls")
		BattleLevel5()

##################################################################################################

def BattleLevel4():
	global HeroPlayerHealth3
	global Level4Health
	while (HeroPlayerHealth3 > 0 and Level4Health > 0):

		Hit(HeroPlayerLowAttack, HeroPlayerHighAttack, HeroPlayerCriticalChance, Level4Armor)
	
		if (Damage>0):
			Level4Health = Level4Health - Damage
	
		if (Level4Health <= 0):
			Level4Health = 0
		
		print(" The fourth boxer has been damaged for ", Damage, " his health is ", '{0:.3g}'.format(Level4Health))
		input("\n__________________________________________________________________\n")

		print ("YOUR STATS: ")
		print ("Health:", '{0:.3g}'.format(HeroPlayerHealth3))
		print ("Armor:", HeroPlayerArmor)
		print ("Attack:", HeroPlayerLowAttack, "-", HeroPlayerHighAttack)
		print ("Critical Chance:", '{0:.3g}'.format(HeroPlayerCriticalChance*100), "%" + "\n")

		print ("BOXER'S STATS: ")
		print ("Health:", '{0:.3g}'.format(Level4Health))
		print ("Armor:", Level4Armor)
		print ("Attack:", Level4LowAttack, "-", Level4HighAttack)
		print ("Critical Chance:", '{0:.3g}'.format(Level4CriticalChance*100), "%" + "\n")

		print("\n Press any key to continue. . . ")
		getch()
		os.system("cls")

		if (Level4Health <= 0):
			EndingLevel4(HeroPlayerHealth3)
			break
	
		HitLevel4(Level4LowAttack, Level4HighAttack, Level4CriticalChance, HeroPlayerArmor)

		if (Damage>0):
			HeroPlayerHealth3 = HeroPlayerHealth3 - Damage

		if (HeroPlayerHealth3 <= 0): 
			HeroPlayerHealth3 = 0

		print(" You have been damaged for ", Damage, " your health is ", '{0:.3g}'.format(HeroPlayerHealth3))
		input("\n__________________________________________________________________\n")

		print ("YOUR STATS: ")
		print ("Health:", '{0:.3g}'.format(HeroPlayerHealth3))
		print ("Armor:", HeroPlayerArmor)
		print ("Attack:", HeroPlayerLowAttack, "-", HeroPlayerHighAttack)
		print ("Critical Chance:", '{0:.3g}'.format(HeroPlayerCriticalChance*100), "%" + "\n")

		print ("BOXER'S STATS: ")
		print ("Health:", '{0:.3g}'.format(Level4Health))
		print ("Armor:", Level4Armor)
		print ("Attack:", Level4LowAttack, "-", Level4HighAttack)
		print ("Critical Chance:", '{0:.3g}'.format(Level4CriticalChance*100), "%" + "\n")

		print("\n Press any key to continue. . . ")
		getch()
		os.system("cls")

		if (HeroPlayerHealth3 <= 0):
			EndingLevel4(HeroPlayerHealth3)
			break

##############################################################################################

def EndingLevel5(HeroPlayerHealth):
	global HeroPlayerLowAttack, HeroPlayerHighAttack, HeroPlayerArmor
	if (HeroPlayerHealth4 <= 0):
		os.system("cls")
		print("\n You have taken a fatal blow!")
		print(" You didn't manage to defeat all the boxers!")
		print(" Game over!")
		print("\n\n\n\n\n Press any key to continue. . . ")
		getch()
		os.system("cls")

	else:
		os.system("cls")
		print("\n You are victorious!")
		print(" You are the one who survived the battle with the fifth boxer!")
		print (" You won the last battle!")
		print (" Congratulations!")
		print("\n\n\n\n\n Press any key to continue. . . ")
		getch()
		os.system("cls")

##################################################################################################

def BattleLevel5():
	global HeroPlayerHealth4
	global Level5Health
	while (HeroPlayerHealth4 > 0 and Level5Health > 0):

		Hit(HeroPlayerLowAttack, HeroPlayerHighAttack, HeroPlayerCriticalChance, Level5Armor)
	
		if (Damage>0):
			Level5Health = Level5Health - Damage
	
		if (Level5Health <= 0):
			Level5Health = 0

		print(" The fifth boxer has been damaged for ", Damage, " his health is ", '{0:.3g}'.format(Level5Health))
		input("\n__________________________________________________________________")

		print ("YOUR STATS: ")
		print ("Health:", '{0:.3g}'.format(HeroPlayerHealth4))
		print ("Armor:", HeroPlayerArmor)
		print ("Attack:", HeroPlayerLowAttack, "-", HeroPlayerHighAttack)
		print ("Critical Chance:", '{0:.3g}'.format(HeroPlayerCriticalChance*100), "%" + "\n")

		print ("BOXER'S STATS: ")
		print ("Health:", '{0:.3g}'.format(Level5Health))
		print ("Armor:", Level5Armor)
		print ("Attack:", Level5LowAttack, "-", Level5HighAttack)
		print ("Critical Chance:", '{0:.3g}'.format(Level5CriticalChance*100), "%" + "\n")

		print("\n Press any key to continue. . . ")
		getch()
		os.system("cls")

		if (Level5Health <= 0):
			EndingLevel5(HeroPlayerHealth4)
			break
	
		HitLevel5(Level5LowAttack, Level5HighAttack, Level5CriticalChance, HeroPlayerArmor)

		if (Damage>0):
			HeroPlayerHealth4 = HeroPlayerHealth4 - Damage

		if (HeroPlayerHealth4 <= 0): 
			HeroPlayerHealth4 = 0
		
		print(" You have been damaged for ", Damage, " your health is ", '{0:.3g}'.format(HeroPlayerHealth4))
		input("\n__________________________________________________________________")

		print ("YOUR STATS: ")
		print ("Health:", '{0:.3g}'.format(HeroPlayerHealth4))
		print ("Armor:", HeroPlayerArmor)
		print ("Attack:", HeroPlayerLowAttack, "-", HeroPlayerHighAttack)
		print ("Critical Chance:", '{0:.3g}'.format(HeroPlayerCriticalChance*100), "%" + "\n")

		print ("BOXER'S STATS: ")
		print ("Health:", '{0:.3g}'.format(Level5Health))
		print ("Armor:", Level5Armor)
		print ("Attack:", Level5LowAttack, "-", Level5HighAttack)
		print ("Critical Chance:", '{0:.3g}'.format(Level5CriticalChance*100), "%" + "\n")

		print("\n Press any key to continue. . . ")
		getch()
		os.system("cls")

		if (HeroPlayerHealth4 <= 0):
			EndingLevel5(HeroPlayerHealth4)
			break

BattleLevel1()
