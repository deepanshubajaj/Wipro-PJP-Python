def ReturnString(string,n):
    new=""
    for i in range(n):
        new+=string
    return new

# Driver Code
string=input("Enter string:")
n=int(input('Enter the value of n: '))
count=0
if n>0 and n<=len(string):
    for i in string:
      count=count+1
    new=string[len(string)//2:len(string)]
print("Newly formed string is:")
print(ReturnString(new,n))