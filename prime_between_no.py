#!/usr/bin/python

f,l=raw_input().split(" ")
f,l=int(f),int(l)
for i in range(f+1,l):
    if i>1:
        for n in range(2,i):
            if i%n==0:
                break
        else:
            print i,

                    
