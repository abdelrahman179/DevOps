
''' 
    Name : AbdElrahman Ibrahim Zaki 
    Task : Assignment 1 
    email : abdelrahmanzaki.aez@gmail.com  
'''

''' ---------------------------------------------------------------------------------------------------------------------------------- '''
''' 
    4- Given a list of numbers, create a function that returns a list where all similar 
        adjacent elements have been reduced to a single element. 
'''
def rem_similar_elements(old_list):
    new_list = []
    for i in old_list:
        if i not in new_list:
            new_list.append(i)
    return new_list


old_list = [7, 2, 6, 8, 4, 6, 7, 6]
new_list = rem_similar_elements(old_list)
print(new_list)