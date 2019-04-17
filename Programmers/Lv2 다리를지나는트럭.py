def solution(bridge_length, weight, truck_weights):
    
    bridge_queue=[0] #현재 다리상황을 보여주는 큐
    bridge_weight=0  #현재 다리의 무게
    time=0           #걸리는 시간
    remove_time=[1]  #트럭이 나갈시간을 기록한 큐
    
    while True:
        #시간 1초 증가
        time+=1
        
        #트럭이 다리를 다 통과할시간이 되면 그 트럭을 뺌 
        if time==remove_time[0]:
            bridge_weight-=bridge_queue[0]
            del bridge_queue[0], remove_time[0]
        
        #종료조건 truck_weights에서 모두 나갔을 때 -> 여기에 다리길이를 더해야 마지막 트럭도통과
        if len(truck_weights)==0:
            break
        
        #하나 더 들어가도 여유 공간이 있으면 트럭을 다리에 올림
        if bridge_weight+truck_weights[0]<=weight: 
            bridge_queue.append(truck_weights[0])
            bridge_weight+=truck_weights[0]
            del truck_weights[0]
            remove_time.append(time+bridge_length)
     
    return time + bridge_length-1
    
    # 프로그래머스 - 다리를지나는 트럭  
    # https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3
