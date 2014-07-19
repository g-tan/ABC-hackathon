"""The Douche Jar, adapted from New Girl"""

import random
import sys
from ucb import main, interact, trace

class Game:
	
	def __init__(self, num_turns=10):
		self.players = []
		self.num_turns = num_turns
		self.num_players = 0
		self.sorted_players = []  

	def get_num_players(self):
		while True:  
			self.num_players = input("How many douches are there? ")
			try:
				int(self.num_players)
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
		statement.analyze_statement()
		player.score += statement.total_douchiness
		player.print_added_score(statement.total_douchiness)
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

	def print_scoreboard(self):


class Statement:
	"""The Statement class stores a player's input."""

	def __init__(self, player, string):
		self.player = player 
		self.string = string 
		self.word_list = []
		self.total_douchiness = 0 

	def extract_words(text):
    """Returns the words in a string in a list, not including punctuation."""
	    return_text = ""
	    for character in text:
	        if character in ascii_letters:
	            return_text += character
	        else:
	            return_text += " "
	    self.word_list += return_text.split() 

	def analyze_statement(self):
		"""Analyzes the douchiness of the words in statment."""
		self.extract_words(self.string)
		counter = 0
		score = 0
		inFile = open("douchejar_dictionary.cvs")
		for word in self.word_list:
			if word in inFile:
				score += inFile[word]
				counter += 1
		inFile.close()
		self.total_douchiness += score/counter

class Player:
	
	def __init__(self, name):
		self.score = 0
		self.name = name

	def print_name(self):
		print(self.name)

	def print_score(self):
		print(self.score)

	def update_score(self, added_score):
		self.score += added_score
	
	def print_added_score(self, added_score):
		print("Congratulations! You've accumulated an additional", added_score, "douchiness.")

	def print_total_score(self):
		print(player.name, "has a total of", self.score, "douchiness.")
