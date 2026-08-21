str='ali is  a goood bboy'
with open("this_file.txt","w") as m:
    m.write(str)



with open("this_file.txt","r") as f:
    print(f.read())



with open("this_file.txt","a") as f:
    f.write("    hassan is a bad boy")