'''write a program to find out whether a student has passed or 
fail if it requries
a total of 40% and at least 33% in each subject to pass assume 3 subject and 
take marks and an input from the user
'''
#first attempt 
first_subject=int(input("entr your first marks:"))
secound_subject=int(input("enter your secound marks:"))
third_subject=int(input('enter your third marks:'))

marks=(first_subject+secound_subject+third_subject)/3
    
if(first_subject<33):
    print("Fail first subject:",first_subject)
elif(secound_subject<33):
    print("Fail secound subject:",secound_subject)  
elif(third_subject<33):  
    print("Fail third subject:",third_subject) 
elif(marks<40):
    print("fail ")
else:
    print("pass all subjects")        
print("persantage:",marks,"%")

#secound attempt
first_subject=int(input("entr your first marks:"))
secound_subject=int(input("enter your secound marks:"))
third_subject=int(input('enter your third marks:'))
persantage=(first_subject+secound_subject+third_subject)/3
if(first_subject<33 and
   secound_subject<33 and
   third_subject<33 and
   persantage<40):
    print("congratulation you passed")
else:
    print("sorry you fail!")
print("Total persantage",round(persantage),"%")      






'''Ek program banao jo student ke 3 subjects ke marks user se le.

Rules:
Pehle check karo:

Agar kisi bhi subject mein 33 se kam marks hain:

Print:
Fail (You have failed in a subject)
Agar har subject mein 33 ya zyada marks hain, to percentage calculate karo.

Phir percentage ke hisaab se grade do:

Percentage 90 ya above → Grade A
Percentage 80 se 89 → Grade B
Percentage 70 se 79 → Grade C
Percentage 60 se 69 → Grade D
Percentage 40 se 59 → Pass
Percentage 40 se kam → Fail'''
first=int(input("ENTER YOUR first MARKS:"))
secound=int(input("ENTER YOUR secound MARKS:"))
third=int(input("ENTER YOUR  third MARKS:"))
marks=(first+secound+third)/3
if(first<33 or
   secound<33 or
   third<33
):
    print("sorry you Fail this exam")
elif(marks>=90):
    print("Grade A")
elif(marks>=80):
    print("Grade B")
elif(marks>=70):
    print("Grade C")
elif(marks>=60):
    print("Grade D")
elif(marks>=40):
    print("Pass")
else:
    print("Fail")
print("Total mark:",round(marks),"%")    
