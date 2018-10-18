import sys
from Utility import Utility
from Solution import Solution

class Driver:

    def __init__(self):
        if len(sys.argv) < 2:
            print("Please provide the testcase filepath as a command line argument")
            return
        input = Utility().read_file(sys.argv[1])
        
      
            
        s = Solution(input.start_node, input.graph)
        solution = s.output_distances()
        print("Your Solution")
        print("=============================================")
        print(solution)
        
Driver()
