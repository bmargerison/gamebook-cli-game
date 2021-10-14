"""
1. Write or draw the problem:
Death - when the player dies, selection of death types
Central chamber - the middle room form which player selects the doors
Door - the choices are player makes to enter certain rooms
	door1 - dead instantly
	door2 - 1 in 10 chance of picing correct door
	door3 - where the player obtains the thing required for the final room
	door4 - fake door
	treasure room - the final room where the player wins

2. Extract key concpets and research them

3. Create a class hierarchy and object map for the concepts
Map
	- next_scene
	- opening_scene
Engine
	- play
Scene
	- enter
	- death
	- door1
	- door2 
	- door3 
	- door4
	- treasure room

4. Code the classes and a test to run them

5. Repeat and refine
My first step was to get the code working from the previous exercise, and 
implement the same logic into my game. 

I decided to add some more complexity to make the game flow a bit
better, by adding 'instances' as an argument to be passed to each time a room
is entered. This allows me to go back and forth between rooms without repeating
the story narrative. The change meant I could apply a condition to the final 
room that the traveller must have obtained an item fromm a different room 
before winning the game. These games at this level of knowledge can end up a bit
contrived so I wanted to add this to enhance the user experience.

That being said I am sure there is a better way to implement this, which I may
come back to at a later date. I have spent quite a bit of time on this exercise
as the book takes a huge leap in logic. I've had to use other resources (well...
googling) to aid my understanding. I think the additional layer I've added has
ensured I fully understand what is happening in the code, even if the code may
not be as clean as I'd like.
"""

from sys import exit
from random import randint

class Room(object):

	def enter(self):
		exit(1)

class Motor(object):

	def __init__(self, room_map):
		self.room_map = room_map

	def play(self, instance=1):
		current_room = self.room_map.first_room()

		while True:
			print("\n--------")
			next_room_name = current_room.enter(instance)
			instance = next_room_name[1]
			current_room = self.room_map.next_room(next_room_name[0])

class Dead(Room):

	quips = [
	"You died. You kinda suck at this.",
	"Your mom would be proud... if she were smarter.",
	"Such a luser",
	"I have a small puppy that's better at this."
	]

	def enter(self, instance):
		print(Dead.quips[randint(0,len(self.quips)-1)])
		exit(1)

class Atrium(Room):

	def enter(self, instance):

		if instance == 2:
			print("\n")

		elif instance == 3:
			print("Which door do you choose next?")

		else:
			print("\tChief Executive and the ", story_name)
			print("You are Chief Executive, an adventurer looking for treasure in the catacombs of Paris.")
			print("You enter the network, where there are 5 doors.")
			print("Which door do you choose?")
		
		try:
			door = int(input("> "))

			if door == 1:
				print("You chose door 1.")
				return ('Door1',1)
			elif door == 2:
				print("You chose door 2.")
				return ('Door2',1)
			elif door == 3:
				print("You chose door 3.")
				return ('Door3',1)
			elif door == 4:
				print("You chose door 4.")
				return ('Door4',1)
			else: 
				print("That's not an option ya doofus.")
				print("Please enter a number from 1 to 5.")
				return ('Atrium',3)

		except ValueError:
			print("That's not an option ya doofus.")
			print("Please enter a number from 1 to 5.")
			return ('Atrium',3)

class Door1(Room):

	def enter(self, instance):
		print("You thought you would be clever and pick each door in turn.\nUnfortunately the door leads to a gaping chasm.\nYou fall down the hole to your death.")
		return ('Death',1)

class Door2(Room):

	def enter(self, instance):

		if instance == 2:
			print("\n")

		else:
			print("There are 10 doors lined up.")
			print("9 of the doors are metal, and one of the doors is paper.")
			print("You must run full pace at one of the doors in order to break it.")
			print("Which door do you choose?")

		door = int(input("> "))

		if door > 11 or door <= 0:
			print("That was not one of the options given, please choose again.")
			return ('Door2',2)
		elif door == 11:
			print("Okay smarty pants, you found a magic number, you can proceed.")
			return ('Treasure_room',1)
		elif door == 3:
			print("Phew, that was a paper door!")
			print("You may proceed.")
			return ('Treasure_room',1)
		elif door <= 2 or door >= 4:
			print("That was a metal door. You break your neck. Ouch.")
			return ('Death',1)
		else:
			print("That was not one of the options given, please choose again.")
			return ('Door2',2)


class Door3(Room):

	global story_name_obtained

	def enter(self, instance):
		global story_name_obtained

		if instance == 2:
			print("\n")

		elif story_name_obtained == True:
			print("You have completed your quest here, return to the original room.")
			return('Atrium',3)

		else:
			print("This is the moment you have been searching for your whole life.")
			print("You see it sitting there behind a contraption:")
			print("The magnificent and glorious, unmistakable ", story_name)
			print("To release it, you must put your hand in one of three holes to pull a lever.")
			print("Which is the correct hole?")

		try:
			hole = int(input("> "))

			if story_name_obtained == False:

				if hole == 1:
					return ('Death',1)
				elif hole == 2:
					return ('Death',1)
				elif hole == 3:
					print("You pull the lever and release the ", story_name, "!")
					print("But your journey is not over, and you must return to the orignal room to find the treasure.")
					story_name_obtained = True
					return('Atrium', 3)

		except ValueError:
			print("That's not an option ya doofus.")
			print("Please enter a number from 1 to 3.")
			return ('Door3',2)

class Door4(Room):

	def enter(self, instance):
		print("There isn't really a door 4, I was just kidding.")
		print("Please choose again.")
		return ('Atrium',3)

class Treasure_room(Room):

	def enter(self, instance):

		print("You have made it! You have found the treasure room!")
		print("But wait, it turns out you need the ", story_name, "to proceed.")

		if story_name_obtained == True:
			print("\nLucky for you traveller, you alredy have it!")
			print("Take all the gold that your heart desires.")
			print("But beware, this level of wealth can corrupt even the most dignified travellers.")
			print("\n")
			print("YOU WIN")
			exit(1)

		else:
			print("You will have to return to the original room to find it.")
			return('Atrium', 3)

class Map(object):

	rooms = {
		'Atrium': Atrium(),
		'Door1': Door1(),
		'Door2': Door2(),
		'Door3': Door3(),
		'Door4': Door4(),
		'Treasure_room': Treasure_room(),
		'Death': Dead(),
	}

	def __init__(self, beginning):
		self.beginning = beginning

	def next_room(self, room_name):
		return(Map.rooms.get(room_name))

	def first_room(self):
		return self.next_room(self.beginning)

story_name = "muppet"
story_name_obtained = False
a_map = Map('Atrium')
a_game = Motor(a_map)
a_game.play()
