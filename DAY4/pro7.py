#sum of two matrixes
r,c=int(input()),int(input())
l1,l2,l3=[],[],[0]*r
for i in range(r):
    i3[i]=[0]*c
for i in range(r):#matrix 1
    l1.append (tuple(map(int,input().split())))
for i in range(r):#matrix 2 
    l2.append (tuple(map(int,input().split())))
for i in range(r):
    for j in range(c):
        l3[i][j]=l1[i][j]+l2[i][j]
for i in l3:
    print(i)
    
