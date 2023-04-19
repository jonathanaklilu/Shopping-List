from shoppinglinkedlist import ShoppingList

print("Welcome to your Shopping List")
shopping = True
your_list = ShoppingList()
while shopping:
    print("\nMENU")
    print("Add to List (a/A) | Remove from List (r\R) | Cross out from List (c\C) | Print List (p/P) | Quit (q/Q)")
    user_choice = input("Enter your choice: ").lower()
    print(' ')
    if user_choice == 'a':
        addition = input("What would you like to add to your Shopping List?: ")
        your_list.insert(addition)
    elif user_choice == 'r':
        index = int(input("Enter the number on the list you want to remove: "))
        your_list.removefromlist(index)
    elif user_choice == 'c':
        index = int(input("Enter the number on the list you want to cross out: "))
        your_list.crossoutvalue(index)
    elif user_choice == 'p':
        your_list.printshoppinglist()
    elif user_choice == 'q':
        quit()
    else:
        continue