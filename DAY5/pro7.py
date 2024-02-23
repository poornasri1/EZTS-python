'''s=input()
for i in s:
    if s.count(i)>1:
        print(i)
        break
else:
    print(".")
poorna
o

sri
.'''


#functions
def count(s):
    for i in s:
        if s.count(i)>1:
            print(i)
            break
    else:
        print(".")
n=input()
count(n)
