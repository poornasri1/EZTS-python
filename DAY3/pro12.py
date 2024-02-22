#to print the sum of odd numbers in a list
l,m=list(map(int,input().split()))
s=0
for i in range (l,m+1):
    if i%2!=0:
        s+=i
print(s)
