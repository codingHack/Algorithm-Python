def addEdge(u,v):
    graph[u].append(v)
    indegree[v]+=1

def toporogicalSort():
    for i in range(1,V+1):
        if indegree[i]==0:
            queue.append(i)

    for i in range(V):
        if not queue:
            print('has cycle')
            return False
        print(queue)
        cur=queue.pop(0)
        result.append(cur)
        for j in graph[cur]:
            indegree[j]-=1
            if indegree[j]==0:
                queue.append(j)
                
    return True

V=6
graph=[[] for i in range(V+1)]
indegree=[0 for i in range(V+1)]
result=[]
queue=[]

addEdge(1,3)
addEdge(3,5)
addEdge(1,4)
addEdge(4,6)
addEdge(2,4)
addEdge(2,6)
toporogicalSort()
print(result)
