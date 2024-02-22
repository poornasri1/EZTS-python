#To print sum of the matrix( we cannot add nested list)
r,c=int(input()),int(input())
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
summ=0
for i in l:
    print(i)
    summ+=sum(i)
print(summ)
      
        







'''r,c=int(input()),int(input())
l=[]
for i in range(c):
    l.append(list(map(int,input().split())))
print(l)'''
'''2
2
1 2
1 2
[[1, 2], [1, 2]]'''



