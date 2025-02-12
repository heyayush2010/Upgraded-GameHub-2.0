import random
import time

# Cluedo code

# The dice
NUMBERS = ["1", "2", "3", "4", "5", "6"]

def roll_dice():
    return random.randint(1, 6)

# Assign values to game characters and conditions
CHARACTERS = ["Miss Scarlett", "Colonel Mustard", "Mr. Green", "Mrs. Peacock", "Professor Plum"]
WEAPONS = ["Candlestick", "Dagger", "Lead Pipe", "Revolver", "Rope"]
ROOMS = ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Billiard Room", "Library", "Lounge", "Hall", "Study"]
CROSS_OUT = {"characters": [], "weapons": [], "rooms": []}  # Items that have been excluded

def setup_game():
    hidden_character = random.choice(CHARACTERS)
    hidden_weapon = random.choice(WEAPONS)
    hidden_room = random.choice(ROOMS)
    return hidden_character, hidden_weapon, hidden_room

def get_clue(room):
    clues = {
        "Kitchen": ["A character is nearby.", "A weapon was found in the corner.", "No one has entered this room today."],
        "Ballroom": ["The windows are locked.", "Someone might have passed through this room.", "It seems a weapon was placed here recently."],
        "Library": ["You hear a faint noise coming from a hidden room.", "The lights flicker occasionally.", "A weapon is under a chair."],
        "Conservatory": ["The plants are well maintained.", "A suspicious footprint near the window.", "A glass vase is missing."],
        "Dining Room": ["There are food stains on the table.", "A strange sound came from the adjacent room.", "The curtains are drawn."],
        "Billiard Room": ["The pool table is disturbed.", "A cue ball is missing.", "The lights are dim in this room."],
        "Lounge": ["A chair is tipped over.", "A strange smell is in the air.", "There's a shadow near the window."],
        "Hall": ["You hear footsteps approaching.", "A door creaks loudly.", "The floor is dusty."],
        "Study": ["There are papers scattered around.", "A book is missing from the shelf.", "A faint smell of tobacco."],
    }
    return random.choice(clues.get(room, ["No clue available for this room."]))

def cross_out_item(item, category):
    if item not in CROSS_OUT[category]:
        CROSS_OUT[category].append(item)
        print(f"{item} has been crossed out from your list.")
    else:
        print(f"{item} is already crossed out.")

def make_accusation():
    accusation_character = input(f"Accuse a character from {CHARACTERS}: ").strip()
    accusation_weapon = input(f"Accuse a weapon from {WEAPONS}: ").strip()
    accusation_room = input(f"Accuse a room from {ROOMS}: ").strip()
    return accusation_character, accusation_weapon, accusation_room

def play_cluedo(hidden_character, hidden_weapon, hidden_room):
    current_room = random.choice(ROOMS)
    print(f"You start in the {current_room}.")
    
    while True:
        input("Press Enter to roll the dice...")
        roll = roll_dice()
        print(f"You rolled a {roll}.")
        
        # Move to a new room
        current_room_index = ROOMS.index(current_room)
        new_room_index = (current_room_index + roll) % len(ROOMS)
        current_room = ROOMS[new_room_index]
        print(f"You moved to the {current_room}.")
        
        # Get a clue card for the current room
        clue = get_clue(current_room)
        print(f"Clue card: {clue}")
        
        print("\nMake your guess:")
        guess_character = input(f"Choose a character from {CHARACTERS}: ").strip()
        guess_weapon = input(f"Choose a weapon from {WEAPONS}: ").strip()
        guess_room = current_room  # The guess room is the current room
        
        print(f"Guess: {guess_character} with the {guess_weapon} in the {guess_room}")
        
        if (guess_character == hidden_character and 
            guess_weapon == hidden_weapon and 
            guess_room == hidden_room):
            print("Congratulations! You have guessed the correct character, weapon, and room!")
            break
        else:
            print("Incorrect guess. Try again.")
            cross_out_item(guess_character, "characters")
            cross_out_item(guess_weapon, "weapons")
            cross_out_item(guess_room, "rooms")
        
        # Ask if player wants to make an accusation
        accuse = input("Do you want to make an accusation? (yes/no): ").strip().lower()
        if accuse == "yes":
            accusation_character, accusation_weapon, accusation_room = make_accusation()
            if (accusation_character == hidden_character and 
                accusation_weapon == hidden_weapon and 
                accusation_room == hidden_room):
                print("Your accusation is correct! You win!")
                break
            else:
                print("Your accusation is incorrect. You lose.")
                break

def watch_cluedo(hidden_character, hidden_weapon, hidden_room):
    current_room = random.choice(ROOMS)
    print(f"The simulation starts in the {current_room}.")
    
    while True:
        roll = roll_dice()
        print(f"Rolled a {roll}.")
        
        # Move to a new room
        current_room_index = ROOMS.index(current_room)
        new_room_index = (current_room_index + roll) % len(ROOMS)
        current_room = ROOMS[new_room_index]
        print(f"Moved to the {current_room}.")
        
        guess_character = random.choice(CHARACTERS)
        guess_weapon = random.choice(WEAPONS)
        guess_room = current_room  # The guess room is the current room
        print(f"Guess: {guess_character} with the {guess_weapon} in the {guess_room}")
        
        if (guess_character == hidden_character and 
            guess_weapon == hidden_weapon and 
            guess_room == hidden_room):
            print("The correct character, weapon, and room have been guessed!")
            break


# Snakes and Ladders code

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time is up!")

def roll_dice_snakes_ladders():
    return random.randint(1, 6)

def move_player(player, position, roll):
    new_position = position + roll
    if new_position > 100:
        new_position = position  # Player cannot move beyond 100
    return new_position

def check_snake_or_ladder(position):
    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    if position in snakes:
        print(f"Player landed on a snake at {position}! Going down to {snakes[position]}")
        return snakes[position]
    elif position in ladders:
        print(f"Player landed on a ladder at {position}! Going up to {ladders[position]}")
        return ladders[position]
    return position

def play_snakes_and_ladders():
    player_positions = [0, 0]
    player_turn = 0

    while True:
        input(f"Player {player_turn + 1}'s turn. Press Enter to roll the dice...")
        roll = roll_dice_snakes_ladders()
        print(f"Player {player_turn + 1} rolled a {roll}")
        player_positions[player_turn] = move_player(player_turn, player_positions[player_turn], roll)
        player_positions[player_turn] = check_snake_or_ladder(player_positions[player_turn])
        print(f"Player {player_turn + 1} is now on square {player_positions[player_turn]}")

        if player_positions[player_turn] == 100:
            print(f"Player {player_turn + 1} wins!")
            break

        if roll != 6:
            player_turn = 1 - player_turn  # Switch turn if the roll is not 6

# Chess code
def play_chess():
    print("Starting a game of Chess...")
    board = [[" " for _ in range(8)] for _ in range(8)]
    board[0] = ["R", "N", "B", "Q", "K", "B", "N", "R"]
    board[1] = ["P"] * 8
    board[6] = ["p"] * 8
    board[7] = ["r", "n", "b", "q", "k", "b", "n", "r"]

    def print_board():
        for row in board:
            print(" ".join(row))
        print()

    def move_piece():
        while True:
            move = input("Enter your move (e.g., e2 e4): ").strip().lower()
            if len(move) == 5 and move[2] == " ":
                start, end = move.split()
                start_col, start_row = ord(start[0]) - ord('a'), 8 - int(start[1])
                end_col, end_row = ord(end[0]) - ord('a'), 8 - int(end[1])
                if 0 <= start_col < 8 and 0 <= start_row < 8 and 0 <= end_col < 8 and 0 <= end_row < 8:
                    board[end_row][end_col] = board[start_row][start_col]
                    board[start_row][start_col] = " "
                    break
                else:
                    print("Invalid move. Try again.")
            else:
                print("Invalid move format. Try again.")

    print_board()
    while True:
        move_piece()
        print_board()

# Football code
def play_football():
    print("Starting a game of Football...")
    team1_score = 0
    team2_score = 0
    for turn in range(10):
        team1_score += random.randint(0, 1)
        team2_score += random.randint(0, 1)
        print(f"Turn {turn + 1}: Team 1 - {team1_score}, Team 2 - {team2_score}")
    if team1_score > team2_score:
        print("Team 1 wins!")
    elif team2_score > team1_score:
        print("Team 2 wins!")
    else:
        print("It's a draw!")

# Uno code
def play_uno():
    print("Starting a game of Uno...")
    colors = ["Red", "Yellow", "Green", "Blue"]
    values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Skip", "Reverse", "Draw Two"]
    deck = [f"{color} {value}" for color in colors for value in values] * 2
    random.shuffle(deck)

    player_hand = [deck.pop() for _ in range(7)]
    computer_hand = [deck.pop() for _ in range(7)]
    discard_pile = [deck.pop()]

    def draw_card(hand):
        hand.append(deck.pop())

    def play_card(hand, card):
        hand.remove(card)
        discard_pile.append(card)

    def valid_play(card, top_card):
        card_color, card_value = card.split()
        top_color, top_value = top_card.split()
        return card_color == top_color or card_value == top_value

    while True:
        print(f"Top card: {discard_pile[-1]}")
        print(f"Your hand: {', '.join(player_hand)}")
        player_move = input("Enter the card to play or 'draw' to draw a card: ").strip()
        if player_move == "draw":
            draw_card(player_hand)
        elif player_move in player_hand and valid_play(player_move, discard_pile[-1]):
            play_card(player_hand, player_move)
        else:
            print("Invalid move. Try again.")

        if not player_hand:
            print("You win!")
            break

        computer_move = next((card for card in computer_hand if valid_play(card, discard_pile[-1])), None)
        if computer_move:
            play_card(computer_hand, computer_move)
            print(f"Computer played: {computer_move}")
        else:
            draw_card(computer_hand)
            print("Computer drew a card.")

        if not computer_hand:
            print("Computer wins!")
            break

if __name__ == "__main__":
    game_choice = input("Enter 'cluedo' to play Cluedo, 'snakes' to play Snakes and Ladders, 'chess' to play Chess, 'football' to play Football, or 'uno' to play Uno: ").strip().lower()
    
    if game_choice == 'cluedo':
        hidden_character, hidden_weapon, hidden_room = setup_game()
        mode = input("Enter 'play' to play the game or 'watch' to watch the simulation: ").strip().lower()
        
        if mode == 'play':
            play_cluedo(hidden_character, hidden_weapon, hidden_room)
        elif mode == 'watch':
            watch_cluedo(hidden_character, hidden_weapon, hidden_room)
        else:
            print("Invalid mode selected.")
    
    elif game_choice == 'snakes':
        play_snakes_and_ladders()
    
    elif game_choice == 'chess':
        play_chess()
    
    elif game_choice == 'football':
        play_football()
    
    elif game_choice == 'uno':
        play_uno()
    
    else:
        print("Invalid game choice. Please enter 'cluedo', 'snakes', 'chess', 'football', or 'uno'.")