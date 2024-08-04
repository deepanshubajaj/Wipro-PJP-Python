a = int(input("Enter number: "))  
sum=0
while a>0:
    sum+=a%10;
    a=a//10;
print(sum)