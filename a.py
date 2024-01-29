for i in range(int(input())):
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    m,n=map(int,input().split())
    e=[[c+a,d+b],[c+a,d-b],[c-a,d+b],[c-a,d-b]]
    j=0
    while j<len(e):
        x=e[j]
        if (abs(m-x[0])==a and abs(n-x[1])==b) or (abs(m-x[0])==b and abs(n-x[1])==a):
            t=1
            j+=1
        else:
            e.pop(j)
    print(len(e))