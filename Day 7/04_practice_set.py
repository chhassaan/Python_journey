'''write a program to find the sum first natural numbers using while loop'''
n=int(input("enter your number:"))
i=1
sum=0
while(i<=n):

     sum+=i
     i+=1

print(sum)


'''Ek program banao jo while loop use karke 1 se n tak sirf un numbers ka sum nikale jo:

3 se completely divide hote hon
5 se completely divide na hote hon'''
n=int(input("enter your number:"))
i=1
while i<=n:
    if n%3==0 and n%5 !=0:
    
        print(n)
i+=1    


n=int(input("enter your number:"))
i=1
sum=0
while i<=n:
    if i%3==0 and i%5!=0:
        sum+=i
    i +=1
print(sum)
