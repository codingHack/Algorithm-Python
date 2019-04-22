N=int(input())
for _ in range(N):
    arr=list(map(lambda x:int(x),input().split()))
    num=arr[0]-arr[1]
    x=2-num
    print(x)
