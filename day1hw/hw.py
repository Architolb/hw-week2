# Exercise1. Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.

number = 1
while number**3 <1001:
    print(number)
    number += 1


# Exercise2. Get first prime numbers up to 100

x = 1
y = 100
for num in range(x,y + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)



# Exercise3. Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors

age = int(input('How old are you?'))

if age < 18:
    print('kids')
elif age < 65:
    print('adults')
else:
    print('seniors')
    



