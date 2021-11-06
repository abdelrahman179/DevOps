
''' 
    Name : AbdElrahman Ibrahim Zaki 
    Task : Assignment 1 
    email : abdelrahmanzaki.aez@gmail.com  
'''

''' ---------------------------------------------------------------------------------------------------------------------------------- '''
''' 
    5- Consider dividing a string into two halves. 
'''

def divideString(string):
    str_size = len(string)  # identify the string length

    if str_size % 2 == 0: # case 1 : The length is even, the front and back halves are the same length.
        half = str_size / 2  
        k = 0
        for i in range(len(string)):
            if k % half == 0: 
                print("\n")
            print(string[i])
            k +=1

    else: #  Case 2 : The length is odd, we'll say that the extra char goes in the front half.
        half = str_size / 2
        first_half = round(half)
        k = 0
        for i in range(len(string)):
            if k % first_half == 0:
                print("\n")
            print(string[i])
            k +=1
    
string = input("Enter a string to get it divided into two parts: ")
divideString(string)