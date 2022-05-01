# Word-guessing-game

# need a library to choose words from
import random

# need a list of words

words = ['gatorade', 'mother', 'father', 'movies', 'library', 'title','lettuce' , 'dodgeball', 'football']
word = random.choice(words)
# need spaces for inputs
spaces = ['_']* len(word)
# function to find letters in guessing word and return the letters if guessed correctly

def letter_place(guess, word, spaces):
    index = -2
    while index != -1:
        if guess in word:
            index = word.find(guess)
            removed_character = '*'
            word = word[:index]+removed_character+word[index+1:]
            spaces[index] = guess
        else:
            index = -1

    return (word, spaces)


# function to check letters guessed correctly yes/no

def win_check():
    for i in range(0, len(spaces)):
        if spaces[i] == '_':
            return -1

    return 1


turns = len(word)
for i in  range(0, turns):
    guess = input('Guess a character')
    if guess in word:
        word, spaces = letter_place(guess, word, spaces)
        print(spaces)
    else:
        print('Sorry that letter is not in the word')

    if win_check() == 1:
        print('YOU WIN!!!')
        break
    print('You have '+str(turns - i)+' turns left.')
    print()