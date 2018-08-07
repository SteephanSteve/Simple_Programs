#!/usr/bin/python

def prog(n,a,d):
    s=0
    for i in range(n):
        s=s+a
        a+=d
        print s
    return s
n,a,d=raw_input().split(" ")
print prog(int(n),int(a),int(d))
