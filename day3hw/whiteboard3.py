# Find Palindrome
# Given a string of lowercase letters, write a function to see if the word is a palindrome (the same word spelled forward and backwards).
# Example Input: 
# string1 = "racecar"
# string2 = "Was it a car or a cat I saw"
# Example Output: True 
# write down the string backward/forward to answere if_palindrome
# def is_palindrome(x):
#    x = x.upper().replace(" ","")
#    return x == x[::-1]
   
# print(is_palindrome(string2))


#  Exercise_1  
# car = {'year': 1984,'make': 'Cadillac','model': 'Coupe Deville'}

# print(f"{car['year']} {car['make']} {car['model']}!")



# Exercise_2

people = {
    'Max': 'blue',
    'Lilly': 'brown',
    'Barney': 'blue',
    'Larney': 'brown',
    'Ted': 'purple'
}

# def people():
#     for key,value in people.items():
#         print(f"{key} has .format(){value} eyes")
        


def loopDict(dictionary):
        for k, v in dictionary:
            print(f'{k} has {dictionary[v]} eyes.')
loopDict(people)
#Exercise_3

def my_function():
    empty_dictionary = {}
    active = True
    while active == True:
        name = input("What is your name?")
        clear_output()
        address = input("What is your address?")
        clear_output()
        quit = input("Would you like to add another input?")
        clear_output()
        empty_dictionary[name] = address
        if quit.lower() == 'no':
            active = False
            return empty_dictionary
print(my_function())