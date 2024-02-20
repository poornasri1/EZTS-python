#strong number or not using functionss
#sum of a factorial of individual digits ex: 145
'''def strong(n):
    x,sum=n,0
    while n>0:
        digit=n%10
        fact=1
        for i in range(1,digit+1):
            fact*=i
        sum+=fact
        n//=10
    if sum==x:
        return"strong"  #print("strong)
    else:
        return"not a strong"  #print(:not a srong)
n=int(input())
print(strong(n))   #strong(n)'''



'''def strong(n,m):
    for i in range(n,m+1):
        x,sum=i,0
        while i>0:
            digit=i%10
            fact=1
            for j in range(1,digit+1):
                fact*=j
            sum+=fact
            i//=10
        if sum==x:
            print(x)
n,m=int(input()),int(input())
strong(n,m)'''

        
        
        
