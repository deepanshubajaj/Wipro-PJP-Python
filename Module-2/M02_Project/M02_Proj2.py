a=[]
n=int(input("Enter number of scores:"))
for i in range(1,n+1):
    b=int(input("Enter score: "))
    a.append(b)
dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
uniq_items.sort()
print("Runner up Score is:",uniq_items[len(uniq_items)-2])
