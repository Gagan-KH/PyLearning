#Match Case

Browsers = str(input("Enter the browser name \n"))
#Browsers = Browsers.lower()  ("Not working need to check")
match Browsers:
    case "Chrome":
        print("you have entered chrome browser")
    case "Firefox":
        print("You have entered firefox browser")
    case "Edge":
        print("you have entered edge browser")
    case _:
        print("No browser found")

