'''the game()
function in a program lets a user paly a game and retuen the score as an integer.
you need to read a file "hi score.txt" which is either blank or contains the the previous 
high score. you need to write a program to update the hi score whenever thhe game() function 
breakes te hi score'''
# import random
# def game():
#     print("you are palying the game!")
#     score=random.randint(1,100)

#     with open("hiscore.txt") as f:
#         hiscore=f.read()
#         if (hiscore!=""):
#             hiscore=int(hiscore)
#         else:
#             hiscore=0

#     print(f"your score {score}")

#     if (score>hiscore ):
#         with open("hiscore.txt","w")as f:
#             f.write(str(score))
#             print("new high score!")

#     return score
# game() 

















# import random
# def game():
#     score=random.randint(1,100)
#     with open("hiscore.txt")as f:
#         hiscore=f.read()
#         if (hiscore!=""):
#             hiscore=int(hiscore)
#         else:
#             hiscore=0
#     print(f"your score:{score}")

#     if (score>hiscore):
#         with open ("hiscore.txt","w")as f:
#             f.write(str(score))



#     return score

# game()

    







# '''

# Ek file score.txt hai jisme ek number stored hai.
# Program:

# File se score read kare.
# Agar score 50 se zyada hai to "You passed" print kare.
# Warna "You failed" print kare.'''

# with open("scored.txt","r")as f:
#     hiscore=int(f.read())
# if hiscore>50:
#     print("you passed")
# else:
#     print("you failed")    






# print(".....................next..............................")



# '''Ek file highscore.txt mein ek purana high score stored hai.

# Program:

# User se current score input lo.
# File se old high score read karo.
# Dono ko compare karo.
# Agar current score zyada ho:'''

# score=int(input("enter your score:"))
# with open("hiscore.txt","r")as f:
#     hiscore=int(f.read())
#     if (hiscore>score):
#         print("old hi score is still higher")
#     else:
#         print("new hiscore")    








# '''Ek file number.txt hai.

# Program:

# User se ek number input lo.
# File mein jo purana number hai, usko read karo.
# Dono numbers compare karo.
# Agar user ka number purane number se zyada hai:
# file mein naya number write karo
# "Number updated" print karo.
# Agar user ka number chhota ya equal ho:
# file ko change mat karo
# "Old number is greater or equal" print karo.'''

# num=int(input("enter your number:"))

# with open("number.txt","r")as f:
#     number=int(f.read())

#     if num>number:
#         with open("number.txt","w")as f:
#             f.write(str(num))
#         print("Number updated")
#     else:
#         print("old number is greater or equal") 







# with open("number.txt","r")as f:
#     data=f.read()
#     if data=="":
#         print("fille is empty")
#     else:
#         print("file has data")    




import random
def game():
    print("start your game!")
    score=random.randint(1,100)

    with open("hiscore.txt")as f:
        hiscore=f.read()
        if hiscore!="":
            hiscore=int(hiscore)
        else:
            hiscore=0
        print(f"your score:{score}")
        if score>hiscore:
            with open("hiscore.txt","w")as f:
                f.write(str(score))
    return score
game()