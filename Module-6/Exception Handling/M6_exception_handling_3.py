try:
    fileptr=open(input('Enter filename: '))
    
except IOError:
    print("File not found!!")
else:
    print("File Opened and printing contents!")
    content = fileptr.read()
    print(content)
    fileptr.close()