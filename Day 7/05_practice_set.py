# '''write a program to calculate the factorial of a given number using loop'''

# num=int(input("enter your number:"))
# factorial=1
# for i in range(1,num+1):
#     factorial=factorial*i
# print(f"the factorail {num} is {factorial}")    


# '''while loop use karke 1 se 20 tak numbers ka sum nikalo.'''
# i=1
# sum=0
# while(i<=20):
#     i+=1
#     sum+=i
# print(sum)    


# '''User se ek number n lo aur 1 se n tak numbers ka product (multiplication)
#  calculate karo using for loop.'''
# n=int(input("enter your num:"))
# multi=1
# for i in range(1,n+1):
#     multi=multi*i
# print(f'calculate {n} ka multiplication {multi}')


# '''User se n lo aur 1 se n tak sirf EVEN numbers ko multiply karo.'''
# n=int(input("enter your num:"))
# multi=1
# for i in range(1,n+1):
#     if i%2==0:
#         multi=multi*i
# print(f"1 sa {n} tak go even number {multi}")        



# '''User se n lo aur n se 1 tak reverse order mein multiplication karo.'''
# n=int(input("enter your number:"))
# pro=1
# for i in range(n,0,-1):
#     pro=pro*i
# print(pro)


# '''User se n lo aur 1 se n tak sirf ODD numbers ka product calculate karo using for loop.'''
# n=int(input("enter your number:"))
# pro=1
# for i in range(1,n+1):
#     if i%2 !=0:
#         pro=pro*i
#     print(pro)        





# '''User se n lo aur 1 se n tak sirf un numbers ka product nikalo jo 3 se completely divide 
# hote hain, 
# lekin 5 se divide nahi hote.'''
# n=int(input("enter your number:"))
# pro=1
# for i in range(1,n+1):
#     if i%3==0:
#         pro=pro*i
#         print(pro)


'''1 se 20 tak sirf EVEN numbers ka sum nikalna hai.'''
sum=0
for i in range(1,21):
    if i%2==0:
        sum=sum+i
    print(f"{i}+{sum}")        



'''User se n lo aur 1 se n tak sirf un numbers ka sum nikalo jo:

2 se completely divide hote hon
3 se completely divide na hote hon'''
n=int(input("enter your number:"))
devid=0
for i in range(1,n+1):
    if i%2==0 and i%3!=0:
        devid=devid+i
print(devid)        
