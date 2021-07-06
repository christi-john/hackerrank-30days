# https://www.hackerrank.com/challenges/30-review-loop/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
for i in range(0,T):
    S=str(input())
    S1=S2=""
    for j in range(0,len(S)):
        if j%2==0:
            S1+=S[j]
        else:
            S2+=S[j]
    print(S1+ " " +S2)