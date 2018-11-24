from operator import itemgetter
import math 
class Solution:
    def __init__(self, points):
        self.points = points
            
    def dist(self, a, b):
        return ((a[0]-b[0])**2 +(a[1]-b[1])**2)**0.5
    
    def brute(self, px):
        
        min = self.dist(px[0], px[1])
        len_x = len(px)
        p1 = px[0]
        p2 = px[1]
        
        if len_x ==2:
            return p1, p2, min 
        for i in range(len_x):
            for j in range(i+1, len_x):
                d = self.dist(px[i], px[j])
                if d < min:
                    min = d
                    p1 = px[i]
                    p2 = px[j]
        return p1, p2, min
    
    def closest_pair_rec(self, px, py):
        len_px = len(px)
        
        if len_px <= 3:
            return self.brute(px)
        
        Qx = px[:len_px//2]
        Rx = px[len_px//2:]
        #print("Qx: " , Qx, '\n', "Rx: ", Rx)
        Qy = []
        Ry = []
        
        for y in py:
            if y[0] <= px[len_px//2][0]: 
                Qy.append(y)
            else: 
                Ry.append(y)
                
        (q1, q2, min1) = self.closest_pair_rec(Qx, Qy)
        (r1, r2, min2) = self.closest_pair_rec(Rx, Ry)
        
        
        if min1<min2 :
            d = min1 
            pair = (q1,q2)
        else:
            d= min2
            pair = (r1,r2)
            
        #print("d: ", d ,"pair: ", pair)
        
        x_star = px[len_px//2][0]
        #print("x_star: ", x_star)
        
        #print("low: " ,x_star-d, "high: ", x_star+d)
        s = [x for x in py if (x_star-d) <= x[0] <= (x_star+d)]
        #print("s: ", s)
        
        for i in range(len(s)):
            for j in range(i+1 , min(i+15, len(s))): 
                first, second = s[i], s[j]
                int_d = self.dist(first, second)
                
                if int_d < d:
                    d = int_d 
                    pair = (first, second)
                    
        return pair[0], pair[1], d
        
    def findClosestPair(self):
        px = sorted(self.points, key=itemgetter(0,1))
        py = sorted(self.points, key=itemgetter(1,0))
        #print("px: ", px)
        #print("py: ", py)
       
        p1, p2, min = self.closest_pair_rec(px,py)
        #rint("p1: ", p1, "p2: ", p2)
        return min        

