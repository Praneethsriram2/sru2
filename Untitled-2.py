"""
    1
   1 2
  1   3
 1     4
1 2 3 4 5
"""
n=int(input())
start,end=n-1,n-1
for i in range(n-1):
    num=0
    for j in range(2*n-1):
        if j==start:
            print(num+1,end='')
        elif j==end:
            print(num+1+i,end='')
        else:
            print(" ",end='')
    start-=1
    end+=1
    print()
for i in range(1,n+1):
    print(i,end='')
    if i!=n:
        print(' ',end='')
