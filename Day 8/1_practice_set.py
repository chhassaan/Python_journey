'''write a program using fumction to find greater of three number'''

def num(a,b,c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    else:
        return c
print(num(34,56,23)) 


print("...................Next...................")


  
'''Write a function that takes 3 numbers and returns the second largest number.'''
def num(a,b,c):
    if(a>b and a<c)or(a<b and a>c):
        return a
    elif (b>a and b<c)or(b<a and b>c):
        return b
    else:
        return c
print(num(10,50,30))    



print("...................Next...................")




def num(a,b):
    if (a>0 and b>0):
        return("both number is positive")
    else:
        return("bith number is neative")
print(num(30,-40))    



print("...................End...................")
