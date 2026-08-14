''''write a recursive function to calculate the sum first n natural number'''
def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)
n=int(input("ente ryour number:"))
print(f"First {n} natural number {sum(n)}")



def sum(n):
    if n==1:
        return 1
    return sum(n-1)+n 
n=int(input("enter your number:"))
print(f"{n} ka sum ho ga {sum(n)}")



print("...............next...................")




'''Write a recursive function to calculate the factorial of a number n.'''
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n - 1)
n=int(input("Enter your number:"))
print(f"{n} of a  Factorial {factorial(n)}")



print("...............next...................")


'''Write a recursive function that prints numbers from n down to 1.'''
def number(n):
    if n==0 or n==1:
        return 1
    return number(n-1)
n=int(input("enter your number:"))
print(number(n))


def number(n):
    if n == 0:
        return

    print(n)
    number(n - 1)


n = int(input("Enter your number: "))
number(n)


