n=int(input("enter no. of numbers :"))
a=[]
for i in range(n):
    b=int(input("enter a number: "))
    a.append(b)
print("max. is ",max(a)," min. is ",min(a))