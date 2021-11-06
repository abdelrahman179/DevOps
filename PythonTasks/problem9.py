
''' 
    Name : AbdElrahman Ibrahim Zaki 
    Task : Assignment 1 
    email : abdelrahmanzaki.aez@gmail.com  
'''

''' ---------------------------------------------------------------------------------------------------------------------------------- '''
''' 
    9- Ask the user to enter the radius of a circle in order to alert its calculated area and circumference. 
'''
from math import pi
def circleArea(rad):
    area = pi * (rad**2)
    print("The Area of the circle which radius is %0.2f = %0.2f" % (rad,area))

def circleCircumference(rad):
    circ = 2 * pi * rad
    print("The Circumference of the circle which radius is %0.2f = %0.2f" %(rad,circ))

radius = float(input("Please enter the circle radius: "))
circleArea(radius)
circleCircumference(radius)