'''we all have played snack,water gun game in our childhood.if you havent google the rules of this 
game and write a python program capable of playing this game with user'''
import random
choices=["snake","water","gun"]
computer=random.choice(choices)
user=input("enter your choice:").lower()
print("computer choice :",computer)
if user==computer:
    print("Draw")
elif user=="Snake"  and computer=="water":
    print("you win") 
elif user=="water" and computer=="gun":
    print("you win")
elif user=="gun" and computer=="snake":
    print("you win")
else:
    print("computer win")         


'''snake=-1
water=0
gun=1'''
import random
computer=random.randint(-1,1)
you=(input("Enter your number:")).lower()
choice={"s":-1,
        "w":0,
        "g":1}
reversedict={-1:"Snake",
             0:"water",
             1:"gun"}
yourdict=choice[you]
print(f"your choise:{reversedict[yourdict]}")
print(f"Computer choice:{reversedict[computer]}")
if yourdict==computer:
    print("Draw!")
elif yourdict==-1 and computer==0:
    print("You win!")
elif yourdict==0 and computer==1:
    print("you win!")
elif yourdict==1 and computer==-1:
    print("you win!")
else:
    print("Computer win!")        