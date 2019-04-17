stair_num=int(input())

score=[]
for i in range(0,stair_num):
    score.append(int(input()))

DP=[0]*(stair_num+1)

DP[0]=score[0]
DP[1]=score[0]+score[1]
DP[2]=max(DP[1]+score[2],DP[2]+score[2])

for i in range(3,stair_num+1):
    DP[i]=max(DP[i-1]+DP[i-3]+score[i],DP[i-2]+score[i])
print(DP)
