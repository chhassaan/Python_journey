'''write a program to find out whether a files is identical & matches the contant of another file'''
with open("first.txt","r")as f:
    contant=f.read()
with open("secound.txt","r")as f:
    contant2=f.read()
    if contant==contant2:
        print("yes first and secound file contant is same")
    else:
        print("not same contant")    