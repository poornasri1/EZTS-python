#insert a number
s,d=map(str,input().split())
for i in range(len(s)):
    if int(s[i])<=int(d):
        print(s[:i]+d+s[i:])
        break
else:
    print(s+d)

32 4
432
