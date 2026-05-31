# Step 1 - Define a Game class and initialize game state
# Create a class called Game. Within the Game class, use the __init__ method to initialize properties that represent the state of your game.

# Below are some of the attributes you might include:

# turn: a string attribute indicating whose turn it is ('X' or 'O'). Initialize it with 'X'.
# tie: a boolean attribute indicating if the game ended in a tie. Initialize it as False.
# winner: an attribute to store the game-winner. Initialize it as None.
# board: a dictionary representing the state of the game board:

{
  'a1': None, 'b1': None, 'c1': None,
  'a2': None, 'b2': None, 'c2': None,
  'a3': None, 'b3': None, 'c3': None,
}

# Each key in the board represents a position on the board, with the corresponding value being an 'X', 'O', or an empty space (None).

# Modeling the board itself as a dictionary and naming the keys appropriately can simplify updating the board based on what the player types in. For example, assume you store the player’s input in a variable named move. You can convert it to lowercase using .lower() and use it as the key to access the board, i.e., board[move].

class Game:
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
        