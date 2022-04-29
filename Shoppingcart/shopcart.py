
shopping_cart = {}

print("""
Welcome to Rude/Food
_ _ _ _ _ _ _ _ _ _ _ 
1: Add Item
2: Remove Item
3: Review Basket
0: Exit Store
""")


option = int(input('Enter an option: '))

while option !=0:
    if option == 1:
        item = input("Pick something!: ")
        quantity = int(input("How many?!: "))
        shopping_cart[item] = quantity
    elif option == 2:
        item = input("Make up your mind!!: ")
        del(shopping_cart[item])
    elif option == 3:
        for item in shopping_cart:
            print(item,":",shopping_cart[item])

    elif option != 0:
        print("We don't have that!")

    option = int(input('\n\nHurry up and buy!!:'))

else:
    print("Get out NOW!!!")






