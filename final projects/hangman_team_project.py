import random

words = ['python', 'hangman', 'development', 'code', 'programming']

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


def get_random_word():
    return random.choice(words)


def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# p and t
# output p_t___


def display_hangman(lives_left):
    print(hangman_graphics[6 - lives_left])


def play_game():
    word = get_random_word()
    guessed_letters = []
    wrong_guesses = []
    lives = 6
    used_letters = set()

    print("Welcome to Hangman!")
    print(f"Thw word has {len(word)} letters")

    while lives > 0:
        print("\nCurrent word " + display_word(word, guessed_letters))
        print(f"Wrong guesses: {', '.join(wrong_guesses)}")
        display_hangman(lives)

        guess = input("Enter a letter (or type quit to exit): ").lower()  # Python #python

        if guess == 'quit':
            print("Goodbye!")
            break

        if guess in used_letters:
            print(f"You have already guessed {guess}. Try again")
            continue

        used_letters.add(guess)

        if guess in word.lower():
            guessed_letters.extend([letter if letter.lower() == guess else '_' for letter in word])
            print(f"Good guess! The letter {guess} is in the word")
        else:
            wrong_guesses.append(guess)
            lives -= 1
            print(f"Oops! The letter {guess} is not in the word")

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations, you've guessed the word: {word}!")
            break

        if lives == 0:
            print(f"\nSorry, you lost! The word was: {word}")
            display_hangman(lives)
            break


play_game()






















