import random

class Game:
	def __init__(self, amt, want):
		self.games = 0
		self.wins = 0
		self.losses = 0
		self.amount = amt
		self.want = want

	def help(self, amt):
		x = random.randint(0, 1)

		if x > 0.5:
			return amt #gained amt
		elif x < 0.5:
			return -amt #lost amt
		else:
			return self.help(amt)

	def play(self):
		self.games += 1

		amt = self.amount
		betAmt = 1

		while amt < self.want and amt != 0:
			if betAmt > amt:
				num = self.help(amt)
				amt += num

				if num > 0:
					betAmt = 1
			else:
				num = self.help(betAmt)
				amt += num

				if num > 0:
					betAmt = 1
				else:
					betAmt *= 2

		if amt >= self.want:
			self.wins += 1
		else:
			self.losses += 1


	def display(self):
		print('Win Percent: {} , Game no {}, Loss Percent {}'.format(self.wins/self.games, self.games, self.losses/self.games))

	def oneRound(self):
		self.play() # plays one round of a game
		#self.display() # displays the result of the game

amt = int(input('Enter the amount you\' are willing to use: '))
want = int(input('Enter the amount that u want to get: '))

x = Game(amt, want)

times = int(input('Enter the Number of Tries: '))
for i in range(times):
	x.oneRound()

x.display()
