
import random   # Import random so we can pick a random Pokémon

# List of possible Pokémon words for the game
word_list =  [
    "pikachu", "charmander", "bulbasaur", "squirtle", "eevee",
    "jigglypuff", "meowth", "snorlax", "psyduck", "machop",
    "gengar", "onix", "mewtwo", "zapdos", "moltres",
    "articuno", "dragonite", "gyarados", "alakazam", "abra",
    "geodude", "diglett", "rattata", "pidgeotto", "sandshrew",
    "ninetales", "vulpix", "lapras", "magikarp", "ditto"
]

# Hangman ASCII stages, each represents the number of lives left
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6  # Player starts with 6 lives

# Randomly pick a Pokémon from the list
chosen_word = random.choice(word_list)
#print(chosen_word)  # For testing (remove in real game)

# Create a placeholder with underscores the same length as chosen_word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False            # Game continues until win/lose
correct_letters = []         # Keep track of guessed letters

# Main game loop
while not game_over:

    # Show lives left
    print(f"****************************{lives} LIVES LEFT****************************")

    # Ask user for a letter
    guess = input("Guess a letter: ").lower()

    # If letter was already guessed, warn player
    if guess in correct_letters:
        print(f"You have already guessed the letter {guess}")

    # Build the display word after this guess
    display = ""
    for letter in chosen_word:
        if letter == guess:          # If guessed letter matches this position
            display += letter
            correct_letters.append(guess)   # Add to guessed letters
        elif letter in correct_letters:     # Keep already guessed correct letters
            display += letter
        else:
            display += "_"           # Otherwise keep it hidden

    # Show updated word progress
    print("Word to guess: " + display)

    # If guess was wrong, remove a life
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        # If lives run out → game over (lose)
        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    # If no underscores left → game over (win)
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Print the current Hangman stage
    print(stages[lives])
