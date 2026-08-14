'''write a python program using funtion to convert celsuis to fahrenhght'''

def celsuis_to_fahrenhght(celsuis):
    celsuis_to_fahrenhght=(celsuis*9/5)+32  #formula (C*9/5)+32
    return celsuis_to_fahrenhght
c=int(input("Enter your temarature: "))
print(f"{c}C={celsuis_to_fahrenhght(c)}F")


print("......................Next........................")

'''Write a function to convert Fahrenheit to Celsius.'''
def fahrenhght_to_celsuis(fahrenhght):
    fahrenhght_to_celsuis=(fahrenhght-32)*5/9   #formula    fahrenhght_to_celsuis=(fahrenhght-32)*5/9
    return fahrenhght_to_celsuis
f=68
print(f"{f}C={fahrenhght_to_celsuis(f)}F")


print("......................Next........................")



'''Write a function that takes 3 numbers and returns their average.'''
def avg(a,b,c):
    avg=(a+b+c)/3
    return avg
print(f"Three nuber average:{avg(10,20,30)}")




print("......................Next........................")




'''Write a function that takes a number and returns whether it is even or odd.'''
n=int(input("Enter your numebr:"))
def num(n):
    if (n%2==0):
        return 'even'
    else:
        return 'odd'
print(f"{n} is {num(n)} number")






print("......................Next........................")



'''Write a function that takes Celsius temperature and tells:;

Below 0°C → "Freezing"
0°C to 30°C → "Normal"
Above 30°C → "Hot"'''

def celsuis(temperature):
    if (temperature<0):
        return "freezing"
    elif temperature<=30:
        return "Normal"
    else:
        return "Hot"
temperature=int(input("Enter your Temperature:"))
print(f"your Temperaute {temperature} is {celsuis(temperature)}")    