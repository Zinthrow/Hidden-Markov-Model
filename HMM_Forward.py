"""
Created on Fri Nov 17 10:46:39 2017
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
    if int(x[1]) in a:
        a[int(x[1])].append([int(x[0]), float(x[2])]) 
    else:
        a[int(x[1])] = []
        a[int(x[1])].append([int(x[0]), float(x[2])])
        
# Find the emissions file, open and extract values    
filename = "emission2.txt"
if os.path.exists(filename):
    lines = open(filename, 'r') 
    lines = lines.readlines()
e = {} #emission probabilities for each position
e_nuc = ['A','C','G','T'] #nucleotides for the emission probabilities
for x in lines:
    x= x.split()
    if int(x[0]) in e:
        e[int(x[0])].append(float(x[2]))
    else:
        e[int(x[0])] = []
        e[int(x[0])].append(float(x[2]))
        
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
    def get_sum(self,i,j):
        f = self.f
        a = self.a
        path_sum = 0
        for x in a[i+1]:
            if j != 0:
                path_sum += (f[j-1][x[0]-1]*x[1])
            if j == 0 and x[0] == 0:
                path_sum += x[1]
        return path_sum 
    def get_emission(self,i,j):
        e = self.e
        seq = self.seq
        if seq[j] == 'A':
            return e[i+1][0]
        elif seq[j] == 'C':
            return e[i+1][1]
        elif seq[j] == 'G':
            return e[i+1][2]
        elif seq[j] == 'T':
            return e[i+1][3]
    def implement(self):
        l = self.l
        seq = self.seq
        for y in range(len(seq)+1):
            for x in range(l):
                self.f[y][x] = self.get_emission(x,y)*self.get_sum(x,y)
                    

forward = Forward(seq)
forward.implement()
print (forward.get_f)


