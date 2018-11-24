import sys

class Solution:

    def __init__(self, graph):
        self.graph = graph
        
    def findMin(self, key, mst):
        
        min = float('infinity')
        return_index = -1 
        
        for j in range(len(self.graph)):
            if key[j] < min and mst[j] == False:
                min = key[j]
                return_index = j
                
        return return_index 
                

    def output_edges(self):
        
        key = [float('infinity')]*len(self.graph)
        parent = [-1]*len(self.graph)
        key[0] = 0 
        mst = [False] *len(self.graph)
        
        parent[0]= -1 
        
        for i in range(len(self.graph)):
            add_node = self.findMin(key, mst)
  
            mst[add_node] = True 
            
            
            for h in range(len(self.graph)):
                if self.graph[add_node][h]>=0 and mst[h] == False and key[h] > self.graph[add_node][h]:
                    key[h] = self.graph[add_node][h]
                    parent[h] = add_node
                    
            
        
        return parent
