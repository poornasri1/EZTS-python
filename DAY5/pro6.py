'''l,d=map(int,input().split())
lst=list(map(int,input().split()))
flag=0
for i in lst:
    for j in lst:
        if j-i==d:
            flag=1

if flag==1:            
    print("True")

else:
    print("False")
    
    
5 60
1 20 40 100 80
True'''




'''l,d=map(int,input().split())
lst=list(map(int,input().split()))
flag=0
for i in lst:
    for j in lst:
        if j-i==d:
            flag=1
x=True if flag==1 else False
print(x)'''
