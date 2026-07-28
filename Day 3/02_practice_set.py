'''write a program to fill in a letter templete given below with name and date
Dear<|name|>
you are selected!
<|date|>
'''
name=input("enter your name:")
date=input("enter your date:")
print(f"Dear<|{name}|>\n you are selected!\n<|{date}|>")

'''write a program to fill in a letter templete given below with name and date
letter=Dear<|name|>
you are selected!
<|date|>
'''
letter='''Dear<|name|>
you are selected!
<|date|>'''
print(letter.replace("name","Hassaan"),letter.replace("date","21"))


'''Write a Python program to generate a bill using product name and price.

Template:
Product: <product>
Price: <price>
Thank you for shopping!'''
product=input("enter the product name:")
price=input("enter your price:")
print(f"Product:<{product}>")
print(f"Price:<{price}>")
print("Thank you for shopping!")

'''Write a Python program to take customer name, units consumed, 
and price per unit from the user.
 Calculate the total electricity bill and display the bill details.'''
coutomer_name=input("enter your name:")
unit_consumed=int(input("enter total uunits connsumed:"))
price_per_unit=23
total_bill=unit_consumed*price_per_unit
print(f"Coustomer name:{coutomer_name}")
print(f"Total unit consumed:{unit_consumed}")
print(f"Total_bill:{total_bill}")

