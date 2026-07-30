



# '''Write a Python program to take 5 numbers from the user, store them in a list, and display:

# The list
# The largest number
# The smallest number'''
# num=[]
# first=int(input("enter the number"))
# num.append(first)
# sec=int(input("enter the number"))
# num.append(sec)
# third=int(input("enter the number"))
# num.append(third)
# fourth=int(input("enter the number"))
# num.append(fourth)
# fifth=int(input("enter the number"))
# num.append(fifth)
# print("The list:",num)
# print("THe Largest number:",max(num))
# print("The Smallest number:",min(num))



'''Q2

Write a Python program to create a list of 6 numbers and:

Sort the list
Remove the last number
Print the updated list'''
list=[23,45,67,89,34,56]
list.sort()
print("sorted list",list)
list.pop()
print("removed last num:",list)
print("updated list",list)

'''Write a Python program to take 5 student marks from the user, store them in a list, and display:

All marks       list
Total marks      sum
Average marks    /6
Highest marks'''#max
marks=[]
first_stu=int(input("Enter the number:"))
marks.append(first_stu)
sec_stu=int(input("Enter the number:"))
marks.append(sec_stu)
third_stu=int(input("Enter the number:"))
marks.append(third_stu)
fourth_stu=int(input("Enter the number:"))
marks.append(fourth_stu)
fifth_stu=int(input("Enter the number:"))
marks.append(fifth_stu)
six_stu=int(input("Enter the number:"))
marks.append(six_stu)
print("All marks:",marks)
total_marks=sum(marks)
print("Total Marks:",total_marks)
print("Higest marks:",max(marks))
aver=total_marks/6
print("Average marks:",aver)