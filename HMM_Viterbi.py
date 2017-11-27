#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 14:57:52 2017

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
        a[int(x[1])].append([int(x[0]), float(x[2])]) # after the key exists this appends the key's extra transition states
    else:
        a[int(x[1])] = []#transition states are saved in a dict format that the key is what is being transitioned to
        a[int(x[1])].append([int(x[0]), float(x[2])]) #inside that key is a list of the original state and the probability to transition to the key
        
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
        e[int(x[0])] = []#Makes a dictionary with a key that signifies the current state "l" and the corresponding nucleotide probabilities
        e[int(x[0])].append(float(x[2]))
        
seq = "TAG"

class Viterbi():
    def __init__(self, seq):
        self.v = [] # table that holds all probabilities
        self.e = e # emission states
        self.a = a # transmission states
        self.e_nuc = e_nuc # nucleotide order in emmissions dictionary
        self.l = l # number of states
        self.seq = seq # the sequence being compared
    def get_v(self): # print results
        for vs in self.v:
            print (vs)
        vb = self.get_max(l-1,len(self.seq))
        print (vb)
        print ("")
        for path in self.v:
            print(len(self.seq) - path[::-1].index(max(path))+1)
            
        
    def get_max(self,i,j): # find the max of all states that leads to the probability at v given state in the previous nucleotides 
        v = self.v
        a = self.a
        path_max = 0
        for x in a[i+1]:
            if j == 0 and x[0] == 0: #for the paths that lead from the original state
                path_current = x[1]
                if path_current > path_max:
                    path_max = path_current                        
            elif j != 0 and x[0] != 0:# for all other paths
                path_current = (v[j-1][x[0]-1]*x[1])
                if path_current > path_max:
                    path_max = path_current
        return path_max 
    def get_emission(self,i,j):# returns the emission of every nucleotide given state "l"
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
    def implement(self):#multiplies the Sum of previous applicable values in "v" by the emission given state "l"
        l = self.l
        seq = self.seq
        for y in range(len(seq)):
            self.v.append([])
            for x in range(l-1):
                v_score = self.get_emission(x,y)*self.get_max(x,y)
                self.v[y].append(v_score)
            
                
viterbi = Viterbi(seq)
viterbi.implement()
viterbi.get_v()
