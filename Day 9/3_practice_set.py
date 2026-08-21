'''write a program to generate a multiplication table 2 to 20 and write it to the diffrenet files
.place these file in a folder for a 13 year old'''

def generatetable(n):
    table=""
    for i in range(1,11):
        table+=f"{n}x{i}={n*i}\n"
    with open(f"tables/table_{n}","w")as f:
        f.write(table)    




for i in range(2,21):
    generatetable(i)



def func():
    print("Hello hassaan")
func()    





def square(n):
    print(n**2)
square(5)


def count(n):
    for i in range(1,n+1):
        print(i)
count(90)


def fun(n):
    for i in range(1,11):
        print(f"{n}x{i}={n*i}")
fun(6)        



def table(n):
    table=""
    for i in range(1,11):
        table+=f"{n}x{i}={n*i}\n"
    print(table)
table(5)        




with open("hello.txt","w")as f:
    f.write("Hello hassaan\ni am learning python")



name="hello"
with open("name.txt","w")as f:
    f.write(name)




with open("number.txt","w")as f:
    for i in range(1,11):
        f.write(str(i)+"\n")

def table(n):
    table=""
    for i in range(1,11):
        table+=f"{n}x{i}={n*i}\n"
    with open (f"{n}_file.txt","w")as f:
        f.write(table)
for i in range(2,21):
            table(i)                



import os
os.mkdir("tables")
def table(n):

    table=""
    for i in range(1,11):
        table+=f"{n}x{i}={n*i}\n"

    with open(f"tables/{n}_file,txt","w")as f:
        f.write(table)

for i in range(2,21):
    table(i)        























import os
os.mkdir('tobl')  #ak tobl name ka folder create
def table(n): #ya ak function haa
    table=""
    for i in range(1,11):
        table+=f"{n}x{i}={n*i}\n"   #ya sara method table create krtaa haa

    with open(f"tobl/{n}_file_table.txt","w")as f:  #is method sa ham tobl folder ka andar table ki files ko create kr rha haa
        f.write(table)    

for i in range(2,21):  #is step sa ham 2 sa 20 tak file ko create kr rha haaa
    table(i)