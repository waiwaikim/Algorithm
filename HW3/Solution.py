class Solution:

    def __init__(self, in_vector):
        """
        The constructor exists only to initialize variables.
        You do not need to change it.
        :param in_vector: The vector given from the file, as a list
        """
        self.in_vector = in_vector

    def output_vector(self):
        """
        This method must be filled in by you. You may add
        other methods and subclasses as you see fit,
        but they must remain within the Solution class.
        :return: a correct output vector, as a Python list
        """
        
        #print(self.in_vector)
        
        return_vector = [0]*len(self.in_vector)
        
        for i in range(len(self.in_vector)-1,-1,-1):
              
            if i == (len(self.in_vector)-1):
                return_vector[i] = self.in_vector[i]
            
            else:
                return_vector[i] = return_vector[i+1] + self.in_vector[i]
        
        '''        
        for i in range(len(self.in_vector)):
        
            print(self.in_vector[i])
        '''
                
        return return_vector
