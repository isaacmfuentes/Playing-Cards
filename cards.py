import random

class Card:
    """
    Class for representing individual playing cards.

    Attributes:
        suit (str): The suit of the card, e.g., "Clubs", "Diamonds", "Hearts", or "Spades".
        value (int): The numerical value of the card, ranging from 2 to 14.
        name (str): The name of the card, such as "2" to "10", "Jack", "Queen", "King", or "Ace".

    Methods:
        __init__(self, value, suit): Initializes a Card instance with the specified value and suit.
        get_card_name(self, value): Returns the name of the card based on its value.
        __str__(self): Returns a string representation of the card, e.g., "7 of Diamonds".
    """

    def __init__(self, value, suit):
        """
        Initialize a Card instance with the provided value and suit.

        Args:
            value (int): The numerical value of the card.
            suit (str): The suit of the card.
        """
        self.suit = suit
        self.value = value
        self.name = self.get_card_name(value)

    def get_card_name(self, value):
        """
        Get the name of the card based on its value.

        Args:
            value (int): The numerical value of the card.

        Returns:
            str: The name of the card, such as "2" to "10", "Jack", "Queen", "King", or "Ace".
        """

        if 2 <= value <= 10:
            return str(value)
        elif value == 11:
            return "Jack"
        elif value == 12:
            return "Queen"
        elif value == 13:
            return "King"
        elif value == 14:
            return "Ace"

    def __str__(self):
        """
        Get a string representation of the card.

        Returns:
            str: A string representing the card, e.g., "7 of Diamonds".
        """
        return f"{self.name} of {self.suit}"

class Deck:
    """
    Class for representing a deck of playing cards.

    Attributes:
        cards (list): A list of Card objects representing the cards in the deck.

    Methods:
        __init__(self): Initializes a Deck instance with a full deck of shuffled cards.
        generate_deck(self): Generates a standard 52-card deck with cards of varying values and suits.
        shuffle_deck(self): Shuffles the cards in the deck.
        draw(self): Draws a card from the deck and returns it.
    """

    def __init__(self):
        """
        Initialize a Deck instance with a full deck of shuffled cards.
        """
        self.cards = []
        self.generate_deck()
        self.shuffle_deck()

    def generate_deck(self):
        """
        Generate a standard 52-card deck with cards of varying values and suits.
        """
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        for suit in suits:
            for value in range(2, 15):
                card = Card(value, suit)
                self.cards.append(card)

    def shuffle_deck(self):
        """
        Shuffle the cards in the deck.
        """
        random.shuffle(self.cards)

    def draw(self):
        """
        Draw a card from the deck.

        Returns:
            Card: A Card object representing the drawn card.

        Raises:
            RuntimeError: If the deck is empty, this exception is raised.
        """
        if self.cards:
            return self.cards.pop()
        else:
            raise RuntimeError("The deck is empty.")
