# program to make encription and decription with a key value using functions
'''def fun(n):
    for i in n:
        ord(i)
        print(ord(i))
n=input()
fun(n)'''


def encryption(s,k):
    p=""
    for i in s:
        x=ord(i)+k
        p+=chr(x)
    print(p)
def decryption(s,k):
    p=""
    for i in s:
        x=ord(i)+k
        p+=chr(x)
    print(p)
k=int(input("enter key value:"))
s=input("enter string:")
op=input("enter the operation")
if op=="encryption":
    encryption(s,k)
elif op=="decryption":
    decryption(s,k)
else:
    print("improper operation")


    




'''enter key value:3
enter string:sri
enter the operationencryption
vul'''
