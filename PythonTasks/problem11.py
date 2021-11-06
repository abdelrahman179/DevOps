
''' 
    Name : AbdElrahman Ibrahim Zaki 
    Task : Assignment 1 
    email : abdelrahmanzaki.aez@gmail.com  
'''

''' ---------------------------------------------------------------------------------------------------------------------------------- '''
''' 
    11- Write a function that takes a string and prints the longest alphabetical ordered substring occured.
'''
def longAlphOrder(str):
    temp = ''
    longAlpStr = ''
    
    for i in range(len(str)):
        temp += str[i]
        if len(temp) > len(longAlpStr): 
            longAlpStr = temp
        if i > len(str)-2:
            break
        if str[i] > str[i+1]:
            temp = ''
    print(longAlpStr)

string = input("Enter a string: ")
longAlphOrder(string)