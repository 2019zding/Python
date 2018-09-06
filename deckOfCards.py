import Random

# the three classes will inherit from the object
class Card(object):
	# the method
	def __init__(self, suit, val):
		# creating attributes
		self.suit = suit
		self.value = val

	# self so that we have access to the attributes
	def show(self):
		# print out value and suit
		print"{} of {}".format(self.value, self.suit)

class Deck(object):
	def __init__(self):
		self.cards = []
		self.build()

	def build(self):
		# building a deck of class using a for loop because
		# you are able to iterate throughout the numbers and then
		# the suits
		for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
			# range is because there are 14 cards in each suit
			for v in range(1, 14):
				# add into card list, instance of card class
				# therefore, you pass down suit and value
				self.cards.append(Card(s,v))
				print v "{} of {}".format(v, s)

	def show(self):
		# for every card in self.cards, show.card, show that card
		for c in self.cards:
			c.show()

	def shuffle(self):
		# range because from the end of the list and back again
		# the length is inclusive, therefore (self.cards)-1
		for i in range(len(self.cards)-1, 0, -1)
			# random number, from left of position because we are
			# starting at the right --> iterating backwards
			rand = random.randint(0, i)
			# then swap two cards, cards at i and r 
			self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

	def drawCard(self):
		# remove a card from the end of deck (pop) and return 
		# that card to method called draw
		return self.cards.pop()

class Player(object):
	def __init__(self, name):
		self.name = name
		# player has hand, start off as
		# empty array and should be able to draw from deck
		self.hand = []

	# draw method needs access to deck
	def draw(self, deck):
		# append the card back to hand
		# function is equal to its return value 
		self.hand.append(deck.drawCard())
		return self

	def showHand(self):
			for card in self.hand:
				card.show()

	def discard(self):
		# pop is remove and return to index
		return self.hand.pop()

# card = Card("Clubs", 6)
# card.show()

deck = Deck()
deck.shuffle()
deck.show()

# zara = Player("Zara")
# zara.draw(deck).draw(deck)
# zara.showHand()

# card = deck.draw()
# card.show()