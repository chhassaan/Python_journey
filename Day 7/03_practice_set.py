'''write a program to find whether a given number is prime or not'''
num=int(input("enter your number:"))
for i in range(2,num):
    if (num%i)==0:
        print("number is not a prime")
        break
else:
    print("numer is prime") 






for num in range (2,101):
    for i in range(2,num):
        if (num%i)==0:
            break
    else:
        print(num)
            




for num in range (2,101):
    for i in range(2,num):
        if (num%i)==0:
            if(num)>10:
                break
    else:
        print(num)        
            




for i in range(2,21):
    if i % 3==0:
        print(i)



for num in range(1,30):
    if num % 3==0:
        print(num)





'''1 se 20 tak numbers print karo aur har number ke saath batao ke wo Even hai ya Odd.'''
for num in range(1,20):
    if num % 2==0:
        print("even number:",num)
    else:
        print("odd number:",num)    




for num in range(1,30):
    if num%2==0:
        print("even number:",num)





for num in range(1,30):
    if num%2 !=0:
        print("even number:",num)





'''1 se 50 tak numbers check karo:

Agar number 3 se divide hota ho → "Fizz" print karo
Agar number 5 se divide hota ho → "Buzz" print karo
Agar number 3 aur 5 dono se divide hota ho → "FizzBuzz" print karo
Baqi numbers ko print mat karo.'''
for num in range(1,51):
      if num%3==0 and num%5==0:
            print("Fizz and buzzz",num)
      elif num%3==0:
        print('fizz',num)
      elif num%5==0:
        print("buzz",num) 





'''1 se 100 tak numbers check karo:

Agar number 2 aur 3 dono se divide hota ho → "Both" print karo.
Agar sirf 2 se divide hota ho → "2" print karo.
Agar sirf 3 se divide hota ho → "3" print karo.
Baqi numbers print mat karo.'''
for i in range(1,100):
    if i%2==0 and i%3==0:
        print("Both",i)
    elif i%2==0:
        print("2",i)
    elif i%3==0:
        print("3",i)        




'''1 se 100 tak numbers check karo:

Agar number 2 aur 3 dono se divide hota ho → Even + Divisible by 3
Agar number sirf 2 se divide hota ho → Even
Agar number sirf 3 se divide hota ho → Divisible by 3
Agar number na 2 se divide ho na 3 se → Other'''
for i in range(1,100):
    if i%2==0 and i%3==0:
        print("even + devisible by 3:",i)
    elif i%2==0:
        print("even",i)
    elif i%3==0:
        print("divible by 3:",i) 
    else:
        print("Other")   

  