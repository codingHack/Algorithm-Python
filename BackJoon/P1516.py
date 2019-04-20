def countTime(num):
    if len(arr[num])==2:
        return arr[num][0]
    else:
        max=0
        for i in range(1,len(arr[num])-1):
            a=countTime(arr[num][i])
            if a>max:
                max=a
        return max+arr[num][0]

building_num=int(input())
arr=[[0,0]]
[arr.append(list(map(lambda x:int(x),input().split()))) for _ in range(0,building_num)]

for i in range(1,building_num+1):
    print(countTime(i))
