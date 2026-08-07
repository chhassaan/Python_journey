'''Write a program for a simple account login system.

The program should take username and password from the user.

Rules:

1. If username is "admin" and password is "12345":
   Print "Login Successful"

2. If username is empty or password length is less than 5:
   Print "Invalid Details"

3. If password contains "123":
   Print "Weak Password"

4. Otherwise:
   Print "Login Failed"'''
#first try fail
# name=input("ENTER USER NAME :").lower()
# password=int(input("ENTER YOUR PASSWORD :"))

# if(name=="admin") and (password==12345):
#     print("login successful")
# elif(len(name)>5) and (len(password)>5):
#     print("Invalied details")
# elif(len(password)<5):
#     print("weak password")
# else:
#     print("login failed")           

#secound try
# user_name=input("ENTER YOUR NAME:")
# password=int(input("ENTER YOUR PASSWORD :"))
# if (user_name=="admin") and (password==12345):
#     print("login successful")
# elif(user_name=="")or (password>5):   #phala len nikalni ha password ki 
#     print("Invalid details")  
# elif(password<5):
#     print("weak password")
# else:
#     print("login failed")        


#third try
user_name=input("ENTER YOUR NAME:")
password=input("ENTER YOUR PASSWORD :")
if (user_name=="admin") and (password==12345):
    print("login successful")
elif(user_name=="")or len(password)<5:
    print("Invalid details")  
elif "123" in password:
    print("weak password")
else:
    print("login failed")               
