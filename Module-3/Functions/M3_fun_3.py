def factorial(s):
    fact=1
    if s>=0:
        for i in range(1,s+1):
	        fact*= i 
        return fact
        
#Driver Main
s = int(input('Enter number: '))

print ("The number is : ",end="")
print (s)

print ("The factorial of a number is : ",end="")
print (factorial(s))
