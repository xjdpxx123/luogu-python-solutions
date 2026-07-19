m,t,s = map(int,input().split())

if t == 0:
    print(0)
else:
    apple = m - (s+t-1)//t
    print(max(0, apple))