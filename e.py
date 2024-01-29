import sys
a=sys.stdin.read().strip().split("\n")
def c(a,y):
	if y=="L":
		for i in range(0,4):
			for j in range(0,3):
				if a[i][j]==a[i][j+1]:
					a[i][j]+=a[i][j+1]
					a[i][j+1]=0
			a[i]=[x for x in a[i] if x!=0]+[0]*(a[i].count(0))
		return a
	elif y=="R":
		for i in range(0,4):
			for j in range(3,0,-1):
				if a[i][j]==a[i][j-1]:
					a[i][j]+=a[i][j-1]
					a[i][j-1]=0
			a[i]=[0]*(a[i].count(0))+[x for x in a[i] if x!=0]
		return a
	elif y=="D":
		for i in range(0,4):
			for j in range(0,3):
				if a[j][i]==a[j+1][i]:
					a[j][i]+=a[j+1][i]
					a[j+1][i]=0
			b=[a[j][i] for j in range(0,4) if a[j][i]!=0]
			b=[0]*(4-len(b))+b
			for m in range(0,4):
				a[m][i]=b[m]
		return a
	elif y=="U":
		for i in range(0,4):
			for j in range(3,0,-1):
				if a[j][i]==a[j-1][i]:
					a[j][i]+=a[j-1][i]
					a[j-1][i]=0
			b=[a[j][i] for j in range(0,4) if a[j][i]!=0]
			b+=[0]*(4-len(b))
			for m in range(0,4):
				a[m][i]=b[m]
		return a
b=[]
for i in range(0,4):
	b.append(list(map(int,a[i].strip().split())))
print(c(b,a[-1].strip()))


