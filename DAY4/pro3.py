# To print the product of the matrix(using Append)
'''r,c=int(input()),int(input())
l=[]
for i in range(c):
    l.append(list(map(int,input().split())))
    product=1
for i in l:
    print(i)
    for j in i:
        product*=j
print(product)'''
    
'''3
3
1 2 3 
4 5 6
7 8 9
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
362880'''
#without append
r,c=int(input()),int(input())
l=[0]*c
for i in range(c):
    l[i]=list(map(int,input().split()))
    product=1
for i in l:
    print(i)
    for j in i:
        product*=j
print(product)
    
