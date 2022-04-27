# Function_Exercise  Write a function that loops through a list of first_names and a list of last_names, combines the two and return a list of full_names

first_name = ['John', 'Evan', 'Jordan', 'Max']
last_name = ['Smith', 'Smith', 'Williams', 'Bell']

for i in range(len(first_name)):
    print(first_name[i], last_name[i])




# Exercise1 Given a list as a parameter,write a function that returns a list of numbers that are less than ten
# For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

my_list =  [1,11,14,5,8,9]
for n in my_list:
    if n<10:
        print(n)




# Write a function that takes in two lists and returns the two lists merged together and sorted
# Hint: You can use the .sort() method

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]
sorted_3 = sorted(l_1) + sorted(l_2)
print(sorted(sorted_3))
