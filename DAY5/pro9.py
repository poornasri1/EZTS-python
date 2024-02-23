#student marks database using nested dict
'''n,m=map(int,input().split())
d={}
for i in range(n):
    k=input()
    v={}
    for i in range(m):
        k1=input()
        v1=input()
        v[k1]=v1
    d[k]=v  #for i in d:
print(d) #print(i,"=",d[i])
1 2
m1
2
m2
3
{'485': {'m1': '2', 'm2': '3'}}'''
'''n,m=map(int,input().split())
d={}
for i in range(n):
    k=input()
    v={}
    for i in range(m):
        k1=input()
        v1=input()
        v[k1]=v1
    d[k]=v  #for i in d:
print(d)
for i in d.items():
    print(i)



2 2
485
m1
3
m2
2
490
m1
5
m2
4
{'485': {'m1': '3', 'm2': '2'}, '490': {'m1': '5', 'm2': '4'}}
('485', {'m1': '3', 'm2': '2'})
('490', {'m1': '5', 'm2': '4'})'''

