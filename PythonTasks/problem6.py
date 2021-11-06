
''' 
    Name : AbdElrahman Ibrahim Zaki 
    Task : Assignment 1 
    email : abdelrahmanzaki.aez@gmail.com  
'''

''' ---------------------------------------------------------------------------------------------------------------------------------- '''
''' 
    6- Write a function that accepts two arguments (length, start) to generate 
    an array of a specific length filled with integer numbers increased by one from start. 
'''
def array_generator(length, start):
    array = list(range(start, start+length))
    print(array)

length = int(input("Enter the array length: "))
start = int(input("Enter the array start: "))
array_generator(length, start)
