#to print word count of vowels,list of the vowels in each word of a sentences using functions
def counting(s):
    print(s)
    s1,vc='',0
    for i in s:
        if i in "AEIOUaeiou":
            vc+=1
            s1+=i
    print(vc)
    print(list(set(s1)))
l=input().split()
for i in l:
    counting(i)
        






Pragati
3
['i', 'a']
Engineering
5
['i', 'e', 'E']
College
3
['o', 'e']























    












































     #input:Pragati Engineering college
