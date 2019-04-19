building_num=int(input())
arr=[[0,0]]
[arr.append(list(map(lambda x:int(x),input().split()))) for _ in range(0,building_num)]

print(arr)
