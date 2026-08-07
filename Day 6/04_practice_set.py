'''write a program to find whether a given username contains 
less than 10 charcter or not'''
user_name=input("enter your name: ")
if(len(user_name)<10):
    print("your user name contain less than 10 character")
else:
    print("all is well")    


'''Write a program to check whether a given password 
contains less than 8 characters or not.'''   
password=input("enter your password")
if(len(password)<8):
    print("your contain password is less than 8")
else:
    print("your contain password is more than 8 ")    


'''Write a program to check whether a given name 
contains more than 15 characters or not.'''
name=input("enter your name:")
if(len(name)>15):
    print("your contain password is more than 15")
else:
    print("your contain password is less than 15 or not")    
