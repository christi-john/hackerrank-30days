# https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem

for i in range(int(input())):
    n=int(input())
    if(n==1):
        print("Not prime")
        continue
    for j in range(2,int(n**(1/2))+1):
        if(n%j==0):
            print("Not prime")
            break
    else: print("Prime")