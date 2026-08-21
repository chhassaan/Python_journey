'''write a program to read the text from a given file "poem.txt" and find out whether 
it contain the word "twinkle" '''

with open("poem.txt")as f:
    text=f.read()
    if "twinkle" in text:
        print("yes the word twinkle is present")
    else:
        print("no the word twinkle not a present")    




with open("poem.txt")as f:
    text=f.read()
    count=text.lower().count("twinkle")
    print(count)


with open("poem.txt", "r") as f:
    for line_number,line in enumerate(f,start=1):
        if "twinkle" in line.lower():
            print("twinkle line",line_number,"mai ha")

























with open("ya_file.txt","r") as f:
    text=f.read()
    if "twinkle" in text:
        print("yes")
    else:
        print("no")




with open("ya_file.txt")as f:
    text=f.read()
    count=text.lower().count("twinkle")
    print("twinkle word is poem ma",count,"time") 

with open("ya_file.txt")as f:    
    for lines_numbers,line in enumerate(f,start=1):
        if "hassaan" in line.lower():
            print("hassan name  line ",lines_numbers,"main ha")
            