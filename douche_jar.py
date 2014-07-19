"""The Douche Jar, adapted from New Girl"""

import random
import sys
from ucb import main, interact, trace

class Game:
	
	def __init__(self, num_turns=10):
		self.players = []
		self.num_turns = num_turns
		num_players = 0 

	def get_num_players(self):
		while True:  
			self.num_players = input("How many douches are there? ")
			try:
				self.num_players = int(self.num_players)
				print("Got it. There are", self.num_players, "players.")
				break 
			except ValueError:
				print("Bro I didn't get that. Enter a numeral ('1', '4', '16')")

	def create_players(self):
		for i in range(self.num_players):
			name = input("Hey douche, what's your name? ")
			print("Got it. Added", name, "to the player list.")
			self.players.append(Player(name))

	def take_turn(self, player):
		statement = Statement(player, input("Enter a douchey statement: "))
		player.turns_taken += 1

class Statement:
	"""The Statement class stores a player's input."""

	def __init__(self, player, string):
		self.player = player 
		self.string = string 
		self.word_list = [] 

	def get_words(self, string):
		"""Takes in a string statement and adds each word in the statment 
		to the word list."""
		words = string.split()
		self.word_list += words 

	def analyze_word(self, word):
		"""Analyzes the douchiness of a single word."""
		"***INSERT CODE HERE***" 

	def analyze_statement(self, word_list):
		"""Takes in a word list and analyzes the douchiness of the words."""

class Player:
	
	def __init__(self, name):
		self.score = 0
		self.name = name
		self.turns_taken = 0
	
	def print_score(player):
		print(self.score)
	
	def make_list(player):
		nonlocal lst
		lst.append(player)

def play_game(args, players):
	import argparse 
