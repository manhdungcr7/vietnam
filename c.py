def s(n):
    m=bin(n)[2:]
    r=m.count("1")
    if r%2==0:
        return 0
    else:
        return 1
n,k=map(int,input().split())
c=[] 
for i in range(n-1,n+k-1):
    c.append(s(i))
print("".join(map(str,c)))
