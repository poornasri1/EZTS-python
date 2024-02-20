#program to print the numbers which are not divisible by 6, 7, 8 in t a givem range
'''n=int(input())
m=int(input())
for i in range(n,m+1):
    if i%6!=0 and i%7!=0 and i%8!=0:
        print(i)'''




n=int(input())
m=int(input())
i = n
while i<=m:
    if i%6!=0 and i%7!=0 and i%8!=0:
        print(i)
        i+=1
