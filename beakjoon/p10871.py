import sys
a,b =map(int,sys.stdin.readline().split())#a 수열갯수 ,b 는 기준값
numlist= list(int(input().split()))
resultlist=[]
for i in range(a):
    if numlist[i]<b:
        resultlist.append(numlist[i])
print(' '.join(resultlist))
