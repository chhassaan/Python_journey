'''Write a python program to display a user enterd name followed by good 
afternon using input function'''
name=input("enter the name:")
print(f"Dear {name} Good afternoon")

'''Write a Python program to take user's:

Name
Age
City

and display the information in a proper sentence.'''
name="Hassaan"
age=21
city="Chiniot"
print(f"Name:{name}\nAge:{age}\nCity:{city}")

'''Write a Python program that takes two numbers from the user and displays:

Addition
Subtraction
Multiplication
Division'''
first_number=int(input("Enter the number:"))
sec_number=int(input("Enter the number:"))
print(f"Addition:{first_number+sec_number}")
print(f"Subtraction:{first_number-sec_number}")
print(f"Multiplaction:{first_number*sec_number}")
print(f"Division:{first_number/sec_number}")

'''Write a Python program that takes marks of three subjects from the user and displays:

Total marks
Average marks'''
eng_marks=int(input("enter the number:"))
math_marks=int(input("enter the number:"))
science_marks=int(input("enter the number:"))
total_marks=(eng_marks+math_marks+science_marks)
print("Total marks:",total_marks)
print("Average marks:",total_marks/3)
