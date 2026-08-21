'''write a program to mine a log file and find out whether is contain "python"'''


with open("logfile.txt","r")as f:
    contant=f.read()
    if "python" in contant.lower():
        print("python is present")
    else:
        print("python is not present")    