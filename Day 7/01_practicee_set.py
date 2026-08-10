'''write a program to print multiplication  table of a given number using for loop'''
num=int(input("Enter your number:"))
for i in range(1,11):
    num*i
    print(num,"x",i,"=",num*i)




num=int(input("enter your number:"))
for i in range(1,11):
    if i==num*3:
        continue
    print(num,"x",i,"=",num*i)




'''User se ek number lo. Us number ka 1 se 10 tak table banao.
 Lekin table mein se sirf woh results 
print karo jo 3 se completely divide ho jaate hain.'''
nummber=int(input("enter your number"))
for i in range(1,11):
    multi=nummber*i
    if multi%3==0:
        print(multi)



num=int(input("enter your num:"))
i=1
while(i<11):
    print(num,"x",i,"=",num*i)
    i+=1





'''User se ek number lo. Us number ka 1 se 10 tak table banao.
 Lekin table mein se sirf woh results 
print karo jo 3 se completely divide ho jaate hain.'''
num=int(input("enter your num:"))
i=1
while(i<11):
    multi=num*i
    i+=1
    if multi%3==0:
        print(multi)
        

    
