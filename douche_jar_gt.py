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
		player.score += statement.analyze_statement
		player.print_added_score(statement.analyze_statement)
		player.print_total_score

	def play_round(self):
		while True: 
			for player in self.players:
				self.take_turn(player)
			num_turns -= 1	
			if self.num_turns <= 0:
				print("Game Over. Good job douches!")
				"***SOME FUNCTION PRINTING OUT SCOREBOARD***"
				break 

class Statement:
	"""The Statement class stores a player's input."""

	def __init__(self, player, string):
		self.player = player 
		self.string = string 
		self.word_list = []
		self.total_douchiness = 0 

	def get_words(self, string):
		"""Takes in a string statement and adds each word in the statment 
		to the word list."""
		words = string.split()
		self.word_list += words 

	def analyze_word(self, word):
		"""Analyzes the douchiness of a single word."""
		"***INSERT CODE HERE***" 

	def analyze_statement(self):
		"""Takes in a word list and analyzes the douchiness of the words."""
		self.get_words(self.string)
		for word in self.word_list:
			self.total_douchiness += self.analyze_word(word)

class Player:
	
	def __init__(self, name):
		self.score = 0
		self.name = name

	def print_name(self):
		print(self.name)
	
	def print_added_score(self, added_score):
		print("Congratulations! You've accumulated an additional", added_score, "douchiness.")

	def print_total_score(self):
		print(player.name, "has a total of", self.score, "douchiness.")
