'''write a program to count the number in the following tuple'''
num=(7,0,8,0,0,0,9)
n=num.count(0)
print(n)


'''Write a Python program to create a tuple of student marks and display:

All marks
Total marks
Average marks
Highest marks
Lowest marks'''
marks=(32,34,56,23,45,67)
print("All Marks:",marks)
total=sum(marks)
print("Total marks:",total)
averg=total/len(marks)
print("Averg marks:",averg)
print("Higest marks:",max(marks))
print("Lowest marks:",min(max))
