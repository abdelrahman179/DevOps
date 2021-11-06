
''' 
    Name : AbdElrahman Ibrahim Zaki 
    Task : Assignment 1 
    email : abdelrahmanzaki.aez@gmail.com  
'''


''' 
    1- Given two points represented as x1,y1,x2,y2. Return the (float) distance between 
    them considering the following distance equation. 
'''


import math
def distance_func(x1, x2, y1, y2):
    distance = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    return distance


a1 = 1.26 
a2 = 2.39
b1 = 1.58
b2 = 2.42
dist = distance_func(a1, a2, b1, b2)
print(dist)