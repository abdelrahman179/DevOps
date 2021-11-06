
''' 
    Name : AbdElrahman Ibrahim Zaki 
    Task : Assignment 1 
    email : abdelrahmanzaki.aez@gmail.com  
'''

''' ---------------------------------------------------------------------------------------------------------------------------------- '''
''' 
    8- Write a function which has an input of a string from user then it will return the same string reversed. 
'''
def reverseString(string):
    str = string[::-1]
    print(str)

string = input("Enter a string: ")
reverseString(string)
