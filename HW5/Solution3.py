from collections import deque 

class Solution2_test:
    def __init__(self, graph):
        self.graph = graph
        self.output = []
        self.visited = [0]*len(graph)
        self.parent = [-1]*len(self.graph)
        self.found = False 
        self.stack = [] 
    def dfs(self, v):
        
        if not self.found : 

            self.visited[v] = 1 
            self.stack.append(v)
            print("v:" , v)
            #print(self.visited)
            for i in self.graph[v]:
                print(i)
                if(self.visited[i] ==0):
                    self.parent[i] = v
                    #print("parent[i]: ", self.parent[i])
                    self.dfs(i)
                elif (self.parent[v] != i) and not(self.found):
                    self.found = True
                    while self.stack: 
                        n = self.stack.pop()
                        self.output.append(n)

        
    def find_cycle(self):
        
        print(self.graph[0])
        print(self.graph[1])
     
        
        for key, value in self.graph.items():
            if(self.visited[key]==0):
               
                self.dfs(key)
        
        return self.output 
    
  
