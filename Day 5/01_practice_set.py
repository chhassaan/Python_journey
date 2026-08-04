'''write a python program to create a dictonary of hindi word with values are 
are their english translation provide user with an option to look it up'''
word={
    "pani":"water",
    "kursi":"chair",
    "mauz":"Table",
    "beli":"cat",
    "pankha":"fan"
}
search=input("enter your word:")
print("English meaning:",word.get(search,"Word not found"))


'''Create a dictionary of student names and their marks. 
Take a student name from the user and display the marks
. If the student does not exist, display "Student not found".'''

marks = {
    "Ali": 85,
    "Hassaan": 90,
    "Subhan": 78
}
search=input("Enter your name:")
print("Marks display:",marks.get(search,"Student not found"))

'''Create a dictionary of fruits and their prices. 
Take a fruit name from the user and display its price. 
If the fruit is not available, display "Fruit not found".'''
fruits={
    "Apple":300,
    "Mango":90,
    "Grapes":800,
    "banana":150
}
search=input("ENTER YOUR FRUITS NAME:")
print("Its price:",fruits.get(search,"Fruit not found"))


'''Create a dictionary of English words and their meanings. 
Allow the user to search for a word and display its meaning.'''
word={
    "Ma ga rha hoo":"I am going",
    "tum kr sakta hoo":"you do it",
    "kia kr rha hoo":"what happend"
}
search=input("ENTER YOUR SENTENCE:")
print("English word:",word.get(search,"word not found"))



'''Create a dictionary of 5 students with their ages. Take a student name from 
the user and display the student's age using the get() method.'''
student={
    "ali":20,
    "Hassaan":21,
    "Subhan":19
}
search=input("ENTER YOUR NAME:")
print("STUDENT AGE:",student.get(search,"Student not found"))

'''Create a phone book using a dictionary. Store names as keys and phone numbers as values. 
Ask the user for a name and display the phone number. 
If the name is not found, display "Contact not found".'''
phone_book={
    "Ali":"3057253248",
    "Subhan":"3287928974",
    "Hassaan":"3180641346"

}
search=input("ENTER YOUR NAME:")
print("THE PHONE NUMBER:",phone_book.get(search,"Contact not found"))

