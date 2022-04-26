# names = ['    coNNor', 'max', ' EVan ', 'JORDAN']

# HINT: You will need to use a for loop for iteration

# list_above = []
# list_above.append(names)
# for x in range(len(1000)):
#     print(x)

# names_list = []
# for name in names:
#     print(name.strip().title())
#     names_list.append(name.strip().title())
# print(names_list)


names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']
 

currentformatname = []
for name in names:
    if name not in currentformatname:
        currentformatname.append(name)
print(currentformatname)






