"""
Created on Fri Nov 17 10:46:39 2017
/home/alex/Documents/Programming/576Bioinformatics/CollinHW/HMM_Forward.py
@author: alex
"""

import os

# Find the transitions file, open and extract values    
filename = "transition2.txt"
if os.path.exists(filename):
    lines = open(filename, 'r') 
    lines = lines.readlines()
a = {} #transition state probabilities lookup dictionary
l = -1 #number of states
for x in lines:
    x = x.split()
    if int(x[1]) > l:
        l = int(x[1])
    if x[1] in a:
        a[x[1]].append([x[0],float(x[2])]) 
    else:
        a[x[1]] = []
        a[x[1]].append([x[0],float(x[2])])
        
# Find the emissions file, open and extract values    
filename = "emission2.txt"
if os.path.exists(filename):
    lines = open(filename, 'r') 
    lines = lines.readlines()
e = {} #emission probabilities for each position
e_nuc = ['A','C','G','T'] #nucleotides for the emission probabilities
for x in lines:
    x= x.split()
    if x[0] in e:
        e[x[0]].append(float(x[2]))
    else:
        e[x[0]] = []
        e[x[0]].append(float(x[2]))
        
seq = "TAGA"

class Forward():
    def __init__(self, seq):
        self.f = ["a"]
        self.e = e
        self.a = a
        self.e_nuc = e_nuc
        self.l = l
        self.seq = seq
    def get_f(self):
        return self.f
    def implement(self):
        print (self.seq)
for y in range(len(seq)+1):
    for x in range(l):
        if y == 0:
            continue

forward = Forward(seq)
forward.implement()


