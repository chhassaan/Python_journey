'''a spam comment is defiend as a text containing following keyword 
"Make a lot of money","Buy now","Subscribe this channel","click this"
write a program to detect these spam'''
mail=input("Enetr your word:").lower()
if("Make a lot of money" in mail or
   "Buy now" in mail or
   "Subscribe this channel or" in mail or
   "click this" in mail
):
    print("spaim mail")
else:
    print("not spam")




mail=input("enter your word:").lower()
if("make a lot of money" in mail or
   "buy now" in mail or
   "subscribe this channel or" in mail or
   "click this" in mail
):
    print("spam email")
else:
    print("not a spam")    

'''User se username lo.

Agar username "admin" ho to print:

Welcome Admin

# Warna print:

# Access Denied'''
name=input("enter your name:").lower()
if(name=="admin"):
    print("welocome admin")
else:
    print("access denied")    


'''Spam keywords:

free
winner
prize
click here

Agar in mein se koi bhi word message mein ho to:

Spam Message

Warna:

Safe Message'''
word=input("enter your word:").lower()
if(word=="free" or
   word=="winner" or
   word=="prize" or
   word=="click here"
):
    print("spam email")
else:
    print("not a spam")    



p1="make a lot of money"
p2="buy now"
p3="subscribe tthis channel"
p4="click this"
word=input("enter your word:").lower()
if(p1 in word) or (p2 in word) or (p3 in word) or (p4 in word):
    print("spaim email")
else:
    print("not a spaim ")    





