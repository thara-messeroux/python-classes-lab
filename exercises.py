'''
Classes Lab
Exercise
Introduction
In this lab, you can practice object-oriented programming (OOP) by building a Tic-tac-toe terminal game with Python Classes.

While working through this lab, consider the gameplay of Tic-Tac-Toe and, if necessary, pseudocode it. Try to write several small functions, each performing a single purpose, e.g., print_board, get_move, check_for_winner, etc. Consider how/where looping makes sense, e.g., loop until the player enters a correct move or until the game’s over, etc.

User Stories
Your goal is to implement the following user stores:

As a user (AAU), I want to see a welcome message at the start of a game.
AAU, before being prompted for a move, I want to see the board printed in the console to know what moves have been made.
AAU, at the beginning of each turn, told whose turn it is: It’s player X’s turn!
AAU, I should be prompted to enter a move and be provided an example of valid input ('Enter a valid move (example: A1)').
AAU, I want to be able to enter my move’s column letter in upper or lower case (a/A, b/B, or c/C) to make it easier to enter my move.
AAU, if I enter a move in an invalid format or try to occupy a cell already taken, I want to see a message chastising me and be re-prompted.
AAU, after entering a move, I should once again be presented with the updated game board, notified of the current turn, and asked to enter a move for the other player. This process should continue until there is a winner or a tie
AAU, I should see a message at the end of the game indicating the winner or stating that the game ended in a tie.
Hints
If you need some guidance with this lab, follow the steps below.

Step 1 - Define a Game class and initialize game state
Create a class called Game. Within the Game class, use the __init__ method to initialize properties that represent the state of your game.

Below are some of the attributes you might include:

turn: a string attribute indicating whose turn it is ('X' or 'O'). Initialize it with 'X'.
tie: a boolean attribute indicating if the game ended in a tie. Initialize it as False.
winner: an attribute to store the game-winner. Initialize it as None.
board: a dictionary representing the state of the game board:

Copy
{
  'a1': None, 'b1': None, 'c1': None,
  'a2': None, 'b2': None, 'c2': None,
  'a3': None, 'b3': None, 'c3': None,
}
Each key in the board represents a position on the board, with the corresponding value being an 'X', 'O', or an empty space (None).

Modeling the board itself as a dictionary and naming the keys appropriately can simplify updating the board based on what the player types in. For example, assume you store the player’s input in a variable named move. You can convert it to lowercase using .lower() and use it as the key to access the board, i.e., board[move].

Step 2 - Playing the game
Next, define a play_game method and confirm that the method is accessible on an instance of the Game class. This function will be used to activate and organize the flow of the game.

Within the play_game method, print a welcome message of your choosing.
Instantiate the Game class and invoke the play_game method:

Copy
game_instance = Game()
game_instance.play_game()
Run the following command in your terminal to verify your welcome message:

Copy
python3 app.py
Step 3 - Rendering
Next, you’ll want to define methods that can ‘render’ information for the user. Based on the separation of concerns, you might break this logic down into two or three methods.

Consider the following approach:

Rendering the board
The print_board method visualizes the current state of the game board.

Copy
def print_board(self):
  b = self.board
  print(f"""
        A   B   C
    1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
        ----------
    2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
        ----------
    3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
  """)
The print statement above should produce something like the following in your terminal:

Copy
        A   B   C
    1)    |   |
        ----------
    2)    |   |
        ----------
    3)    |   |
Rendering messages
The print_message method updates users about the current status of a game, including whose turn it is, who won the game, and if the game ended in a tie.

Copy
  def print_message(self):
    ## If there is a tie: print("Tie game!")
    ## If there is a winner: print(f"{self.winner} wins the game!")
    ## Otherwise: print(f"It's player {self.turn}'s turn!")
Consolidated rendering
Optionally, a third render method can be used to consolidate the other two, streamlining the rendering process:

Copy
  def render(self):
    # Call upon print_board
    ## Call upon print_message
Step 4 - Handling player input
Next, you’ll need a method to handle user input, such as get_move or place_piece. This method should prompt a user to enter the key of an empty space on the board.

To capture player input, use the input() function. This function displays a prompt in the terminal and returns the string that the user enters.

Copy
move = input(f"Enter a valid movie (example: A1): ").lower()
Within this method, it’s essential to ensure that the input received is valid.

Valid input must satisfy two conditions:

The input corresponds to a key on the board.
The specified board space is currently unoccupied (None).
To achieve this, set up a loop that continuously prompts the user until a valid input is received. You can create an infinite loop with while True. When valid input is received, the loop should be configured to conclude with a return or break statement.

Take a look at the structure below for reference:

Copy
  while True:
    # prompt user for input
    # If the input is valid, update the board and break the loop
    # otherwise, print a message notifying the user of the invalid input and allow the loop to continue
Step 5 - Checking for a winner
Next, create a method for determining a winner by checking the board for the eight possible winning combinations. Upon detecting a winning combination, update the winner attribute to reflect the current player (turn).

A loop of some sort would be appropriate, but you can also check each combination manually:

Copy
self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1'])
💡 This example checks for a winning condition across the top row. Similar logic can be applied to other win conditions.

Step 6 - Checking for a tie
The check_for_winner method should be followed with a check_for_tie method.

This method should check if both of the following conditions are true:

The board is entire: All spaces on the board are filled, with no positions marked as None.
No winner: A winner has not already been declared.
If both of these conditions are met, the value of tie should be set to True.

Step 7 - Switching turns
The switch_turn method should alternate the value of turn between 'X' and 'O'. This should occur at the end of every turn. There are several ways to accomplish this, but a small lookup table using a dictionary might work nicely.

Step 8 - Managing gameplay
The last step is combining all these methods in a functional gameplay loop. The loop should continue until a winner or tie is declared.

Below is an outline of how you might structure the play_game method:

Copy
  def play_game(self):
    print("Shall we play a game?")
    # While there is no winner or tie
        # render
        # get player input
        # check for a winner
        # check for a tie
        # switch turns
        # ...repeat until there is a winner or tie
    # Outside the loop, render state at the end of a game


If you wish to expand on the functionality of your game, try implementing the following user stories:

AAU, at the end of a game, I should be asked if I would like to play again.
AAU, if I accept the offer to play again, the game should reset and begin again.
AAU, if I decline the offer to play again, the program should stop running.
AAU, I would like the game to record wins and losses and display these records at the end of every game.
'''
class Game:
    def __init__(self):
        # --- BONUS feature: Initialize win/loss tracking variables ---
        self.score = {'X': 0, 'O': 0, 'Ties': 0}
        self.reset_game_state()

    def reset_game_state(self):
        # Reset everything back to the starting point for a new round
        self.turn = 'X'      # Player X always starts
        self.tie = False     # Game starts without a tie
        self.winner = None   # No winner at the beginning
        self.board = {       # Clear out the board entirely
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def print_board(self):
        # Step 3: Draw the 3x3 grid using standard text so the player can see it
        b = self.board
        print(f"""
              A   B   C
          1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
              ----------
          2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
              ----------
          3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        # Step 3: Print text updating players on what is happening
        if self.tie:
            print("🤝 Tie game!")
        elif self.winner:
            print(f"🎉 Player {self.winner} wins the game!")
        else:
            print(f"👋 It's player {self.turn}'s turn!")

    def render(self):
        # Step 3: Combine drawing the board and updating messages into one action
        self.print_board()
        self.print_message()

    def get_move(self):
        # Step 4: Infinite loop that keeps asking until the player makes a legal move
        while True:
            move = input("Enter a valid move (example: A1): ").strip().lower()
            
            # Check condition A: Is this an actual square on our board?
            if move not in self.board:
                print("❌ Oops! That spot doesn't exist. Please choose a space from A1 to C3.")
                continue
                
            # Check condition B: Is anyone already standing there?
            if self.board[move] is not None:
                print("❌ That spot is already taken! Pick an empty square.")
                continue
            
            # If it passes both tests, update the board state and exit the loop
            self.board[move] = self.turn
            break

    def check_for_winner(self):
        # Step 5: Check all 8 ways a player can achieve 3-in-a-row
        b = self.board
        winning_combos = [
            ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'], # Rows
            ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'], # Columns
            ['a1', 'b2', 'c3'], ['c1', 'b2', 'a3']                      # Diagonals
        ]
        
        for combo in winning_combos:
            # If the first spot is filled and matches the next two spots, we have a winner!
            if b[combo[0]] and (b[combo[0]] == b[combo[1]] == b[combo[2]]):
                self.winner = b[combo[0]]
                return

    def check_for_tie(self):
        # Step 6: If there's no winner, but every single board value is full, it's a tie
        if not self.winner and all(value is not None for value in self.board.values()):
            self.tie = True

    def switch_turn(self):
        # Step 7: Simple swap logic using a dictionary as a shortcut toggle
        toggle = {'X': 'O', 'O': 'X'}
        self.turn = toggle[self.turn]

    def play_game(self):
        # Step 2 & 8: The main orchestration machinery that runs the game loop
        print("\n👾 Welcome to Py-Pac-Poe! 👾")
        
        while True:
            self.reset_game_state()
            
            # Run the active match until someone wins or ties
            while not self.winner and not self.tie:
                self.render()
                self.get_move()
                self.check_for_winner()
                self.check_for_tie()
                if not self.winner and not self.tie:
                    self.switch_turn()
            
            # Show the final results of the match
            self.render()
            
            # --- BONUS Feature: Track the lifetime session records ---
            if self.winner:
                self.score[self.winner] += 1
            elif self.tie:
                self.score['Ties'] += 1
                
            print("\n📊 Current Scoreboard:")
            print(f"Player X: {self.score['X']} wins | Player O: {self.score['O']} wins | Ties: {self.score['Ties']}")
            
            # --- BONUS Feature: Offer an explicit option to replay or close out ---
            replay = input("\nWould you like to play again? (y/n): ").strip().lower()
            if replay != 'y':
                print("\nThanks for playing Py-Pac-Poe! Goodbye! 👋")
                break

# Execute the application
if __name__ == "__main__":
    game_instance = Game()
    game_instance.play_game()