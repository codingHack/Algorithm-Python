def countTime(num):
    if building_visited[num]:
        return 0
    else:
        building_visited[num]=True
        if len(arr[num])==2:
            return arr[num][0]
        else:
            count=0
            for i in range(1,len(arr[num])-1):
                count+=countTime(arr[num][i])
            print('add:',count)
            return arr[num][0]+count

building_num=int(input())
arr=[[0,0]]
building_visited=[False]*(building_num+1)
[arr.append(list(map(lambda x:int(x),input().split()))) for _ in range(0,building_num)]

for i in range(1,building_num+1):
    building_visited=[False]*(building_num+1)
    print(building_visited,countTime(i))
