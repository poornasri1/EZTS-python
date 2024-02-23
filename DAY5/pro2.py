'''n=int(input())
d={}
for i in range(n):
    k,v=map(str,input().split())
    d[k]=v
m=int(input("no.of search items"))
for i in range(m):
    s=input()
    if s in d:
        print(s,d[s])
    else:
        print("not found")
    
3
sam 45678
tom 98765
harry 5678765
no.of search items3
sam
sam 45678
sri
not found
poorna
not found'''
