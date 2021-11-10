#!/usr/bin/env python
# coding: utf-8

# In[25]:


from queue import Queue
adj_list = {'A':['B','D'],                                     ##list of the adjesnts for every node in the form of dictionary
            'B':['A','C'],
            'C':['D'],
            'D':['A','E','F'],
            'E':['D','F','G'],
            'F':['D','E','H'],
            'G':['E','H'],
            'H':['F','G'],}
visited= {}
level= {}
parent={}
bfs_out=[]
queue=Queue()
for node in adj_list.keys():
    visited[node]=False
    parent[node]=None
    level[node]=-1
                                                               ##Viewing the dictionaries before starting (initial state) 
print(visited)
print(level)
print(parent)   
                                                               ##put u = 'A' as A is the starting node
u='A'
visited [u]=True
level[u]=0
queue.put(u)
                                                               ##put values of the dictionaries 
while not queue.empty():
    u=queue.get()
    bfs_out.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[v]=True
            parent[v]=u
            level[v]=level[u]+1
            queue.put(v)
v='G'                                                         ##finding the shortest path for any node from the starting node ('G' for example)
path=[]
while v is not None:
    path.append(v)
    v=parent[v]
path.reverse()

print(bfs_out)
print(level)
print(path)
        

