import random

# Predefined list of words (for simplicity, we are using these)
# List (Data Structure: List) - This list contains words that will be used for the game.
# A random word will be selected from this list at the start of each game.
words = ['python', 'hangman', 'development', 'code', 'programming']

# ASCII Art for Hangman based on remaining lives
# List (Data Structure: List) - This list stores the ASCII art that will represent the hangman
# at different stages depending on the remaining number of lives.
# Each element in this list corresponds to the hangman state at each life loss (from 6 lives to 0 lives).
hangman_graphics = [
    '''
     -----
     |   |
         |
         |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
         |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
     |   |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
    /|   |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    '''
]

# Function to get a random word
# This function randomly selects a word from the predefined list of words.
# Random selection is done using the `random.choice()` method, which returns a random item from a list.
def get_random_word():
    return random.choice(words)

# Function to display the current game state (word with guessed letters)
# This function takes the word and a list of guessed letters, and returns a string representation of the current word.
# For each letter in the word, if the letter is guessed correctly, it is shown. If not, it is replaced with an underscore ('_').
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Function to display the current hangman state (lives left)
# This function prints the ASCII art corresponding to the number of lives left.
# It uses the `hangman_graphics` list, where the index is calculated as `6 - lives_left` to show the right state.
def display_hangman(lives_left):
    print(hangman_graphics[6 - lives_left])

# Function to run the game
def play_game():
    word = get_random_word()  # Select a random word from the predefined list
    guessed_letters = []  # List to keep track of correctly guessed letters
    wrong_guesses = []  # List to store incorrect guesses
    lives = 6  # Starting number of lives (6 lives)
    used_letters = set()  # Set to track all the letters that have been guessed before

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")  # Print the number of letters in the word

    # The main game loop runs as long as the player has lives left
    while lives > 0:
        # Display the current game state (word with guessed letters)
        print("\nCurrent word: " + display_word(word, guessed_letters))
        print(f"Wrong guesses: {', '.join(wrong_guesses)}")  # Show all incorrect guesses
        display_hangman(lives)  # Display the hangman ASCII art based on the current number of lives

        # Ask the player for a guess (or allow quitting)
        guess = input("Enter a letter (or type 'quit' to exit): ").lower()  # Convert input to lowercase for case-insensitive comparison

        # Quit condition: if the player types 'quit', the game ends
        if guess == 'quit':
            print("Goodbye!")
            break

        # Input validation: Ensure the player enters a single letter
        # If the input is not a single letter or if it's not an alphabet character, we prompt the player to try again
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if the player has already guessed this letter
        # If the letter has already been guessed, we inform the player and continue to the next iteration
        if guess in used_letters:
            print(f"You've already guessed '{guess}'. Try again.")
            continue

        used_letters.add(guess)  # Add the guessed letter to the set of used letters

        # Check if the guessed letter is in the word
        # If the letter is found in the word, we reveal it in the current game state
        if guess in word.lower():  # Case-insensitive comparison by converting both word and guess to lowercase
            # We update the guessed letters list to reveal all instances of the guessed letter in the word
            guessed_letters.extend([letter if letter.lower() == guess else '_' for letter in word])
            guessed_letters = list(dict.fromkeys(guessed_letters))  # Remove duplicate letters from guessed_letters
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            # If the guess is incorrect, we add it to the list of wrong guesses and reduce the number of lives
            wrong_guesses.append(guess)
            lives -= 1  # Reduce a life for each incorrect guess
            print(f"Oops! The letter '{guess}' is not in the word.")

        # Check if the player has won: All letters in the word have been correctly guessed
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations, you've guessed the word: {word}!")
            break

        # Check if the player has lost: No lives left
        if lives == 0:
            print(f"\nSorry, you lost! The word was: {word}")
            display_hangman(lives)  # Display the final hangman state when the player loses
            break


# The main entry point of the program, which starts the game
play_game()
