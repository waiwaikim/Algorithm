import math 


def pow(a, n):
    b= 1
    for i in range(n):
        b = b*a 
    
    return  b

def divide_conquer_pow(a, n):
    if n==1: 
        return a 
    
    power = divide_conquer_pow(a, n//2) 
    
    if n%2 ==1:
        return a*power*power
    else:
        return power*power 
    
   
if __name__ == "__main__":
    
    a = 3 
    n = 4
    
    print(divide_conquer_pow(a, n))
 
     