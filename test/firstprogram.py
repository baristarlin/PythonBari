#def määrittää funktion ja mitä muuta se tekee
def say_hi(name):
    if name == '':
        print("You didn't enter your name")
    else:
        print("Hi there...")
        for letter in name:
                print(letter)

#Lets create a loop
while True:
    name = input("Your name: ")
    say_hi(name)


