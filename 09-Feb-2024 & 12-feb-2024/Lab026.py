#Match Case (basically it is a switch case)

numbers = int(input("Enter the number 1-5\n"))
match numbers:
    case 1 :
        print("You have entered number 1")
    case 2 :
        print("You have entered number 2")
    case 3:
        print("You have entered number 3")
    case 4:
        print("You have entered number 4")
    case _ :
        print("No idea")






