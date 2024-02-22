# To print the smallest vowel repeating odd number of times in the given string
'''s=input()
s1=""
for i in s:
    if i  in  "aeiouAE0IOU":
        if s.count(i)%2!=0:
            s1+=i
print(min(s1))'''


'''s=input()
s1=""
for i in s:
    if i not in  "aeiouAE0IOU":
        if s.count(i)%2!=0:
            s1+=i
print(min(s1))'''
