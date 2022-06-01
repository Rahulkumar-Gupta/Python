'''n=int(input("Enter Number :"))
for i in range(0,n):
    for j in range(0,n):
        print("*",end=" ")
    print()
    ****
    ****
    ****
    ****
    '''
'''
n=int(input("Enter Number :"))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
    *
    **
    ***
    ****
    '''
'''
n=int(input("Enter Number :"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
1 2 3 4 5 6 7
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10 11
1 2 3 4 5 6 7 8 9 10 11 12
'''
'''
num=int(input("Enter Row Range "))
n=int(input("Enter start Point"))
for i in range(0,num):
    for j in range(i+1):
        print(n,end=" ")
        n=n+1
    print()
'''
n=int(input("Enter Number"))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()

