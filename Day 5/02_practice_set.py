'''write a program to input eight numbers from the user and display all the 
unique numbers '''
s=set()
a=int(input("enter the number"))
s.add(a)
b=int(input("enter the number"))
s.add(b)
c=int(input("enter the number"))
s.add(c)
d=int(input("enter the number"))
s.add(d)
e=int(input("enter the number"))
s.add(e)
f=int(input("enter the number"))
s.add(f)
g=int(input("enter the number"))
s.add(g)
h=int(input("enter the number"))
s.add(h)
print(s)


'''Write a Python program to input 6 numbers from the user and 
display only the unique numbers using a set.'''
s=set()
a=int(input("ente your number:"))
s.add(a)
b=int(input("ente your number:"))
s.add(b)
c=int(input("ente your number:"))
s.add(c)
d=int(input("ente your number:"))
s.add(d)
e=int(input("ente your number:"))
s.add(e)
f=int(input("ente your number:"))
s.add(f)
print(s)

'''Write a Python program to create a dictionary of 5 products and their prices. 
Ask the user for a product name and display its price. 
If the product is not available, display 
"Product not found".'''
product={
    "fan":450,
    "chair":564,
    "cap":345,
    "cable":234,
    "table":234
}
search=input("enter your product:")
print(product[search])


'''Write a Python program to create two sets of numbers and display:

Union
Intersection'''
first_set={1,2,3,0,9,8}
sec_set={5,4,3,6,7,8}
print(first_set.union(sec_set))
print(first_set.intersection(sec_set))


