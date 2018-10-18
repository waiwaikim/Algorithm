import sys
from Utility import Utility
from Solution import Solution
from Match import Match
import numpy as np 

class Driver:
    
    def compare(): 
        answer = np.genfromtxt(sys.argv[2], delimiter = ',')
        
        
    

    def __init__(self):
        if len(sys.argv) < 2:
            print("Please provide the testcase filepath as a command line argument")
            return
        
        input = Utility().read_file(sys.argv[1])
        s = Solution(len(input.hospital_preferences), len(input.student_preferences), input.hospital_preferences, input.student_preferences, input.hospital_open_slots)
        solution = s.get_matches()
        print("Your Solution")
        print("=============================================")
        print(solution)

        '''
        
        f = open(sys.argv[2], 'r')
        answer = [] 
        
        for t in open(sys.argv[2]).read().split('),'):
            a, b = t.replace('(','').replace(')','').replace('[','').replace(']','').replace(' ', '').split(',')
            answer.append(Match(int(a), int(b)))
        
        print('\n')
        print(answer)
        print("lengh of solution %d" %len(solution))
        for sol in solution:
            print(sol)
            try:
                answer.remove(sol)
            except:
                print("error")
                print(sol)
                break
        
        print(answer )
        '''
Driver()
