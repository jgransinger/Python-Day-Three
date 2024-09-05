print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you?: "))
    if age >= 18:
        print("You're paying the adult price. Sorry! (over 18)")
    elif age >= 12:
        print("You qualify for the teen's ticket price! (between 12-18)")
    else:
        print ("You qualify for the child's ticket price! (under 12)")
else:
    print("Sorry you have to grow taller before you can ride.")

