
num1=0
num2=1
initialRep=2
rep=int(input("number of repeatation:\n"))

print(num1)
print(num2)
while initialRep<=rep:
    num1=num1+num2
    temp=num1
    print(temp)
    num1=num2
    num2=temp
    initialRep+=1