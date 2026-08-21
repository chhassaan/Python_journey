# f=open("my_file.txt")
# data=f.readline()
# print(data,type(data))
# data=f.readline()
# print(data)
# data=f.readline()
# print(data,type(data))
# data=f.readlines()
# print(data)
# f.close
f=open("my_file.txt")
line=f.readline()
while line != "":
    print(line,end="")
    line=f.readline()
f.close()    


