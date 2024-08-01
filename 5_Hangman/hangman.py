import random 
from words import words 
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words) # letters in the word
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # letters used 
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have ', lives ,' lives left you have used these letters: ', ' '.join(used_letters))

        # what the status of current word ( W _ R _)
        word_list = [letter if letter in used_letters else '-' for letter in word] # list comprehension  numbers = [1, 2, 3, 4, 5] squares = [x**2 for x in numbers]
        print( 'Current word: ', ' '.join(word_list))
        #getting the user input
        user_letter = input('Guess a letter: ').upper()
        # if the user letter is new and haven't been used
        if user_letter in alphabet - used_letters:
            # then add to the used letters set
            used_letters.add(user_letter)
            # And if the user guessed the letter 
            if user_letter in word_letters:
                # then remove it from the word letters set
                word_letters.remove(user_letter)
            else:
                lives = lives -1 # take the live for inccorect guess
                print("letter is not in the word")

        elif user_letter in used_letters:
            print('You have already used this letter. Please try again. ')
        else: 
            print('Invalid character. Please try again.')
        # while lop ends when the word_letters == 0 or lives == 0
        if lives == 0:
            print('You died, sorry. The word was ', word)
        else:
            print('You guessed the word', word, '!!')     

##user_input = input('Type something: ')
##print(user_input)
hangman();