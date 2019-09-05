import cmd
import textwrap
import sys
import os
import time
import random
from pygame import mixer
from items import *
from map import *
screen_width = 80
helpMenu = False
musicOn = False
titleMenu = True
sys.screen_width = screen_width
#### player Setup ####
class player:
	def __init__(self):
		self.name = ''
		self.hp = 0
		self.job = ''
		self.mp = 0
		self.status_effects = []
		self.location= "c2"
		self.game_over = False
myPlayer = player()



#### Title Screen ####
def title_screen_selections():
	global helpMenu
	global titleMenu
	option = input('> ')
	if option.lower() == "play":
		titleMenu = False
		setup_game()
	elif option.lower() == "help":
		help_menu()
	elif option.lower() == "quit":
		sys.exit()
	elif option.lower() == "music":
		music_control()
	elif option.lower() == "back" and helpMenu:
			title_screen()


	while option.lower() not in ("play", "help", "quit", "music"):
		print("i do not understand the meaning of "+ option)
		option = input('> ')
		if option.lower() == ("play"):
			titleMenu = False
			setup_game()
		elif option.lower() == ("help"):
			help_menu()
		elif option.lower() == ("quit"):
			sys.exit()
		elif option.lower() == "music":
			music_control()
		elif option.lower() == "back" and helpMenu:
			title_screen()

def music_control():
	global musicOn
	global titleMenu
	global helpMenu

	file ='resources/title.mp3'
	mixer.init()
	mixer.music.load(file)
	if not musicOn:
		mixer.music.play()
		musicOn = True
		if titleMenu:
			if helpMenu:
				help_menu()
			else:
				title_screen()
		else:
			prompt()
	if musicOn:
		mixer.music.stop();
		musicOn = False
		if titleMenu:
			if helpMenu:
				help_menu()
			else:
				title_screen()
		else:
			prompt()

def title_screen():
	os.system('clear')
	global helpMenu
	helpMenu = False

	print("#############################################")
	print("# WELCOME TO THE BEST TEXT BASED GAME EVER! #")
	print("#############################################")
	print("                                             ")
	print("                  - Play -                   ")
	print("                  - Help -                   ")
	print("                  - Quit -                   ")
	print("                  - Music-                   ")
	print("                                             ")
	print("#############################################")
	print("# Copyright 2019 by me - dont steal my shit #")
	print("#############################################")
	title_screen_selections()

def help_menu():
	global helpMenu
	helpMenu = True
	os.system('clear')
	print(items['sign'][SHORTDESC])
	print("#############################################")
	print("                  HELP MENU                  ")
	print("#############################################")
	print(" MOMEMENT:                                   ")
	print("  Type: \"UP\", \"DOWN\", \"LEFT\", \"RIGHT\"")
	print("                                             ")
	print(" ACTIONS:                                    ")
	print("  Type: \"Look\", \"Inventory\", \"Take\"    ")
	print("        \"Push\", \"Pull\", \"Speak\"        ")
	print("                                             ")
	print("#############################################")
	print("  Type - Quit to exit or \"Back\" to go back ")
	print("#############################################")
	title_screen_selections()





def print_location():
	print(myPlayer.location.upper())
	print('#' * (4 + len(myPlayer.location)))
	main_game_loop()

def help_in_game():
	print('type \'move\'- and then up, down, left, right to move\n')
	print('try typing.. \'look\', \'location\', \'examine\', \'search\', \'take\', \'inventory\' etc..')

def prompt():
	global musicOn
	print(myPlayer.location.upper())
	print('#' * (4 + len(myPlayer.location)))
	print ('\n' + '==========================')
	print ('What would you like to do?')
	action = input("> ")
	acceptable_actions = ["move", "walk", "go", "travel", "music", "help", "quit", "look", "examine", "interact", "inspect", "location"]
	while action.lower() not in acceptable_actions:
		print ("I do not know the meaning of " + action +'\n')
		action = input("> ")

	if action.lower() in ['quit']:
		sys.exit()
	if action.lower() in ["music"]:
		music_control()
	elif action.lower() in ["move", "walk", "go", "travel"]:
		player_move(action.lower())
	elif action.lower() in ["examine", "interact", "inspect", "location"]:
		player_action(action.lower())

def player_move(myAction):
	print("Where do you want to move to?? \n")
	dest = input("> ")
	dest = dest.lower();
	if dest in ["up", "north"]:
		if not zoneMap[myPlayer.location][UP]:
			print("You cannot go that way")
		else:
			movement_handler(zoneMap[myPlayer.location][UP])
	elif dest in ["down", "south"]:
		if not zoneMap[myPlayer.location][DOWN]:
			print("You cannot go that way")
		else:
			movement_handler(zoneMap[myPlayer.location][DOWN])
	elif dest in ["left", "west"]:
		if not zoneMap[myPlayer.location][LEFT]:
			print("You cannot go that way")
		else:
			movement_handler(zoneMap[myPlayer.location][LEFT])
	elif dest in ["right", "East"]:
		if not zoneMap[myPlayer.location][RIGHT]:
			print("You cannot go that way")
		else:
			movement_handler(zoneMap[myPlayer.location][RIGHT])

	while dest not in []:
		print("Where do you want to move to?? \n")
		dest = input("> ")

		if dest in ["up, north"]:
			if not zoneMap[myPlayer.location][UP]:
				print("You cannot go that way")
			else:
				movement_handler(zoneMap[myPlayer.location][UP])
		elif dest in ["down", "south"]:
			if not zoneMap[myPlayer.location][DOWN]:
				print("You cannot go that way")
			else:
				movement_handler(zoneMap[myPlayer.location][DOWN])
		elif dest in ["left", "west"]:
			if not zoneMap[myPlayer.location][LEFT]:
				print("You cannot go that way")
			else:
				movement_handler(zoneMap[myPlayer.location][LEFT])
		elif dest in ["right", "East"]:
			if not zoneMap[myPlayer.location][RIGHT]:
				print("You cannot go that way")
			else:
				movement_handler(zoneMap[myPlayer.location][RIGHT])

def movement_handler(destination):
	os.system('clear')
	myPlayer.location = destination
	print("-----------------------------------\n")
	print (" you have moved to the " + destination)
	print_location()

def player_action(action):

	if  action.lower() == "location":
		print_location()
	elif action.lower() == "help":
		help_in_game()
	elif action.lower() == "music":
		music_control()
	if zoneMap[myPlayer.location][SOLVED]:
		print ("done")

def main_game_loop():
	while not myPlayer.game_over:
		print('You are at '+ zoneMap[myPlayer.location][ZONENAME])
		prompt()

def setup_game():
	os.system('clear')


	question1 = "Hello what is your name?"
	for c in question1:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.05)
	myPlayer.name = input('> ')

	statement1 = "Nice to meet you " + myPlayer.name + "\n"
	for c in statement1:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.05)
	question2 = "What role do you wish to play?\n"
	question2added = "you can play as a Bum, Hypocrite, or Fuckwit\n"
	for c in question2:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.05)
	for c in question2added:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.03)
	classInput = input('> ')
	validClass = ["bum", "hypocrite", "fuckwit"]
	if classInput.lower() in validClass:
		myPlayer.job = classInput
		print("you chose " + myPlayer.job)
	while classInput.lower() not in validClass:
		print ("invalid class\n")
		for c in question2:
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(0.05)
		for c in question2added:
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(0.03)
		classInput = input('> ')
		validClass = ["bum", "hypocrite", "fuckwit"]
		if classInput.lower() in validClass:
			myPlayer.job = classInput
			print("you chose " + myPlayer.job)

	intro = "Welcome " + myPlayer.name + "\nyou chose to be a " + myPlayer.job
	intro1 = "\nI think i shall call you"
	intro2 = "..."
	intro3 = "\nLets Begin\n"
	intro4 = "Morssy"
	for c in intro:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.05)
	for c in intro1:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.05)
	for c in intro2:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.8)
	for c in intro4:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.07)
	time.sleep(0.5)
	for c in intro3:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.5)
	time.sleep(1.5)
	os.system('clear')
	main_game_loop()


music_control()
title_screen()
