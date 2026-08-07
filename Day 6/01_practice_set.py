'''write a program to find the greatest of four numbers enterd by the user'''
num1=int(input("ENTER YOUR FIRST NUMBER:"))
num2=int(input("ENTER YOUR sec NUMBER:"))
num3=int(input("ENTER YOUR third NUMBER:"))
num4=int(input("ENTER YOUR fourth NUMBER:"))
if(num1>num2 and num1>num3 and num1>num4):
     print("NUM 1 is greatest")
elif(num2>num1 and num2>num3 and num2>num4):
     print("num 2 is greatest")    
elif(num3>num1 and num3>num2 and num3>num4):
     print("num 3 is greatest")
else:
     print("num 4 is greatest")    


'''Write a Python program that takes a number from the user and checks:

If number is positive → print "Positive"
If number is negative → print "Negative"
If number is zero → print "Zero"

Concepts:

if-elif-else
comparison operators'''
num=int(input("ENTER YOUR FIRST NUMBER:"))
if(num>0):
    print("positive")
elif(num<0):
    print("negative")
else:
    print("zero")        





    

'''Write a program that takes marks from the user and displays grade:

90 or above → Grade A
80 to 89 → Grade B
70 to 79 → Grade C
60 to 69 → Grade D
Below 60 → Fail

Concepts:

if-elif-else
multiple conditions'''
num=int(input('enter your marks:'))
if(num>90):
    print("GRADE A")
elif(num>80):
    print("Grade B")
elif(num>70):
    print("Grade C")
elif(num>60):
    print("Grade D")
else:
    print("Fail")                



'''Create a simple login system.

Store:

correct username = "admin"
correct password = "12345"

# Ask user for username and password.

# Rules:

# Both correct → "Login Successful"
# Username wrong → "Invalid Username"
# Password wrong → "Invalid Password"

# Concepts:

# logical operators
# comparison operators''' 
#70% correct mistakes
name=input("ENTER YOUR NAME:")
password=input("ENTER YOUR PASSWORD:")
if(name=="Hassaan@123" and password=="Allahone@123"):
    print("Vallied user name")
    print("login successfull")
else:
    print("Invalid password")
    print("invallied username")
    print("please put valied name and password")

#100% correct
name=input("ENTER YOUR NAME:")
password=input("ENTER YOUR PASSWORD:") 
if(name=="Hassaan098" and password=="Allahone098"):
    print("login successfull")
elif(name!="Hassaan098"):
    print("Invalied name")
    print("please use correct username")
elif(password!="Allahone098"):
    print("Invalied password")
    print("please inter correct password")
else:
    print("Inavlied user name and password")    



'''Write a program that calculates electricity bill according to units:

First 100 units → Rs 5 per unit
Next 100 units → Rs 10 per unit
Above 200 units → Rs 15 per unit

User se units input lo aur total bill calculate karo.

Concepts:

if-elif-else
arithmetic operators'''
 
   
#3rd attemed
unit=int(input("enter your unit:"))
if(unit<=100):
    bill=unit*5
elif(unit<=200):
    bill=(100*5)+(unit-100)*10
else:
    bill=(100*5)+(200*10)+(unit-200)*15
print("Your bill",bill)    


'''User se age lo aur category print karo:

Age 0–12 → Child
Age 13–19 → Teenager
Age 20–59 → Adult
Age 60+ → Senior Citizen

Concepts:

if-elif-else
comparison operators'''
age=int(input("Enter your age:"))
if(age<=12):
    print("child")
elif(age<=19):
    print("Teenager")
elif(age<=25):
    print("adult") 
else:
    print("senior citizen")

'''Ek shopping store ka program banao:

User se total shopping amount lo.

Rules:

Amount 5000 ya zyada → 20% discount
Amount 3000 ya zyada → 10% discount
Amount 1000 ya zyada → 5% discount
Warna koi discount nahi

Final price calculate karo.

Concepts:

if-elif-else
arithmetic operators'''
#first attemp 
user=int(input("ENTER YOUR amount:"))
if(user>=5000):
    dis=user*20/100
elif(user>=3000):
    dis=user*10/100
elif(user>=1000):
    dis=user*5/5
# print(dis)

#correct code 
amount=int(input("Enter your amount:"))
if(amount>=5000):
    dis=amount*20/100
elif(amount>=3000):
    dis=amount*10/100    
elif(amount>=1000):
    dis=amount*5/100
else:
    dis=0
print("Discount amount:",dis)    
final_price=amount-dis
print("final price:",final_price)        
    
