from random import *
print("Welcome to the number guess game!!")
print("I'm thinking of a number between 1 and 100 .")
choice = input("Choose a difficulty level....type 'easy' or 'Hard' : ")
ch_num = randint(1,100)
print(ch_num)

if choice == "easy":
    n = 10
    for i in range(n):
        print ("You have "+ str(n) + " attempts remaining to guess a number.")
        nn = int(input("Make a guess: "))
        n = n-1
        if nn == ch_num:
            print("Your guess is right")
            break
        elif nn > ch_num:
            print("Too high")
            print("Guess Again....")
        elif nn < ch_num :
            print("Too low")
            print("Guess Again....")
else: 
    n = 5
    for i in range(n):
        print ("You have "+ str(n) + " attempts remaining to guess a number.")
        nn = int(input("Make a guess: "))
        n = n-1
        if nn == ch_num:
            print("Your guess is right")
            break
        elif nn > ch_num:
            print("Too high")
            print("Guess Again....")
        elif nn < ch_num :
            print("Too low")
            print("Guess Again....")



