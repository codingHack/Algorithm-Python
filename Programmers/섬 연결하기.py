def hasCycle(graph,cost):
    temp=dict(graph)
    #추가 되었다고 가정
    temp[cost[0]].append(cost[1])
    temp[cost[1]].append(cost[0])
    
    visited=[]

    #시작지점
    stack=[cost[0]]

    while stack:
        node=stack.pop()
        if node not in visited:
            visited.append(node)
            for i in temp[node]:
                if i not in visited:
                    stack.append(i)
        else:#사이클 존재
            return True
        
    return False    

def solution(n, costs):

    answer=0 #총 비용
    graph={} #현재 그래프

    #가중치 순으로 정렬
    costs=sorted(costs,key = lambda x:x[2])

    #graph에 노드 추가 
    for cost in costs:
        if cost[0] not in graph:
            graph[cost[0]]=[]
        if cost[1] not in graph:
            graph[cost[1]]=[]
    
    edge=0 #연결된 엣지 수
    for cost in costs:        
        #사이클이 없다면 edgs,비용 추기
        if not hasCycle(graph,cost):
            answer+=cost[2]
            edge+=1

        #노드-1 만큼 엣지가 있을 때 까지 반복
        if (len(graph)-1)==edge:
            break

    return answer

    

arr=[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(4,arr))
