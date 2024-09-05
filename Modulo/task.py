#Modulo - operator gives you the remainder of a division.

print(6 % 2) #6/2 is two
print(6 % 5) #6/5 is 1 with a remainder of 1
print(6 % 4) #6/4 is 1 with a remainder of 2

#Odd or even assignment
number = int(input("Pick a number: "))
if number % 2 == 0:
    print("That's an even number!")
else:
    print("That's an odd number!")