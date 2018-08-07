#!/usr/bin/python

a=[]
for i in range(2):
    t=raw_input().split(' ')
    t=map(int,t)
    x=t[0]*60+t[1]
    a.append(x)
d=abs(a[0]-a[1])
print d//60,d%60
