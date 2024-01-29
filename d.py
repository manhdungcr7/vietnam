import sys
arr=sys.stdin.read().strip().split('\n')
case=1
case_line=0
while True:
    count=0
    m,n=list(map(int,arr[case_line].strip().split()))
    temp=arr[case_line+1:case_line+m+1]
    temp=[[i for i in line] for line in temp]
    def bucket_fill(temp_arr,i,j):
        if i<0 or j<0 or i>=len(temp_arr) or j>=len(temp_arr[0]):
            return 
        if temp_arr[i][j]!='-':
            return
        temp_arr[i][j]='!'
        bucket_fill(temp_arr,i-1,j)
        bucket_fill(temp_arr,i+1,j)
        bucket_fill(temp_arr,i,j-1)
        bucket_fill(temp_arr,i,j+1)

    for so_hang,hang in enumerate(temp):
        for so_cot,cell in enumerate(hang):
            if cell=='-': 
                count+=1
                bucket_fill(temp,so_hang,so_cot)
                
    print(f'Case {case}: {count}')
    case_line=case_line+m+1
    case+=1
    if case_line>=len(arr):
        break