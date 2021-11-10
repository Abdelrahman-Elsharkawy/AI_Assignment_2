#!/usr/bin/env python
# coding: utf-8

# In[2]:


adj_list = {'A':['B','C'],                                     ##list of the adjesnts for every node in the form of dictionary
            'B':['D','E'],
            'C':['B','F'],
            'D':[],
            'E':['F'],
            'F':[],}
color= {}                                                     ##three colors define the state of each node (White,Gray and Black)
parent= {}
traversal_time= {}                                            ##Time of first and last visit for each node
dfs_out= []
for node in adj_list:
    color[node]= 'W'
    parent[node]= None
    traversal_time[node]= [-1,-1]                    
time=0
def dfs(u):
    global time
    color[u]= 'G'
    traversal_time[u][0]= time
    dfs_out.append(u)
    for v in adj_list[u]:
        if color[v]== 'W':
            parent[v]= u
            dfs(v)                                           ##calling the dfs function recursivly
    color[u]= 'B'
    traversal_time[u][1] =time
    time+=1
dfs('A')                                                    ##passing 'A' to the function as A is the starting node
print(color)
print(parent)
print(traversal_time)
print(dfs_out)
print()
for node in adj_list.keys():
    print()
    print(node,"==>",traversal_time[node])

