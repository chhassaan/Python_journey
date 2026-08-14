'''write a python function which convert inches to cm'''
def inches_to_cms(inches):
    return inches*2.54
n=float(input("enter inches:"))
print(f'the crosponding value cms is {inches_to_cms(n)}')

print("..........next...............")

'''write a python function whicch convert cm to inches'''

def cm_to_inches(cm):
    return cm/2.54
n=float(input("enter your cm:"))
print(f"the crosponding inches is {cm_to_inches(n)}")