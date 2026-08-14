n=int(input("enter your number:"))
for i in range(1,n+1):
    print(" *"*i)
    print("* "*i)



for i in range(1,6):
    print(" "*(5-i)+"*"*i)


n=int(input("enter your number:"))
for i in range(1,n+1):
    print(" "*(5-i)+"*"*(2*i-1))


n=int(input("enter your number:"))
for i in range(1,n+1):
    print(" "*(5-i),end="")
    print("*"*(2*i-1),end="")
    print()
    


n=int(input("enter your nuumber:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")


n=int(input("enter your number:"))
for i in range(1,n+1):
    print("*"*i)



n=int(input("enter the number:"))
for i in range(1,n+1):
    print('*'*n,end="")
    print(" ")




n=int(input("enter your number:"))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")            



n=int(input("enter your num:"))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" ",end="")
        print("*",end="")
    print("")        



n=int(input("enter your number:"))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    elif(i==2 or i==n):
         print("*",end="")
         print(" ",end="")
         print(" ",end="")
         print(" ",end="")
         print("*",end="")  
    elif(i==3 or i==n):     
        print("*",end="")
        print(" ",end="")
        print(" ",end="")
        print(" ",end="")
        print("*",end="")
    else:      
        print("*",end="")
        print(" ",end="")
        print(" ",end="")
        print(" ",end="")
        print("*",end="")        
    print("")





n=int(input("enter your number:"))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*"+" "*(n-2)+"*",end="")
    print("")            