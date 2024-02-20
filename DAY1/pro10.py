s,c=map(int,input().split())
if c>=s:
    np=0
else:
    count=s-c
    if c%4==0:
        np=count//4
    else:
        np=(count//4)+1
print(np)
