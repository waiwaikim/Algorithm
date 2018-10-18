import sys
from Utility import Utility
from Solution_test import Solution_test

class Driver:

    def __init__(self):
        if len(sys.argv) < 2:
            print("Please provide the testcase filepath as a command line argument")
            return
        input = Utility().read_file(sys.argv[1])
        
             
        s = Solution_test(input)
        s.output_vector()
        print("Your solution")
        print("==========================================")
        print(s.output_vector())

Driver()
