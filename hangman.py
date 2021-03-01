# Testproject with python: Hangman game
from random import randint

def find_word():
    # Read available words from textfile
    with open('textfile.txt') as textfile:
        words = list(textfile)

    #Get random word
    count_words = len(words)
    rand_value = randint(0, count_words - 1)
    word = words[rand_value].rstrip().lower()

    return word

def print_text(explain, guess_word):
    print(explain)
    print_gw = ' '.join(map(str, guess_word))
    print(print_gw)
    guess_letter = input('Guess a letter: ')
    return guess_letter

word = find_word()
guess_word = ["."] * len(word)
print("Hoi")
print(guess_word)
print(word)

end_game = False
errors = 0
print_line = "Welcome to hangman"
while end_game == False:
    letter = print_text(print_line, guess_word)
    letter = letter.lower()

    # Check the input
    if letter.isalpha() == False:
        # non-alphanumeric input
        print_line = "Wrong input. Only letters allowed."
        continue
    double = [i for i, x in enumerate(guess_word) if x == letter]
    if len(double) != 0:
        # Letter already used
        print_line = "Wrong input. Letter already used"
        continue

    # Check if the guessed letter occurs in the word
    found = [i for i, x in enumerate(word) if x == letter]
    if len(found) == 0:
        errors = errors + 1
        if errors > 5:
            print_line = "You have lost..."
            break
    else:
        for y in found:
            guess_word[y] = letter
        check_win = [i for i, x in enumerate(guess_word) if x == '.']
        if len(check_win) == 0:
            print_line = "You have won!!!"
            break
    print_line = "Total errors: {}".format(errors)
print(print_line)
