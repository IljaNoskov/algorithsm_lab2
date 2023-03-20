n=int(input())
q=[]
for i in range(n):
    s=input().split()
    for k in range(4):
        s[k]=int(s[k])
    q.append(s)
m=int(input())
p=[]
for i in range(m):
    s=input().split()
    for k in range(2):
        s[k]=int(s[k])
    p.append(s)
for i in range(m):
    num=0
    for k in range(n):
        if (p[i][0]>=q[k][0] and p[i][0]<=q[k][2]) and (p[i][1]>=q[k][1] and p[i][1]<=q[k][3]):
            num+=1
    print(num,end=' ')
