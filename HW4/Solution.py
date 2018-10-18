import queue
from collections import deque 
class Solution:

    def __init__(self, start_node, graph):
        self.start_node = start_node
        self.graph = graph
        
    def output_distances(self):
        """
        :return: the list of minimum distances from each node to the start node
        """

        #initialization 
        return_list = [-1]*len(self.graph)
        visit_check_list = [0]*len(self.graph)
        checker = 0 ; 
        
        #q = queue.Queue()
        q= deque()
        q.append(self.start_node)
               
        start_node = self.start_node
        return_list[start_node] = 0 
        visit_check_list[start_node]=1
        checker = 1
        # end of initialization 
        
      
        while q and checker < len(self.graph):
            current_node = q.popleft()
            current_dist = return_list[current_node]
            
            for i in self.graph[current_node]:
                
                if visit_check_list[i] == 0 : 
                    return_list[i] = current_dist +1 
                    visit_check_list[i] = 1
                    checker += 1
                    q.append(i)
                    
                else:
                    pass
  
        #print(return_list[start_node])
        return return_list
