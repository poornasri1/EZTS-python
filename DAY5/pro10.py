# average of each student marks using nested dict
'''n,m=map(int,input().split())
d={}
for i in range(n):
    k=input()
    v={}
    sum=0
    for i in range(m):
        k1=input()
        v1=int(input())
        v[k1]=v1
        sum+=v1
    d[k]=v  
print(sum/m) 
1 2
90
m1
3
m2
3
3.0'''
n,m=map(int,input().split())
d={}
for i in range(n):
    k=input()
    v={}
    for i in range(m):
        k1=input()
        v1=int(input())
        v[k1]=v1
    d[k]=v
for i in d:
    l=list(d[i].values())
    print(f"{i}:{sum(l)/m}")
        
