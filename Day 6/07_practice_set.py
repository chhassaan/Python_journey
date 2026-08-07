'''write a program to find out whether a given post is talking about 
"Harry" or not'''
post=("i am harry ")
name=input("enter your name:").lower()
if name in post:
    print("harry is exsit")
else:
    print("harry not exsit in post ")    