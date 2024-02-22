#sum of n natural numbers using recursiondef printing(n):
def printing(n):
    if n<1:
        return 1
    else:
        print(n)
        return n+printing(n-1)
n=int(input())
sum=printing(n)
print(sum)


'''10
10
9
8
7
6
5
4
3
2
1
56'''
