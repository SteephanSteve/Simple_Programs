#!/usr/bin/python

f,l=raw_input().split(" ")
for n in range(int(f)+1,int(l)):
    n=map(int,list(str(n)))
    s=0
    for i in n:
        s=s+(i**len(n))
    if int(''.join(map(str,n)))==s:
       print s,




