'''create an empty dictonory allow 4 friends to enter their favourite languae as value 
and use key as their name assume that the names are unique '''
friends={}
name=input("enter your name:")
language=input("enter your language:")
friends[name]=language
name=input("enter your name:")
language=input("enter your language:")
friends[name]=language
name=input("enter your name:")
language=input("enter your language:")
friends[name]=language
name=input("enter your name:")
language=input("enter your language:")
friends[name]=language
name=input("enter your name:")
language=input("enter your language:")
friends[name]=language
print(friends)


'''Create a student record system using a dictionary.

Requirements:

Student name as key
Store marks as value
Allow user to enter 5 students
Display all students with their marks'''
record={}
name=input("ENTER YOUR STUDENT NAME:")
marks=input("ENTER YOUR STUDENT MARK")
record.update({name:marks})
name=input("ENTER YOUR STUDENT NAME:")
marks=input("ENTER YOUR STUDENT MARK")
record.update({name:marks})
name=input("ENTER YOUR STUDENT NAME:")
marks=input("ENTER YOUR STUDENT MARK")
record.update({name:marks})
name=input("ENTER YOUR STUDENT NAME:")
marks=input("ENTER YOUR STUDENT MARK")
record.update({name:marks})
name=input("ENTER YOUR STUDENT NAME:")
marks=input("ENTER YOUR STUDENT MARK")
record.update({name:marks})
print(record)


