while True:
    wh=list(map(lambda x:int(x),input().split()))
    w=wh[0]
    h=wh[1]
    if (w+h)==0:
        break
    table=[]
    for _ in range(0,h):
        arr=list(map(lambda x:int(x),input().split()))
        table.append(arr)
    count=0
    for i in range(h):
        for j in range(w):
            if table[i][j]==1:
                
                stack=[[i,j]]
                while stack:
                    v=stack.pop()
                    table[v[0]][v[1]]=0
                    #up
                    if (v[0]-1)>=0:
                        area=[v[0]-1,v[1]]
                        if table[area[0]][area[1]]==1:
                            table[area[0]][area[1]]=0
                            stack.append(area)
                    #down
                    if (v[0]+1)<h:
                        area=[v[0]+1,v[1]]
                        if table[area[0]][area[1]]==1:
                            table[area[0]][area[1]]=0
                            stack.append(area)
                    #right
                    if (v[1]+1)<w:
                        area=[v[0],v[1]+1]
                        if table[area[0]][area[1]]==1:
                            table[area[0]][area[1]]=0
                            stack.append(area)
                    #left
                    if (v[1]-1)>=0:
                        area=[v[0],v[1]-1]
                        if table[area[0]][area[1]]==1:
                            table[area[0]][area[1]]=0
                            stack.append(area)

                    #1
                    if (v[0]-1)>=0 and (v[1]+1)<w:
                        area=[v[0]-1,v[1]+1]
                        if table[area[0]][area[1]]==1:
                            table[area[0]][area[1]]=0
                            stack.append(area)
                    #5
                    if (v[0]+1)<h and (v[1]+1)<w:
                        area=[v[0]+1,v[1]+1]
                        if table[area[0]][area[1]]==1:
                            table[area[0]][area[1]]=0
                            stack.append(area)
                    #7
                    if (v[0]+1)<h and (v[1]-1)>=0:
                        area=[v[0]+1,v[1]-1]
                        if table[area[0]][area[1]]==1:
                            table[area[0]][area[1]]=0
                            stack.append(area)
                    #11
                    if (v[0]-1)>=0 and (v[1]-1)>=0:
                        area=[v[0]-1,v[1]-1]
                        if table[area[0]][area[1]]==1:
                            table[area[0]][area[1]]=0
                            stack.append(area)  
                count+=1
    print(count)
