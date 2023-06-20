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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("INSTRUCTION : TYPE YOUR CHOICE AT EVERY STEP")
lr = input("So let's start....you are at cross road and now you have to choose 'left' or 'right' ?? ").lower()


if lr == "left":
    sw = input("Now you are at lake and island is in between the lake ....so do you want to 'swim' across or 'wait' for boat ?? ").lower()
    if sw == "wait":
        d = input("heyyy!!! Welcome to the island.....last step to win treasure. you habe 3 doors to choose 'red' , 'yellow' , 'blue' . make a right choice or you will be loosing your treasure. ").lower()

        if d == "red":
            print("!!!!! YOU WON !!!!!")
            print("you won lots and blessing and well wishes for your future journey.")
        elif d == "yellow":
            print("Attacked by wild animals \n GAME OVER")
        else:
            print("Burned by fire.\n GAME OVER")
    else:
        print("Attacked by trout. \n GAME OVER")
else:
    print("Fall into a hole.\n GAME OVER")
