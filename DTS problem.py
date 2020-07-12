# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 13:32:29 2020

@author: RV
"""
import pandas as pd


file = open('files.txt', 'r')
node = open('nodes.txt', 'r')

files = {}
nodes = {}

for line in file.readlines():
    line = line.split()
    if(len(line)>0 and line[0][0].isalpha()):
        files[line[0]] = int(line[1])



for line in node.readlines():
    line = line.split()
    if(len(line)>0 and line[0][0].isalpha()):
        nodes[line[0]] = int(line[1])
    

files_sorted = sorted(files.items(), key=lambda x: x[1], reverse=True)
#nodes_sorted = sorted(nodes.items(), key=lambda x: x[1], reverse=True)
                   
values = nodes.copy()
for i in nodes:
    values[i]=0

plan={}

#values = sorted(values.items(), key=lambda x: x[1])
for f in files_sorted:
    values = sorted(values.items(), key=lambda x: x[1])
    test_tup1 = [i[0] for i in values]
    test_tup2 = [i[1] for i in values]
    values = {test_tup1[i] : test_tup2[i] for i, _ in enumerate(test_tup2)}
    k_values = [i for i in values.values()]
    k_key = [i for i in values.keys()]
    flag =1
    for i in range(len(values)):
        if(int(f[1]) <= int(nodes[k_key[i]])):
            plan[f[0]] = k_key[i]
            values[k_key[i]] += int(f[1])
            nodes[k_key[i]] -= int(f[1])
            flag=0
            break
    if flag ==1:
        plan[f[0]]='NULL'   
        
f = open('result.txt','w')       
 
for i in plan:
    k = i + " " + str(plan[i])
    f.write(k)
    f.write('\n')
    