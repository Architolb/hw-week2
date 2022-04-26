#Given a string after every y add an ! and after every s add a peroid and make every w and g capital
#Make a Function that takes a string as input and returns the adjusted string.
s="Hey welcome to doing whiteboard problems get prepared to figure our a problem on the fly"
#output= Hey! Welcome to doinG Whiteboard problems. Get prepared to fiGure our a problem on the fly!


def fix_string(s):
    new_sentence=""
    for letter in s:
        if letter.lower()=='y':
            new_sentence+=letter+"!"
        elif letter.lower()=='s':
            new_sentence+=letter+"."
        elif letter.lower()=='w' or letter.lower()=='g':
            new_sentence+=letter.upper()
        else:
            new_sentence+=letter
    return new_sentence

print(fix_string(s))




def punctuation(sentence):
    x = ' '
    for letters in sentence:
        if letters == 'y':
            x = x + 'y!'
        elif letters == 's':
            x = x + 's'
        elif letters == 'w':
            x = x + 'w'
        elif letters == 'g':
            x = x + 'G'
        else:
            x = x + letters
    return x
print (punctuation(s))
