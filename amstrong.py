#!/usr/bin/python

n=map(int,list(raw_input()))
s=0
for i in n:
    s=s+(i**len(n))
if int(''.join(map(str,n)))==s:
       print "yes"
else:
    print "no"
