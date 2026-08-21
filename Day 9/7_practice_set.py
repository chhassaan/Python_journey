with open("number.txt","r")as f:
    contant=f.read()

with open ("number_copy.txt","w")as f:
    f.write(contant)    