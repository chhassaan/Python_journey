'''write a python function to print first n line of the following pattren '''
def patren(n):
    for i in range(n,0,-1):
        print("*"*i)
        
n=3
patren(n)     


print("...............next.................")


'''Write a Python function to print the following pattern for n lines:'''
def patren(n):
    for i in range(1,n+1):
        print("*"*i)
n=int(input("enter your number:"))
patren(n)        



print("...............next.................")


def patren(n):
    if (n==0):
        return
    print("*"*n)
    patren(n-1)
n=int(input("enter your number:"))
patren(n) 

