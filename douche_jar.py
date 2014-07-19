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
<<<<<<< HEAD
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
	def sort_scores(self):
		self.sorted_players = self.players[0:]
		for i in range(len(self.sorted_players)):
        	for j in range(i+1, len(self.sorted_players)):
            	if self.sorted_players[j] < self.sorted_players[i]:
                	self.sorted_players[j], self.sorted_players[i] = self.sorted_players[i], self.sorted_players[j]



	def print_scoreboard(self):
		print("SCOREBOARD")
		for i in range(len(self.sorted_players)):
			print((b+1)+".", self.sorted_players[i].name)




=======
		if player.turns_taken >= self.num_turns:
			"***SOME KIND OF GAME OVER***"
		else:
			statement = Statement(player, input("Enter a douchey statement: "))
			print("Congratulations! You've accumulated an additional", statement.analyze_statement, "douchiness.")
			player.score += statement.analyze_statement
			print(player.name, "now has a total of", player.score, "douchiness.")
			player.turns_taken += 1
>>>>>>> d1856d2e2b4304588a0a569de4e7b370a1b2ec68

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

	def print_score(self):
		print(self.score)

	def update_score(self, added_score):
		self.score += added_score
	
	def print_added_score(self, added_score):
		print("Congratulations! You've accumulated an additional", added_score, "douchiness.")

	def print_total_score(self):
		print(player.name, "has a total of", self.score, "douchiness.")

			


@main
def play_game():
	game_rounds = input("How many rounds? ")
	game = Game(game_rounds)
	game.get_num_players()
	game.create_players()
	round_number = 1
	while round_number <= game_rounds:
		print("GET READY FOR THE NEXT ROUND.")
		for player in game.players:
			print("It is now", player.name+"'s turn.")
			player.take_turn
		print("Round over. Here's the scoreboard:")
		game.print_scoreboard()
		round_number += 1
		if round_number == game_rounds:
			print("Game over, bro! The winner is:", game.sorted_players[0].name+".")
		
