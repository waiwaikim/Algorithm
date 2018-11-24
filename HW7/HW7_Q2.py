

if __name__ == '__main__':
    
    graph = {1: [ 2, 4],
             2: [ 1, 3, 8],
             3: [2],
             4: [1, 5],
             5: [4, 6, 7],
             6: [5],
             7: [5],
             8: [2]}
    
    discovered = [0]*len(graph)
    discovered[1] = 1 
    
    