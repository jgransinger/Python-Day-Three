print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

sPizza = 15
mPizza = 20
lPizza = 25
sPepperoni = 2
mlPepperoni = 3
xCheese = 1

#Small pie
if size == "S":
    total = sPizza
    if pepperoni == "Y":
        total += sPepperoni
    if extra_cheese == "Y":
        total += xCheese
    print(f"Your final bill is: ${total}")

#Medium pie
elif size == "M":
    total = mPizza
    if pepperoni == "Y":
        total += mlPepperoni
    if extra_cheese == "Y":
        total += xCheese
    print(f"Your final bill is: ${total}")

#Large pie
elif size == "L":
    total = lPizza
    if pepperoni == "Y":
        total = total + mlPepperoni
    if extra_cheese == "Y":
        total = total + xCheese
    print(f"Your final bill is: ${total}")

