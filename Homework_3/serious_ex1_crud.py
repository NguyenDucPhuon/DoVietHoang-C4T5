read = ["T-Shirt", "Sweater"]
crud = input("Welcome to our shop, what do you want (C, R, U, D) ?")
choice = crud.upper()

while choice== "R" or "C" or  "U" or "D" :
    if choice == "R" :
        print("Our items: ", end = ' ')
        print(*read, sep = ', ')


    elif choice == "C" :
        new_item = input("Enter new item: ")
        read.append(new_item)
        print("Our items: ", end = ' ')
        print(*read, sep = ', ')

    elif choice == "U" :
        index = int(input("Update position ? "))
        new_item = input("Enter new item: ")
        read[index - 1] = new_item
        print("Our items: ", end = ' ')
        print(*read, sep = ', ')

    elif choice == "D" :
        delete_index = int(input("Delete position ? "))
        read.remove(read[delete_index - 1])
        print("Our items: ", end = ' ')
        print(*read, sep = ', ')

    else:
        print("See you next time")
        break

    crud = input("Welcome to our shop, what do you want (C, R, U, D) ?")
    choice = crud.upper()




