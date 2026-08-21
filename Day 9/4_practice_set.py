'''a file contains a word donkey multiple time you need to write a program which replace this 
word with by updating the same file '''
with open("donkey.txt")as f:
    text=f.read()
    text=text.replace("donkey","hourse")
with open("donkey.txt","w")as f:
    f.write(text)



with open("donkey.txt")as f:
    test=f.read()
    test=test.replace("hourse","donkey")
with open("donkey.txt","w")as f:
    f.write(test)        




'''repeat program 4 for a list of such words to be conserd'''
word=["donkey","ganda","bad"]
with open("donkey.txt","r") as f:
    contant=f.read()
    for i in word:
        contant=contant.replace(i,"acha")

    with open("donkey.txt","w")as f:
        f.write(contant)
        