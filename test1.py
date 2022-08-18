'''
#1
sum=0
for a in range(1,1000):
    if a%3==0 or a%5==0:
        sum=sum+a
print(sum)
'''
'''
#29
value=set()
for a in range(2,6):
    for b in range(2,6):
        value.add(a**b)
        sorted(value)
print(len(value))
'''

#34
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

def Checkfactorial(num):
    temp=num
    sum=0
    while temp!=0:
        reminder=temp%10 #reminder=145%10,reminder=5
        sum=sum+factorial(reminder)#pass reminder 5 in factorial function
        temp=temp//10#temp=145//10,temp=14
    if sum==num:
        return True
    
result=0
for i in range(3,100000):
    if Checkfactorial(i):
        result=result+i
print(result)




