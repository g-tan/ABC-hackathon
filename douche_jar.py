"""The Douche Jar, adapted from New Girl"""

import random
import sys
from ucb import main, interact, trace

class Game:
	
	def __init__(self, players, num_turns=10):
		self.players = players
		self.num_turns = num_turns

	def take_turn(self, player):
		player_statement = input('Hey douche! Enter a douchey statement: ')
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

	def analyze_statement(self, word_list):
		"""Takes in a word list and analyzes the douchiness of the words."""

def play_game(args, players):
	import argparse 
