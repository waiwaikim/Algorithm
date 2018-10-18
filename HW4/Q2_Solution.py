from collections import deque 
from xml.dom import InuseAttributeErr

class Q2_Solution :
    
    def __init__(self):
        
        '''
        input_list = [(1,3), (1,2)]                 # input_list = list of tuple 
        n = 3                                       # p = # of ADFs
        '''
        '''
        input_list = [(1,2), (2,3), (1,4), (3,4)]
        n = 4 
        '''
        '''
        input_list = [(2,1), (2,4), (5,3)]
        n = 5 
        '''
        theater= [0]*(n**2)               
        # theater is p x p list 
        
        
        ### input_list will be converted into a adjacency list 
        adjacency_list = {}                         
        #empty dictionary
        
        for i in range(1, n+1):                     
            #dictionary with p keys 
            adjacency_list[i] = []
        
        for p in input_list:                        
            #complete adjacency list 
            adjacency_list[p[0]].append(p[1])
            adjacency_list[p[1]].append(p[0])  
        
        max_key= list(adjacency_list.keys())[0]
        for key, value in adjacency_list.items():   
            #sort the adjacency list 
            value.sort()
            
            if len(adjacency_list[max_key]) <len(value):
                max_key=key                 
                #max key will the starting node at the first row 

        ### complete constructing adjacency list 

        seated_check_list = [0]*n                   
        #check if an element has been seated
        q = deque() 
        
        ##initialize seating 
        q.append(max_key)
        seated_check_list[max_key-1] = 1              
        #max_key takes a seat
        cur_row = 0 
        cur_column= max_column = 0 
        theater[n*cur_row + cur_column] = max_key 

        
        while 0 in seated_check_list:
        #while loops until everyone is seated 
            try:    
                current_node = q.popleft()
                cur_row+= 1 
                #increment after seating one row (one BFS level)       
                for j in adjacency_list[current_node]:
                    
                    if seated_check_list[j-1] ==0:
                        theater[n*cur_row + cur_column] = j
                        seated_check_list[j-1] = 1 
                        cur_column +=1 
                        max_column += 1
                        #next seats in the same row, next column 
                        q.append(j)
                    else:
                        pass
            except IndexError:
            #accounting for disconnected node / graph when queue is empty
                for key, value in adjacency_list.items():
                    if seated_check_list[key-1]==0:
                        q.append(key)
                        seated_check_list[key-1] = 1
                        cur_row = 0
                        cur_column = max_column 
                        theater[n*cur_row + cur_column] = key
                        break
        print(theater)
Q2_Solution()