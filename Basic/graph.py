def dfsAndBfs(start,a): #1은 dfs 2는 bfs
    if a==1:
        print('start ',start,' dfs')
    else:
        print('start ',start,' bfs')
    stackOrQueue=[start]
    visited=[False for i in range(N+1)]
    result=[]
    while stackOrQueue:
        if a==1: #dfs
            v=stackOrQueue.pop()
        else:
            v=stackOrQueue.pop(0)
        visited[v]=True
        result.append(v)
        for i in graph[v]:
            if not visited[i] and i not in stackOrQueue:
                stackOrQueue.append(i)
    print(result)
    print('------------')

N=13
graph=[[] for i in range(N+1)]

#  1 - 2 - 3 - 10 - 11 - 12
#  |   |
#  4 - 5 - 6 - 7
#      |       |   
#      8       9  - 13
"""
13
1 2
2 3
3 10
10 11
11 12
1 4
2 5
4 5
5 6
6 7
5 8
7 9
9 13
"""
v=int(input())
for i in range(v):
    arr=list(map(lambda x:int(x),input().split()))
    graph[arr[0]].append(arr[1])
    graph[arr[1]].append(arr[0])



dfsAndBfs(1,1)
dfsAndBfs(1,2)
dfsAndBfs(9,1)
dfsAndBfs(9,2)




