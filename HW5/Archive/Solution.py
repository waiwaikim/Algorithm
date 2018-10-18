from collections import deque 

class Solution:
    def __init__(self, graph):
        self.graph = graph
   
    def isCyclicUtil(self, u, parent):
       
        Visited[u] = 1
        
        for i in self.graph[u]:

            if Visited[i]== 0 and parent != i:
            #not visited / not parent 
                if(self.isCyclicUtil(i, u)):
                    
                 Unordered.append(i)
                 return True
                    
            elif Visited[i] ==1 and parent != i :
            #visited / not parent 

                return True
        
        return False   
    
    def TopOrderOrCyle(self, ordering, k, active):
        
        #Unorderd is a stack. Make sure to use append() / pop()
        
        length = len(self.graph)
        if (k == length):
            return ordering 
        
        else:

            w = active.index(1)
            global Visited 
            Visited = [0]*length
            Visited[w] = 1 

            global Unordered
            Unordered = []
            Unordered.append(w)
            
            self.isCyclicUtil(w, -1)
            
            return Unordered


    def find_cycle(self):
        
        length = len(self.graph)
        
        incomingEdges = [0]*length
        NoIncoming =[]
        ordering = []*length
        active = [1]*length
     
        for key, value in self.graph.items():
            for i in value:
                incomingEdges[i] += 1
          
        for k in range(length):
            if incomingEdges[k] == 0 :
                NoIncoming.append(k)
        '''
        for key, value in self.graph.items():
            if incomingEdges[key] == 0:
                NoIncoming.append(key)
        '''                
        
        k=0 
  
        while(NoIncoming):
            v = NoIncoming[0]
            NoIncoming.remove(v)
           
            #ordering[k].append(v) 
            ordering[k]= v
            k += 1 

            for j in self.graph[v]:
                if active[j] == 1 :
                    incomingEdges[j] -= 1 
                if incomingEdges[j] == 0 :
                    NoIncoming.append(j)
            
            active[v] =0
            
            print("ordering: ", ordering)
        
    
        return self.TopOrderOrCyle(ordering, k, active)
       
