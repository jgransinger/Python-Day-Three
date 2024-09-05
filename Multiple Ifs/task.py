print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
        bill = 5
    elif age <= 18:
        print("Please pay $7.")
        bill = 7
    else:
        print("Please pay $12.")
        bill = 12
    photo = input("Want a photo? (Y/N): ")
    if photo == "y":
        print("That'll be $3 additional dollars.")
        bill += 3
        print(f"Your total ticket price is: {bill}")
    else:
        print("You won't be charged for a photo.")
        print(f"Your total ticket price is: {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
