'''write a program to find out the ine number where python is present from ques 6'''
with open("logfile.txt","r")as f:
    lines=f.readlines()
    for i,lineno in enumerate(lines,start=1):
        if "python" in lineno.lower():
            print(f"python is here in line {i} and {lineno}")


            




