#Main application

#Ask user name and do they like cats

name = input("What's your name? ")

likeCats = input("Do you like cats? yes or no ")

if likeCats == "yes":
    print(name, "yay, you like cats! ")

else:
    print(name, "oh no! you don't like cats ")

def nameLength(name):
    """Calculates name length

    Args:
        name (str): name of the person

    Returns:
        int: returns length of the name
    """
    length = len(name)
    return length

#Calculate name length

length = nameLength(name)
print(name, " has ", length, " words.")