import sys
arr=sys.stdin.read().strip().split("\n")
r,c=map(int,arr[0].split())
a=[list(map(int,arr[j].split())) for j in range(1,r+1)]
def u(a,r,c,i):
    if r==0 or c==0 or len(a)==0:
        return []
    else:
        if r==1 and c==1:
            return [[a[0][0]]]
        elif r==1:
            if i==1:
                b=[[a[0][-1]]+a[0][:-1]]
                return b
            else:
                b=[a[0][1:]+[a[0][0]]]
                return b
        elif c==1:
            if i==1:
                b=[[a[-1][0]]]+[[a[j][0]] for j in range(0,r-1)]
                return b
            else:
                b=[[a[j][0]] for j in range(1,r)]+[[a[0][0]]]
                return b
        elif r>=2 and c>=2:
            if i==1:
                if r==2 or c==2:
                    e=[]
                    if r==2:
                        g=[[a[1][0]]+a[0][:-1]]+[a[-1][1:]+[a[-2][-1]]]
                    elif c==2 and r>2:
                        g=[[a[1][0]]+a[0][:-1]]+[[a[m+2][0]]+[a[m][-1]] for m in range(0,r-2)]+[a[-1][1:]+[a[-2][-1]]]
                else:
                    e=[[a[m][n] for n in range(1,c-1)] for m in range(1,r-1)]
                    f=u(e,r-2,c-2,-1)
                    g=[[a[1][0]]+a[0][:-1]]+[[a[m+2][0]]+f[m]+[a[m][-1]] for m in range(0,r-2)]+[a[-1][1:]+[a[-2][-1]]]
                return g
            else:
                if r==2 or c==2:
                    e=[]
                    if r==2:
                        g=[a[0][1:]+[a[1][-1]]]+[[a[-2][0]]+a[-1][:-1]]
                    elif c==2 and r>2:
                        g=[a[0][1:]+[a[1][-1]]]+[[a[j][0]]+[a[j+2][-1]] for j in range(0,r-2)]+[[a[-2][0]]+a[-1][:-1]]
                else:
                    e=[[a[m][n] for n in range(1,c-1)] for m in range(1,r-1)]
                    f=u(e,r-2,c-2,1)
                    g=[a[0][1:]+[a[1][-1]]]+[[a[m][0]]+f[m]+[a[m+2][-1]] for m in range(0,r-2)]+[[a[-2][0]]+a[-1][:-1]]
                return g
b=u(a,r,c,1)
for i in range(0,len(b)):
    print(" ".join(map(str,b[i])))