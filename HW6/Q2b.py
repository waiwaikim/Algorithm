import sys 
import operator

def q2_part_b(house_list):
    
    house_list.sort(key=operator.itemgetter(1))
    print("after sorting: " , house_list)
 
    tower_list= [(0,100)] 
    cur_band = 100 
  
    for i in range(len(house_list)-1):
        if house_list[i+1][1] < cur_band:
            pass     
        else:   
            cur_band = house_list[i][1] + 100
            tower_list.append((house_list[i][0], cur_band))
    
    return tower_list 


def q2_part_b2(house_list):
    
    house_list.sort(key=operator.itemgetter(1))
    print("after sorting: " , house_list)
    #the input given to us is not sorted.
    #it's sorted by the distance from the first house
    
    tower_list= [(0,100)] 
    cur_band = 100 
    #it's assumed that the first tower is installed on the first house
    #tower_list[i] = (house number, current bandwidth)
    #tower_list[0]=(0,100) = (first tower installed at house 0, the tower has bandwidth up to 100)
    
    for i in range(len(house_list)-1):
        #iterate up to the second-to-last house 
        if house_list[i+1][1] < cur_band:
            #when the next house inside the current bandwidth, we do nothing and go to the next house
            pass
        else:
            #install tower at the current house location
            #increment the current bandwidth by 100 miles             
            cur_band = house_list[i][1] + 100
            tower_list.append((house_list[i][0], cur_band))
    
    return tower_list 


if __name__ == "__main__":
    
    input = [(1,120), (2,50), (3,250), (4,160)]
    print("initial input: ", input)
    print(q2_part_b(input))
    