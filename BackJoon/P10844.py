import sys
N=int(sys.stdin.readline())
print(N)
DP=[0 for i in range(N+1)]
DP[1]=9
stack=[1,2,3,4,5,6,7,8,9]

for i in range(2,N+1):
    newstack=[]
    #stack을 돌면서 %10 을 했을때
    for num in stack:
        nam=num%10
        #0인 경우 1만 어펜드
        if nam==0:
            newstack.append(num*10+1)
        #9인 경우 8만 어펜드
        elif nam==9:
            newstack.append(num*10+8)
        #나머지 경우 -1, +1 어펜드
        else:
            newstack.append(num*10+(nam-1))
            newstack.append(num*10+(nam+1))
    DP[i]=len(newstack)
    stack=newstack

print(DP[N]%1000000000)











