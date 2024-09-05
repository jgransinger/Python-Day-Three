print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Path Choice
path = input("You approach a fork in the forest. Which path will you choose? Left or Right?: \n")
if path == "Left" or path == "left":
    print("You choose the left path, and wander along until you reach a river. ")
    river = input("A boat will arrive in 30 minutes, but you could also swim across. What do you do, Wait or Swim?: \n")
    if river == "Wait" or river == "wait":
        print("You decided to play it safe, and wait. Your decision pays off, as the boat arrives just as scheduled. ")
        door = input("You step onto the boat and sail across the river. Immediately on the other side, you see a building. "
                     "As you enter the front door, you see three doors of different colors. Which color "
                     "door do you open: Red, Blue, or Yellow?: \n")
        if door == "Blue" or door == "blue":
            print("The blue door creaks open, and you are presented with more gold than you ever imagined. You did it!")
        elif door == "Red" or door == "red":
            print("The red door creaks open, and a tiger jumps towards your face and mauls you to death. You died!")
        elif door == "Yellow" or door == "yellow":
            print("The yellow door opens, and the smell of toxic gas and poison overwhelms you. You have died!")
    elif river == "Swim":
        print("Piranhas swarm and maul you to death. Game over. ")
elif path == "Right" or path == "right":
    print("You take three steps onto the right path, and fall into a pit with spikes. You have died.")
else:
    print("Incorrect entry. Game Over. ")

#############################################################################################

#IGNORE BELOW --- IT WOULDNT WORK THIS WAY

# path = input("You approach a fork in the forest. Which path will you choose? Left or Right?: \n")
# if path == "Left" or "left":
#     print("You choose the left path, and wander along until you reach a river. ")
#     river = input("A boat will arrive in 30 minutes, but you could also swim across. What do you do, Wait or Swim?: \n")
# elif path == "Right" or "right":
#     print("You fall into a hole and die. Game over.")
#
# if river == "Wait" or "wait":
#     print("You decided to play it safe, and wait. Your decision pays off, as the boat arrives just as scheduled. ")
#     door = input("You step onto the boat and sail across the river. Immediately on the other side, you see a building. "
#                  "As you enter the front door, you see three doors of different colors. Which color "
#                  "door do you open: Red, Blue, or Yellow?: \n")
# elif river == "Swim" or "swim":
#         "You were mauled by angry piranha's with laser beams on their heads. Game over."