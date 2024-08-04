def SumPrint(Dict):
      
    sum = 0
    for i in Dict:
        sum = sum + Dict[i]
      
    return sum
  
# Driver Function
dict = {'a': 100, 'b':200, 'c':300}
print("Sum :",SumPrint(dict))