list_num=[1,2,-3,-10,50]
try:
    index=int(input('Enter index: '))
    if list_num[index]>0:
        print("Positive Number")
    else:
        print("Negative Number")
    
except:
    print("Error Exist! \n1) Index may not be a number or \n2) Array index does not exist !")

    