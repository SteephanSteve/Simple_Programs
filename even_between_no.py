#!/usr/bin/python

f,l=raw_input().split(" ")
f,l=int(f),int(l)
for i in range(f+1,l):
    if i%2==0:
        print i,
