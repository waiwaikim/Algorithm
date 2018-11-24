from _ast import operator
import operator
class Solution:
    
    def __init__(self, listOfRallies):
        self.rallies = listOfRallies
    
    def getSchedule(self):
        
        key_rally = []
        for i in range(len(self.rallies)):
            key_rally.append((i, self.rallies[i][0], self.rallies[i][1]))
        
        key_rally.sort(key=operator.itemgetter(2))
        #print(key_rally)
        
        schedule = [] 
        
        for rally in key_rally:
            
            id = rally[0]
            
            if not schedule:
                start = 0 
                finish = start + rally[1]
            else: 
                start = finish 
                finish = start + rally[1]
                    
            if finish > rally[2]:
                return [] 
            schedule.append((id, start))
 
        return schedule 
