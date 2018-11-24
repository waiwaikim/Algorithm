import heapq
class Solution:
    def __init__(self, start_node, end_node, graph):
        self.graph = graph
        self.start_node = start_node
        self.end_node = end_node

    def outputPath(self):
        
        dist = {node : float('infinity') for node, neighbor in self.graph.items() }
        dist[self.start_node] = 0 
        
        entry_lookup = {} 
        pq = [] 
        
        explored = set()
        heapq.heappush(pq, [0,self.start_node,None] )
        
        for  node, distance in dist.items():
            entry = [distance, node]
            entry_lookup[node] = entry 
            
        #print("starting priority queue: " , pq)
         
        while pq: 
            cur_dist, cur_node, cur_path = heapq.heappop(pq)
            
            if cur_node not in explored:
                explored.add(cur_node)
            
                if cur_node == self.end_node: 
                    #at destination, reverse traverse entry_lookup
                    return_list = [] 
                    temp = cur_node 
                    return_list.append(temp)
                    while temp != self.start_node:
                        temp = entry_lookup[temp][1]
                        return_list.insert(0, temp)                   
                
                    return return_list
            
                neighbor_dist = self.graph[cur_node][0]
                neighbor_list = self.graph[cur_node][1:]
                
                for neighbor in neighbor_list: 
                    if neighbor in explored: pass
                    
                    else:
                        distance = cur_dist + neighbor_dist 
                        
                        if distance <entry_lookup[neighbor][0]:
                           #when algo finds a shorter path, update 
                            entry_lookup[neighbor] = distance , cur_node 
                            heapq.heappush(pq, [distance, neighbor, cur_node])
                              

        return [] #Return empty
