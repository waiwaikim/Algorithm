import sys
from collections import deque 

def Toporder(G):
    
    IncomingEdges = [0]*len(G)
    NoIncoming = deque()
    TopOrder = []
    
    for v, e in G.items():
        for edge in e: 
            IncomingEdges[edge[0]-1] += 1 
    
    for index in range(len(IncomingEdges)):
        if IncomingEdges[index] == 0:
            NoIncoming.append(index+1)       
    
 
    while NoIncoming : 
        current = NoIncoming.popleft()
        TopOrder.append(current)
        
        for e in G[current]:
            IncomingEdges[e[0]-1] -=1 
            if IncomingEdges[e[0]-1] == 0 :
                NoIncoming.append(e[0])
    
    return TopOrder

def DagShort(G, top, s, f):        
    
    dist= {v: [float('infinity'), -1] for v,_ in G.items()}
    dist[s][0] = 0 
    
    start_index = top.index(s)
    
    for v in top[start_index:]: 
        for e in G[v]:
            vertex = e[0]
            weight = e[1]
            
            if dist[vertex][0] > dist[v][0] + weight:
                dist[vertex][0] = dist[v][0] + weight
                dist[vertex][1] = v 
                
    #print(dist)
    return_path = [] 
    temp = f 
    return_path.insert(0, temp)
    
    while temp != s:
        temp = dist[temp][1]
        return_path.insert(0,temp )
        
    return return_path
        
    
if __name__ == '__main__':
    
    graph = {1: [(2,5), (3,3)], 
             2: [(3,2), (4,6)], 
             3:[(4,7),(5,4),(6,2)], 
             4:[(5,-1), (6,1)], 
             5:[(6,-2)],
             6:[] }
    
    #print(graph)
    
    toporder = Toporder(graph)
    
    print(DagShort(graph, toporder, 1,5))
   