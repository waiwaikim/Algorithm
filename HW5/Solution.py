from collections import deque 

class Solution:
    def __init__(self, graph):
        self.graph = graph
        self.output = []
        self.visited = [0]*len(graph)
        self.parent = [-2]*len(graph)
        self.found = False 
        self.stack = [] 
        
    def dfs(self, v, p):
        
        if not self.found : 
            
            
            self.visited[v] = 1 
            self.stack.append(v)
            #print("\n")
            #print("v:" , v)
            #print("Stack: ", self.stack)
            #print(self.visited)
            for i in self.graph[v]:
                #print(v, ":", i)
                if(self.visited[i] ==0) and (len(self.graph[i]) >1 ) :
                    #not visited yet 
                    self.parent[i] = v
       
                    self.dfs(i, v)
        
                elif (self.parent[v] != i) and not(self.found) and len(self.graph[i]) >1 and len(self.stack) >=3 :
                    #visited, not parent 
          
                    self.found = True
                    #print("found at ", i)
                    while self.stack: 
                        n = self.stack.pop()
                        '''
                        if len(self.output)>0 :
                            print("current term: ", n )
                            print("previous term's parent: ", self.parent[self.output[(len(self.output))-1 ]], "\n")
                        '''
                        if (len(self.output) == 0):
                            self.output.append(n)
                        elif  (n == self.parent[self.output[(len(self.output))-1 ]]):
                            self.output.append(n)
                
                    while not (self.output[len(self.output)-1] in self.graph[self.output[0]]):
                        self.output = self.output[:len(self.output)-1]
                    break
        
        
    def find_cycle(self):
        
        for key, value in self.graph.items():
            
            #print("key several times:" , key)
            if(self.visited[key]==0):
                #print("cleared stack")
                self.parent[key] =-1 
                self.stack.clear()
                self.dfs(key,-3)
        
            if(self.found ==1 ):
                break
        return self.output 
    
  
