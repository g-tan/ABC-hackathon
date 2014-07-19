"""The Douche Jar, adapted from New Girl"""

import random
import sys
from ucb import main, interact, trace
from string import ascii_letters
from data import word_sentiments

class Game:
	
	def __init__(self, num_turns=10):
		self.players = []
		self.num_turns = num_turns
		self.num_players = 0
		self.sorted_players = []  

	def get_num_players(self):
		while True:  
			print()
			self.num_players = input("How many douches are there? ")
			try:
				int(self.num_players)
				print()
				print("Got it. There are", self.num_players, "players.")
				break 
			except ValueError:
				print("Bro I didn't get that. Enter a numeral ('1', '4', '16')")

	def create_players(self):
		for i in range(int(self.num_players)):
			name = input("Hey douche, what's your name? ")
			print("Got it. Added", name, "to the player list.")
			print()
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

	def sort_scores(self):
		self.sorted_players = self.players[0:]
		for i in range(len(self.sorted_players)):
			for j in range(i+1, len(self.sorted_players)):
				if self.sorted_players[j].score > self.sorted_players[i].score:
					self.sorted_players[j], self.sorted_players[i] = self.sorted_players[i], self.sorted_players[j]

	def print_scoreboard(self):
		print("SCOREBOARD")
		self.sort_scores()
		for i in range(len(self.sorted_players)):
			print(str(i+1)+".",self.sorted_players[i].name,"("+str(self.sorted_players[i].score)+")")


class Statement:
	"""The Statement class stores a player's input."""

	def __init__(self, player, string):
		self.player = player 
		self.string = string 
		self.word_list = []
		self.total_douchiness = 0 

	def extract_words(self, text):
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
		for word in self.word_list:
			if word_sentiments.get(word) != None:
				score += word_sentiments.get(word)
				counter += 1
		if counter != 0:
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
		print()
		print("Congratulations! You've accumulated an additional", added_score, "douchiness.")
		print()

	def print_total_score(self):
		print(player.name, "has a total of", self.score, "douchiness.")

@main
def play_game():
	game_rounds = int(input("How many rounds? "))
	game = Game(game_rounds)
	game.get_num_players()
	game.create_players()
	round_number = 1
	while round_number <= game_rounds:
		print()
		print("GET READY FOR THE NEXT ROUND.")
		print()
		print()
		print()
		for player in game.players:
			print("It is now", player.name+"'s turn.")
			game.take_turn(player)
			print
		print("Round over. Here's the scoreboard:")
		game.print_scoreboard()
		game.sort_scores()
		if round_number == game_rounds:
			print()
			print("Game over, bro! The winner is: "+game.sorted_players[0].name+".")
		round_number += 1

