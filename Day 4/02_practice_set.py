# '''Write a program to accept marks of 6 student and display than in a sorted manner'''
# list=[]  #empty list
# first_student=int(input("Enter marks:"))
# list.append(first_student)   #take 6 marks from a user
# sec_student=int(input("Enter marks:"))
# list.append(sec_student)
# third_student=int(input("Enter marks:"))
# list.append(third_student)
# fourth_student=int(input("Enter marks:"))
# list.append(fourth_student)
# five_student=int(input("Enter marks:"))
# list.append(five_student)
# six_student=int(input("Enter marks:"))
# list.append(six_student)
# list.sort()
# print(list)


# '''Write a Python program to take 5 numbers from the user, store them in a list,
#  and display the list in sorted order.

# Concepts: input(), append(), sort()'''
# list=[]  #empty list
# first_student=int(input("Enter marks:"))
# list.append(first_student)   #append ist ma add krna ka lya
# sec_student=int(input("Enter marks:"))
# list.append(sec_student)
# third_student=int(input("Enter marks:"))
# list.append(third_student)
# fourth_student=int(input("Enter marks:"))
# list.append(fourth_student)
# five_student=int(input("Enter marks:"))
# list.append(five_student)
# list.sort()
# print(list)

# '''Write a Python program to take 5 fruit names from the user,
#  store them in a list, and print the list. Then remove the last fruit using pop() and print the updated list.

# Concepts: append(), pop()'''
# list=[]
# first_fruit=input("enter you fruit:")
# list.append(first_fruit)
# sec_fruit=input("enter your fruit name:")
# list.append(sec_fruit)
# third_fruit=input("enter your fruit name:")
# list.append(third_fruit)
# four_fruit=input("enter your fruit name:")
# list.append(four_fruit)
# fiv_fruit=input("enter your fruit name:")
# list.append(fiv_fruit)
# list.pop()
# print(list)

'''Write a Python program to take 6 student marks from the user,
 store them in a list, sort the list, create a copy of the sorted list, and print both lists.

Concepts: append(), sort(), copy()'''

list=[]  #empty list
first_student=int(input("Enter marks:"))
list.append(first_student)   #take 6 marks from a user
sec_student=int(input("Enter marks:"))
list.append(sec_student)
third_student=int(input("Enter marks:"))
list.append(third_student)
fourth_student=int(input("Enter marks:"))
list.append(fourth_student)
five_student=int(input("Enter marks:"))
list.append(five_student)
list.sort()
print(list)
mew_list=list.copy()
print(mew_list)                                                                     