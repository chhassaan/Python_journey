def count(n):
    if n == 0:
        return
    print(n)
    count(n - 1)

count(5)



def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print(factorial(5))

n=int(input("enter your number:"))
def fact(n):
    
    if (n==0 or n==1):
        return 1
    return n*fact (n-1)
print(f"{n} ka factorial:{fact(n)}")