'''write a program which findout whether a given name in present in a list or not'''
name=["hassaan","ali","subhan"]
pre=input("enter your name:").lower()
if pre in name:
    print("name is present")
else:
    print("name is not present")    

'''Write a program that takes a username from the user.
If the username is "admin", print "Welcome Admin".
Otherwise print "Access Denied".'''
name=input("enter your name: ").lower()
if (name=="admin"):
    print("welcome admin")
else:
    print("access denied")

'''Write a program that takes a mobile number from the user.
Check whether the mobile number contains exactly 11 characters or not.'''
numb=input("enter your number:")
if(len(numb)==11):
    print("mob number is vallied")
else:
    print("mob number is not vallied")    

'''Write a program that checks whether a given city name is present in the list or not.

cities = ["Lahore", "Karachi", "Islamabad", "Faisalabad"]'''

cities = ["lahore", "karachi", "islamabad", "faisalabad"]
name=input("enter your suggestion name:").lower()
if name in cities:
    print("your enter name is present in list")
else:
    print("your enter name is not a present in list")


'''Write a program that takes a password from the user.
If the password length is less than 8 characters,
print "Weak Password".
Otherwise print "Strong Password".'''
password=input("enter your password:")
if len(password)<8:
    print("weak password")
else:
    print("strong password")    

'''Write a program that takes a comment from the user.
If the comment contains any of these words:

"bad"
"hate"
"spam"

print "Blocked Comment"

Otherwise print "Allowed Comment".'''
comment=input("enter your comment:").lower()
if ("bad" in comment) or ("hate" in comment) or ("spam" in comment):
    print("Block comment")
else:
    print("Allowed comment")    


'''Write a program that takes marks from the user.

If marks are:
90 or above → Grade A
80 to 89 → Grade B
70 to 79 → Grade C
Below 70 → Fail'''
marks=int(input("enter your marks:"))
if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
elif marks>=70:
    print("Grade C")
else:
    print("Fail")