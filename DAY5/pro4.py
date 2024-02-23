
# to check the given string is anagram or not
s1=input()
s2=input()
if len(s1)==len(s2):
    if sorted(list(s1))==sorted(list(s2)):
        print("anagram")
    else:
        print("not")
else:
    print("not")
'''stop
post
anagram



stop
pose
not'''
