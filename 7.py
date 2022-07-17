n=int(input("enter a number: "))

a=[]
i=1
while(i<=n/2):
    if(((n%i)==0)):
        a.append(i)
    i+=1
print("divisors of ",n," are ",a)