lst=[]
n=int(input("enter your numbers"))
for i in range(0,n):
    element=int(input())
    lst.append(element)
    lst.sort()
    a=lst[::-1]
    print(a)