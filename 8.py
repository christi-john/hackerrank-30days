# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

n=int(input())
d={}

for i in range(n):
    data = input().split(' ')
    d[data[0]] = data[1]
    
while True:
    try:
        query=input()
        if query in d:
            print(str(query) + "=" + str(d[query]))
        else:
            print('Not found')
    except:
        break   