from Match import Match

class Solution:
    
    def __init__(self, m, n, hospital_list, student_list, hosp_open_slots):
        """
            The constructor exists only to initialize variables. You do not need to change it.
            :param m: The number of hospitals
            :param n: The number of students
            :param hospital_list: The preference list of hospitals, as a dictionary.
            :param student_list: The preference list of the students, as a dictionary.
            :param hosp_open_slots: Open slots of each hospital
            """
        self.m = m
        self.n = n
        self.hospital_list = hospital_list
        self.student_list = student_list
        self.hosp_open_slots = hosp_open_slots
    
    def get_matches(self):
        #print("the number of hospitals %d" %self.m)
        #print("the number of students %d" %self.n)
        
        #print("print hospital list")
        #print(self.hospital_list.keys())

        #print(self.student_list.keys())  
        
        tot_open_slots = 0 
        for h in self.hosp_open_slots:
            tot_open_slots += self.hosp_open_slots[h]
            
        #print("total number of open slots %d" %tot_open_slots)
        
        tot_pos_proposal = self.m * self.n  ; 
        cur_proposal_num = 0 ;
        
        hos_proposal_num = dict.fromkeys(self.hospital_list.keys(),0)
        '''keeps track of the number of proposal hospitals have given out''' 
                
        student_match_check = dict.fromkeys(self.student_list.keys(), 0 )
        hospital_match_check = dict.fromkeys(self.hospital_list.keys(), 0)
        '''checks if a student is matched or not. first = matched or not / second hospital '''
  
        return_match = []
        
        while (len(return_match) < tot_open_slots and cur_proposal_num < tot_pos_proposal):
       
            for h in self.hospital_list:
                    if(self.hosp_open_slots[h]>0): 
                        
                        s = self.hospital_list[h][hos_proposal_num[h]]
                        #student 
                        hos_proposal_num[h] += 1 
                        cur_proposal_num += 1
                        #one for loop counts as one proposal
                        
                        if (self.hosp_open_slots[h]>0 and student_match_check[s] == 0 ) :
                        # if s is unmatched
                            return_match.append(Match(h,s))
                            self.hosp_open_slots[h] -=1 
                            student_match_check[s] = h
                            hospital_match_check[h] = s 
                            
                        elif (self.hosp_open_slots[h] > 0 and student_match_check[s] != 0  and self.student_list[s].index(h) < self.student_list[s].index(student_match_check[s]) ):
                            #curren if student is already matched 
      
                            return_match.remove(Match(student_match_check[s],s))
                           
                            self.hosp_open_slots[h] -= 1
                            self.hosp_open_slots[student_match_check[s]] += 1
                            
                            hospital_match_check[student_match_check[s]] =0 
                            student_match_check[s] = h 
                            hospital_match_check[h] =s 
                            return_match.append(Match(h,s))
              
                        else:
                        #student rejects h 
                            pass
                    else:
                        pass
                    #print(return_match)
            #print('\n')
                    #if cur_proposal_num == 100:
                     #   print(return_match)
        
        return return_match 
    
'''
        while (len(return_match) < tot_open_slots and cur_proposal_num < tot_pos_proposal):
        #while the number of matches in the current list is smaller than the total possible matches
        #and hospitals have not exhausted proposal possibilities 
        
            for h in self.hospital_list:
                s = self.hospital_list[h][hos_proposal_num[h]]
                #student 
                hos_proposal_num[h] += 1 
                #one for loop counts as one proposal
                #print("(h,s) %d %d" %(h , s))
              
                if (self.hosp_open_slots[h] >0  and student_match_check[s] == 0) :
                # if s is unmatched
                    return_match.append(Match(h,s))
                    self.hosp_open_slots[h] -=1 
                    student_match_check[s] = h
                    
                elif (self.hosp_open_slots[h] >0 and self.student_list[s].index(h) < self.student_list[s].index(student_match_check[s]) ):
                    #if student is already matched 
                    #print("current hospital %d ranking %d " %(student_match_check[s], self.student_list[s].index(student_match_check[s]) ))
                    #print("alt hosptial %d ranking %d " %(h, self.student_list[s].index(h))) 
                    
                    return_match.remove(Match(student_match_check[s],s))
                    self.hosp_open_slots[h] -= 1
                    self.hosp_open_slots[student_match_check[s]] += 1
                    student_match_check[s] = h 
                    return_match.append(Match(h,s))
                    
                else:
                #student rejects h 
                    pass
                #print(return_match)
         '''   
