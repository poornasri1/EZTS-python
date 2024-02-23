n,m=map(int,input().split())
d={}
for i in range(n):
    k,v=map(str,input().split())
    d[k]=v
for i in range(m):
    k1,v1=map(str,input().split())
    for i in d:
        if d[i]==v1[:-1]:
            print(f"{k1} {v1} #{i}")
            
            


'''2 2
insta 1.1.1
sri 1.1.4.2
poorna 1.1.4.2;
snap 1.1.1;
poorna 1.1.4.2; #sri
snap 1.1.1; #insta'''
