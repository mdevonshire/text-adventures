print "Welcome to this text adventure"
print "RULES / ADVICE"
print "1. Answer everything in capitals"
print "2. Answer with one word answers only"
print "-------------------------------------"
score = 0
#---------------------------------------
#This next bit is setting the inventory.
def game_setup():
	global Shield
	global Sword
	global Armour
	global Bow
	global Arrows
	global Shurikens
	global Fork
	global Knife
	global Dagger
	global Coin
	global Stealth
	Sword = False
	Shield = False
	Bow = False
	Knife = False
	Fork = True
	Coin = False
	Arrows = 0
	Shurikens = 0
	Dagger = 0
	Armour = 0
	Stealth = False
	name_of_character()
#----------------------------------------
def name_of_character():
	print "What is your name?"
	global name
	name = raw_input()
	print "So your name is %s? YES or NO" % (name)
	name_yesno = raw_input()
	if name_yesno == "YES":
		print "Welcome %s, adventure awaits you." % (name)
		pick_class()
	elif name_yesno == "NO":
		name_of_character()
	else: 
		print "Invalid Response" 
		name_of_character()
# Name
#-----------------------------------------
def pick_class():
	print "Which class are you?"
	print "KNIGHT, ARCHER or NINJA"
	class_ = raw_input()
	if class_ == "KNIGHT":
		global Shield
		Shield = True
		global Sword
		Sword = True
		global Armour
		Armour = 5
		print "You have chosen to be a knight."
		print "You have been eqipped with a SWORD, SHIELD and ARMOUR."
		print "Remember these items, you will need them."
		shop()
	elif class_ == "ARCHER":
		global Bow
		Bow = True
		global Arrows
		Arrows = 5
		global Knife
		Knife = True
		print "You have chosen to be an archer."
		print "You have been eqipped with a BOW, KNIFE and 5 Arrows."
		print "Remember these items, you will need them."
		shop()
	elif class_ == "NINJA":
		global Dagger
		Dagger = 1
		global Shurikens
		Shurikens = 5
		global Stealth
		Stealth = True
		print "You have chosen to be a ninja."
		print "You have been eqipped with a DAGGER and 5 SHURIKENs."
		print "You have also recieved the ability of stealth"
		print "Remember these items, you will need them."
		shop()
# More classes can be added here with elif
	else: 
		print "Invalid Response"
		pick_class()
#Picking of class
#-----------------------------------
def shop():
	print "-----------------------------"
	print "You arrived at the shop"
	print "You have enough money to buy one item at the shop"
	print "'Hello %s', says the shopkeeper." % (name)
	shop2()
def shop2():
	print " 'Would you like to buy a SHURIKEN, a DAGGER or ARMOUR?'"
	extra_item = raw_input()
	if extra_item == "SHURIKEN":
		global Shurikens
		Shurikens = Shurikens + 1
		print "You now have %s SHURIKEN" % (Shurikens)
		print "---------------------------------------"
		rumour()
	elif extra_item == "DAGGER":
		global Dagger
		Dagger = Dagger + 1
		print "You now have %s DAGGER" % (Dagger)
		print "---------------------------------------"
		rumour()
	elif extra_item == "ARMOUR":
		global Armour
		if Armour > 0:
			print "Because you already have armour on, you had to leave the new armour at the shop."
			print "That was not a smart move %s." % (name)
			rumour()
		else:
			Armour = 5
			print "You are now equipped with ARMOUR"
			rumour()
	else:
		print "Invalid Response"
		shop2()
#Picking extra item
#-----------------------------------
def rumour():
	print "On the way out of the shop," 
	print "you hear someone talking about a great tresure hidden in a large cave system."
	print "You know where this cave is. "
	global no_count
	no_count = 0
	rumour2() 
def rumour2():
	global Final_Objective
	global no_count
	print "Do you want to look for the treasure?"
	print "YES or NO"
	look_confirm = raw_input()
	if look_confirm == "NO":
		no_count = no_count + 1
		if no_count > 1:
			print "Fine then!"
			print "What about you search the cave system for a small terrorist that goes by the name of monkey?"
			print "YES or NO"
			look_confirm_2 = raw_input()
			if look_confirm_2 == "NO":
				print "You are so boring %s" % (name)
				no_count = 0
				rumour2()
			elif look_confirm_2 == "YES":
				Final_Objective = "MONKEY"
				print "You head off to the cave."
				print "----------------------------------------------"
				cave_room_1()
			else:
				print "Invalid Response"
				rumour2()
		else:
			print "C'mon %s, you're such a coward" % (name)
			rumour2()
	elif look_confirm == "YES":
		Final_Objective = "TREASURE"
		print "You head off to the cave."
		print "------------------------------------------------"
		cave_room_1()
	else:
		print "Invalid Response"
		rumour2()
#The rumour.
#--------------------------------------
def cave_room_1():
	print "You take a hike to where the cave is."
	print "Once you enter the cave you see a troll gaurding the way."
	cave_room_1b()
def cave_room_1b():
	global Shield
	global Sword
	global Armour
	global Bow
	global Arrows
	global Shurikens
	global Fork
	global Knife
	global Dagger
	global Coin
	global Stealth
	print "Do you ATTACK the troll with a ranged weapon or WALK closer?"
	option_1 = raw_input()
	if option_1 == "ATTACK":
		if Arrows or Shurikens or Dagger > 0:
			cave_room_1c()
		else:
			print "You do not have a ranged weapon"
			cave_room_1b()
	elif option_1 == "WALK":
		print "You walk closer"
		cave_room_1d()
	else:
		print "Invalid Response"
		cave_room_1b()
def cave_room_1c():
	global Shield
	global Sword
	global Armour
	global Bow
	global Arrows
	global Shurikens
	global Fork
	global Knife
	global Dagger
	global Coin
	global Stealth
	print "What will you attack with?"
	option_1b = raw_input()
	if option_1b == "BOW":
		if Bow == True and Arrows > 0:
			print "You let an arrow fly straight into the eye of the troll."
			print "It hits the ground with a 'thump!'"
			print "On the way past you retrive your arrow"
			print "You now have %s arrows." % (Arrows)
			cave_room_1z()
		elif Bow == True and Arrows < 1:
			print "You do not have any arrows"
			cave_room_1c()
		else:
			print "You do not have a bow"
			cave_room_1c()
	elif option_1b == "DAGGER":
		if Dagger > 0:
			if Armour == 0:
				print "You throw the dagger and it hits the troll right in the heart."
				print "On the way past you retrive your dagger."
				print "You now have %s dagger" % (Dagger)
				cave_room_1z()
			else:
				Dagger = Dagger - 1
				print "Your heavy armour causes your throw to fall short."
				print "The dagger hits the ground and awakes the troll, aleting it of your presence."
				print "The troll picks up the dagger and slams into the ground in rage."
				cave_room_1e()
		else:
			print "You do not have a dagger"
			cave_room_1c()
	elif option_1b == "SHURIKEN":
		if Shurikens > 0:
			if Armour == 0:
				print "You throw the shuriken and it hits the troll right in the heart."
				print "On the way past you retrive your shuriken."
				print "You now have %s shurikens" % (Shurikens)
				cave_room_1z()
			else:
				Shurikens = Shurikens - 1
				print "Your heavy armour causes your throw to fall short."
				print "The shuriken hits the ground and bounces off into darkness."
				print "This awakes the troll, aleting it of your presence."
				cave_room_1e()
	else:
		print "Invalid Response"
		cave_room_1c()
def cave_room_1d():
	global Shield
	global Sword
	global Armour
	global Bow
	global Arrows
	global Shurikens
	global Fork
	global Knife
	global Dagger
	global Coin
	global Stealth
	print "You decided to walk"
	if Stealth != True:
		print "You accidentally kick a stone, awaking and alerting the troll of you presence."
		cave_room_1e()
	else:
		cave_room_1d2()
def cave_room_1d2():
		print "You are now close enough to strike the troll with your dagger"
		print "Or you could try to sneak past the sleeping troll"
		cave_room_1d3()
def cave_room_1d3():
	global Shield
	global Sword
	global Armour
	global Bow
	global Arrows
	global Shurikens
	global Fork
	global Knife
	global Dagger
	global Coin
	global Stealth
	print "SNEAK or DAGGER"
	option_1d = raw_input()
	if option_1d == "DAGGER":
		if Dagger > 0:
			print "As you lunge, the troll smells you, wakes up, and bites your head off"
			game_over()
		else:
			print "You do not have a dagger"
			cave_room_1d3()
	elif option_1d == "SNEAK":
		print "You sneak past and into the next chamber"
		print "-------------------------------------------"
		a2_cave_room
	else:
		print "Invalid Response"
		cave_room_1d3()
def cave_room_1e():
	print "The troll lunges at you with both fists"
	global blockcount1a
	blockcount1a = 0
	cave_room_1f()
def cave_room_1f():
	global Shield
	global Sword
	global Armour
	global Bow
	global Arrows
	global Shurikens
	global Fork
	global Knife
	global Dagger
	global Coin
	global Stealth
	print "What do you counter it with?"
	a1counter = raw_input()
	if a1counter == "BOW":
		if Bow == True:
			print "You cannot use this bow at close quarters"
			cave_room_1f()
		else:
			print "You do not have a bow"
			cave_room_1f()
	elif a1counter == "SHIELD":
		global blockcount1a
		if blockcount1a == 0:
			blockcount1a = blockcount1a + 1
			print "You block the hits but the troll attacks again, aiming to puch you in the chest"
			cave_room_1f()
		else:
			print "You block the hit but the troll attacks again with both fists"
			blockcount1a = 0
			cave_room_1f()
	elif a1counter == "SWORD":
		if Sword == True:
			print "You sidestep the clumsy troll and swing your sword at its neck. You cut the trolls head clean off and it rolls away into the darkness. You clean your sword on the troll's tunic before you advance."
			cave_room_1z()
		else:
			print "You do not have a sword"
			cave_room_1f()
	elif a1counter == "SHURIKEN":
		if Shurikens < 1:
			print "You do not have a shuriken"
			cave_room_1f()
		else:
			print "You cannot use this weapon at close range"
			cave_room_1f()
	elif a1counter == "KNIFE":
		if Knife == True:
			print "You dodge the troll's feeble attack and watch it stumble forward. You then jump on its back and slit its throat."
			cave_room_1z()
		else:
			print "You do not have a knife"
			cave_room_1f()
	elif a1counter == "DAGGER":
		if Dagger > 0:
			if Armour > 0:
				print "You stab the troll in the heart, but not before it hits you with its fists. Lucky you had armour on."
				Armour = Armour - 1
				print "Your armour is now at %s/5 health" % (Armour)
				cave_room_1z()
			else:
				print "You stab the troll in the heart, but not before it hits you with its fist. Its fist crush your ribs, puncturing your lungs."
				raw_input("Press Enter to continue")
				print "You then lie in a pool of blood until you die"
				raw_input("Press Enter to contine")
				game_over()
		else:
			print "You don't have a dagger"
			cave_room_1f()
	else:
		print "Invalid Response"
		cave_room_1f()
def cave_room_1z():
	global score
	score = score + 1
	print "You walk to the next chamber"
	print "--------------------------------"
	a2_cave_room()
#Cave 1 : TROLL
#--------------------------------------------------------------------------------------
def a2_cave_room():
	global killed_rats
	#global
	#global
	killed_rats = 0
	arrows_in_rats = 0
	shurikens_in_rats = 0
	print "You peer into the murky darkeness and see three giant rats near a large crevice. They haven't seen you yet."
	b2_cave_room()
def a2b_cave_room():
	print "The other two rats have not seen you yet"
	b2_cave_room
def a2c_cave_room():
	print "The last rat still has not seen you."
	b2_cave_room()
def b2_cave_room():
	global Shield
	global Sword
	global Armour
	global Bow
	global Arrows
	global Shurikens
	global Fork
	global Knife
	global Dagger
	global Coin
	global Stealth
	print "Do you ATTACK a rat with a ranged weapon or WALK closer?"
	option_1 = raw_input()
	if option_1 == "ATTACK":
		if Arrows or Shurikens or Dagger > 0:
			c2_cave_room()
		else:
			print "You do not have a ranged weapon"
			b2_cave_room()
	elif option_1 == "WALK":
		print "You walk closer"
		d2_cave_room()
	else:
		print "Invalid Response"
		b2_cave_room()
def c2_cave_room():
	global Shield
	global Sword
	global Armour
	global Bow
	global Arrows
	global Shurikens
	global Fork
	global Knife
	global Dagger
	global Coin
	global Stealth
	global killed_rats
	global arrows_in_rats
	global shurikens_in_rats
	global daggers_in_rats
	print "What will you attack with?"
	option_1b = raw_input()
	if option_1b == "BOW":
		if Bow == True and Arrows > 0:
			if killed_rats == 0:
				print "You hit the first rat in the side and it falls into the crevice."
				Arrows = Arrows - 1
				print "You now have %s arrows." % (Arrows)
				killed_rats = killed_rats + 1
				arrows_in_rats = arrows_in_rats + 1
				a2b_cave_room()
			elif killed_rats == 1:
				print "You hit the second rat in the head and it rolls into the crevice."
				Arrows = Arrows - 1
				print "You now have %s arrows." % (Arrows)
				killed_rats = killed_rats + 1
				arrows_in_rats = arrows_in_rats + 1
				a2c_cave_room()
			elif killed_rats == 2:
				print "You hit the last rat in the side and it falls into the crevice."
				Arrows = Arrows - 1
				print "You now have %s arrows." % (Arrows)
				killed_rats = killed_rats + 1
				arrows_in_rats = arrows_in_rats + 1
				z2_cave_room()
			else:
				print "ERROR"
		elif Bow == True and Arrows < 1:
			print "You do not have any arrows"
			cave_room()
		else:
			print "You do not have a bow"
			c2_cave_room()
	elif option_1b == "DAGGER":
		if Dagger > 0:
			if killed_rats == 0:
				print "You hit the first rat in the side and it falls into the crevice."
				Dagger = Dagger - 1
				print "You now have %s dagger." % (Dagger)
				killed_rats = killed_rats + 1
				daggers_in_rats = daggers_in_rats + 1
				a2b_cave_room()
			elif killed_rats == 1:
				print "You hit the second rat in the head and it rolls into the crevice."
				Dagger = Dagger - 1
				print "You now have %s dagger." % (Dagger)
				killed_rats = killed_rats + 1
				daggers_in_rats = daggers_in_rats + 1
				a2c_cave_room()
			elif killed_rats == 2:
				print "You hit the last rat in the side and it falls into the crevice."
				Dagger = Dagger - 1
				print "You now have %s dagger." % (Dagger)
				killed_rats = killed_rats + 1
				daggers_in_rats = daggers_in_rats + 1
				z2_cave_room()
			else:
				print "ERROR"
		else:
			print "You do not have a dagger"
			c2_cave_room()
	elif option_1b == "SHURIKEN":
		if Shurikens > 0:
			if killed_rats == 0:
				print "You hit the first rat in the side and it falls into the crevice."
				Shurikens = Shurikens - 1
				print "You now have %s shurikens." % (Shurikens)
				killed_rats = killed_rats + 1
				shurikens_in_rats = shurikens_in_rats + 1
				a2b_cave_room()
			elif killed_rats == 1:
				print "You hit the second rat in the head and it rolls into the crevice."
				Shurikens = Shurikens - 1
				print "You now have %s shurikens." % (Shurikens)
				killed_rats = killed_rats + 1
				shurikens_in_rats = shurikens_in_rats + 1
				a2c_cave_room()
			elif killed_rats == 2:
				print "You hit the last rat in the pupil of the eyeball and it falls into the crevice."
				Shurikens = Shurikens - 1
				print "You now have %s shurikens." % (Shurikens)
				killed_rats = killed_rats + 1
				shurikens_in_rats = shurikens_in_rats + 1
				z2_cave_room()
			else:
				print "ERROR"
	else:
		print "Invalid Response"
		c2_cave_room()
def d2_cave_room():
	print "You can now ATTACK the rats or you can try to SNEAK past."
	ak_sk = raw_input()
def cave_room_1e():
	print "The troll lunges at you with both fists"
	global blockcount1a
	blockcount1a = 0
	cave_room_1f()
def cave_room_1f():
	global Shield
	global Sword
	global Armour
	global Bow
	global Arrows
	global Shurikens
	global Fork
	global Knife
	global Dagger
	global Coin
	global Stealth
	print "What do you counter it with?"
	a1counter = raw_input()
	if a1counter == "BOW":
		if Bow == True:
			print "You cannot use this bow at close quarters"
			cave_room_1f()
		else:
			print "You do not have a bow"
			cave_room_1f()
	elif a1counter == "SHIELD":
		global blockcount1a
		if blockcount1a == 0:
			blockcount1a = blockcount1a + 1
			print "You block the hits but the troll attacks again, aiming to puch you in the chest"
			cave_room_1f()
		else:
			print "You block the hit but the troll attacks again with both fists"
			blockcount1a = 0
			cave_room_1f()
	elif a1counter == "SWORD":
		if Sword == True:
			print "You sidestep the clumsy troll and swing your sword at its neck. You cut the trolls head clean off and it rolls away into the darkness. You clean your sword on the troll's tunic before you advance."
			cave_room_1z()
		else:
			print "You do not have a sword"
			cave_room_1f()
	elif a1counter == "SHURIKEN":
		if Shurikens < 1:
			print "You do not have a shuriken"
			cave_room_1f()
		else:
			print "You cannot use this weapon at close range"
			cave_room_1f()
	elif a1counter == "KNIFE":
		if Knife == True:
			print "You dodge the troll's feeble attack and watch it stumble forward. You then jump on its back and slit its throat."
			cave_room_1z()
		else:
			print "You do not have a knife"
			cave_room_1f()
	elif a1counter == "DAGGER":
		if Dagger > 0:
			if Armour > 0:
				print "You stab the troll in the heart, but not before it hits you with its fists. Lucky you had armour on."
				Armour = Armour - 1
				print "Your armour is now at %s/5 health" % (Armour)
				cave_room_1z()
			else:
				print "You stab the troll in the heart, but not before it hits you with its fist. Its fist crush your ribs, puncturing your lungs."
				raw_input("Press Enter to continue")
				print "You then lie in a pool of blood until you die"
				raw_input("Press Enter to contine")
				game_over()
		else:
			print "You don't have a dagger"
			cave_room_1f()
	else:
		print "Invalid Response"
		cave_room_1f()
def z2_cave_room():
	global score
	score = score + 1
	print "You walk to the next chamber"
	print "--------------------------------"
	a3_cave_room()

#Cave 2 : RATS
#--------------------------------------------------------------------------
def a3_cave_room():
	print "cave 3"

def game_over():
	global score
	score = score - 1
	print "      .... NO! ...                  ... MNO! ..."
	print "    ..... MNO!! ...................... MNNOO! ..."
	print "  ..... MMNO! ......................... MNNOO!! ."
	print " ..... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! ."
	print "  ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ...."
	print "     ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ..."
	print "    ........ MMMMMMMMMMMMPPPPPOOOOOOII!! ....."
	print "    ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ..."
	print "    ....... MMMMM..    OPPMMP    .,OMI! ...."
	print "     ...... MMMM::   o.,OPMP,.o   ::I!! ..."
	print "  	    .... NNM:::.,,OOPM!P,.::::!! ...."
	print "          .. MMNNNNNOOOOPMO!!IIPPO!!O! ....."
	print "         ... MMMMMNNNNOO:!!:!!IPPPPOO! ...."
	print "           .. MMMMMNNOOMMNNIIIPPPOO!! ......"
	print "        ...... MMMONNMMNNNIIIOO!.........."
	print "    ....... MN MOMMMNNNIIIIIO! OO .........."
	print "    ......... MNO! IiiiiiiiiiiiI OOOO ..........."
	print "  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........"
	print "  .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........"
	print "  ...... MNNNNO! .. PPPPPPPPP .. MMNON!........"
	print "   ...... OO! ................. ON! ......."
	print "      ................................"
	print "%s died,   GAME OVER" % (name)
	print ""
	print ""
	print "Would you like to play again?"
	play_again = raw_input()
	if play_again == "YES" or "Y":
		game_setup()
	elif play_again == "NO":
		print "%s gave up with a score of %s" % (name, score)
def credits():
	print "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
	print "This text based adventure game was made by Matthew Devonshire. Under the copyright act 1435 it is illeagal to copy or reproduce, in part or full, this work without said owners consent. Ihope you enjoyed playing but your really should try and not die next time." 
#Keep this thing at the bottom
game_setup()
