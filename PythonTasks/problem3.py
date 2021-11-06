
''' 
    Name : AbdElrahman Ibrahim Zaki 
    Task : Assignment 1 
    email : abdelrahmanzaki.aez@gmail.com  
'''

''' ---------------------------------------------------------------------------------------------------------------------------------- '''
''' 
    3- The program takes a string and a character and returns a list with all the 
    locations that character was found in the given string. 
'''
def char_index(character, string):
    character_list = []
    count = 0
    for i in range(len(string)):
        if(string[i] == character):
            character_list.append(i)
    return character_list
    

string = input("Enter a string: ")
character = input("Enter a character to find: ")
loc_list = char_index(character, string)
if(len(loc_list)):
    print(loc_list)
else:
    print("Character "+character+" was not found in the given string.")
