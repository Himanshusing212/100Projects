
import random 
print("WELCOME TO THE ROCK PAPER SCISSOR GAME")
game = ['rock','paper','scissor']
n = int(input("number of rounds you want to play: "))
count1 = 0
count2 = 0
while n > 0:
    a = int(input("what do you choose ? 0 for rock , 1 for paper and 2 for scissor \n"))
    uch = game[int(a)]
    cch = random.choice(game)
    print("USER CHOICE IS     : ", uch)
    print("COMPUTER CHOICE IS : ", cch)



    if (uch=='rock' and cch =='rock') or (uch=='paper' and cch =='paper') or      (uch=='scissor' and cch =='scissor') :
        print("DRAW !! RESTART THE GAME")
        count1= count1+1
        count2= count2+1
        n-=1

    elif(uch=='rock' and cch =='paper') or (uch=='paper' and cch =='scissor') or (uch=='scissor' and cch =='rock'):
        print("COMPUTER WINS")
        count2 = count2+2
        n-=1

    elif(uch=='rock' and cch =='scissor') or (uch=='scissor' and cch =='paper') or (uch=='paper' and cch =='rock'):
        print("USER WINS")
        count1 = count1+2
        n-=1

    else:print("RESTART GAME")

print("FINAL SCORECARD")
print("USER: ",count1)
print("COMPUTER: ",count2)
if (count1 > count2):
    print("USER WINS THE SERIES")
elif(count2 > count1): 
    print("COMPUTER WINS THE SERIES")
else:
    print("SERIES DRAWS")



