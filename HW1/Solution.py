from Marriage import Marriage
from itertools import permutations
import itertools

class Solution:

    def __init__(self, number, women, men):
        """
        The constructor exists only to initialize variables. You do not need to change it.
        :param number: The number of members
        :param men: The preference list of men, as a dictionary.
        :param women: The preference list of the women, as a dictionary.
        """
        self.num = number
        self.men = men
        self.women = women
        self.count = 0
        self.stable_matchings = []
      
      

    def set_marriage(self):
        
        men_list = list(self.men.keys())
        women_list = list(self.women.keys())
        marriage_list = [] 
        
        for w in itertools.permutations(women_list):
            each_marriage_set = [] 
 
            for i in range(0,self.num):
                each_marriage_set.append(Marriage(i+1, w[i])) 
            #print(type(each_marriage_set))
            #print(each_marriage_set)
            marriage_list.append(each_marriage_set)
        ''' marriage_list contains all possible permutations of marriages'''
        
        return marriage_list
    
    def test_marriage(self, set):
        ''' return 1 if it's stable, else return 0 (unstable) '''
        
        for i in range(0, self.num):

            m = set[i].man()
            w = set[i].woman()
            for j in range(0, self.num):
    
                alt_w = set[j].woman()
                alt_m = set[j].man()
               
                if (w == alt_w) :
                    pass 
                else:
                    cur_pos_w_in_m = self.men[m].index(w)
                    pos_alt_w_in_m = self.men[m].index(alt_w)
                    
                    cur_pos_m_in_alt_w = self.women[alt_w].index(alt_m)
                    pos_alt_m_in_alt_m= self.women[alt_w].index(m)
                 
                    if (cur_pos_w_in_m > pos_alt_w_in_m) and (cur_pos_m_in_alt_w > pos_alt_m_in_alt_m ):
                        '''
                        print("man : %d" %m)
                        print("woman : %d" %w)
                        
                        print(self.men[m])
                        print(self.women[w])
                        
                        print("ranking of man's current partner : %d" %m_cur_pos)
                        print("ranking of woman's current partner : %d" %w_cur_pos)
                        print("man's alternative partner: %d" %alt_w)
                        print(self.women[alt_w])
                        print("ranking of man's alternative partner: %d" %m_alt_pos)
                        print("ranking of woman's alternative partner: %d" %w_alt_pos)
                        '''
                        return 0 

        return 1 
       
        
    def iterate_set(self, input):
        return_list =[]
        
        for x in input:
            #print(type(x))
            test = self.test_marriage(x)    
            if test ==1 :
                return_list.append(x)
                
        return return_list 
    
    def output_stable_matchings(self):
        """
        This method both computes and returns the stable matchings
        :return: the list of stable matchings
        """
        
        possible_marriage = self.set_marriage()  
        self.stable_matchings = self.iterate_set(possible_marriage)
        
#         print(self.stable_matchings)
        
#         for i in self.women:
#             print("id %d :" %i , end="")
#             for j in self.women[i]:
#                 print(" %d" % j, end="")
#             print(' ')
        
        return self.stable_matchings
