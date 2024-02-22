# strong number using recursion
'''def fact(n):
    if n<1:
        return 1
    else:
        return n*fact(n-1)
def strong(x):
    s=str(x)
    sum=0
    for i in s:
        sum+=fact(int(i))
    if sum==x:
        return "strong"
    else:
        return "not strong"
x=int(input())
print(strong(x))'''
    



'''145
strong'''

def fact(n):
    if n<1:
        return 1
    else:
        return n*fact(n-1)
def strong(x):
    s=str(x)
    sum=0
    for i in s:
        sum+=fact(int(i))
    if sum==x:
        print(x)
a,b=int(input()),int(input())
for i in range(a,b+1):
    strong(i)

    
