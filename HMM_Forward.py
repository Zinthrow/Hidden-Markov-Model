"""
Created on Fri Nov 17 10:46:39 2017
/home/alex/Documents/Programming/576Bioinformatics/CollinHW/HMM_Forward.py
@author: alex
"""

import os

class Node():
    def __init__(self):
        self.score = None
        self.child = []
        self.parent = []
 
# Find the transitions file, open and extract values    
filename = "transition2.txt"
if os.path.exists(filename):
    lines = open(filename, 'r') 
    lines = lines.readlines()
a = {} #transition state probabilities lookup dictionary
for x in lines:
    x = x.split()
    a[x[0]+x[1]] = float(x[2])
 
# Find the emissions file, open and extract values    
filename = "emission2.txt"
if os.path.exists(filename):
    lines = open(filename, 'r') 
    lines = lines.readlines()
e = {} #emission probabilities for each position
e_nuc = ['A','C','G','T'] # the corresponding nucleotides for the emission probabilities
for x in lines:
    x= x.split()
    e_nuc.append(x[1])
    if x[0] in e:
        e[x[0]].append(float(x[2]))
    else:
        e[x[0]] = []
        e[x[0]].append(float(x[2]))
        
seq = "TAGA"
f = []

print (a)
'''
for y in range(len(seq)+1):
    for x in
    
'''

