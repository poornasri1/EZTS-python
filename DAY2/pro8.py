#To print amstrong number in a range using functions
def fun(n,m):
    for i in range(n,m+1):#100-1001
        sum=0
        x=i#101
        while i>0:
            temp=i%10
            sum+=temp**3
            i//=10
        if sum==x:#1==100
            print(x)
n,m=int(input()),int(input())#100-1000
fun(n,m)
