
''' 
    Name : AbdElrahman Ibrahim Zaki 
    Task : Assignment 1 
    email : abdelrahmanzaki.aez@gmail.com  
'''

''' ---------------------------------------------------------------------------------------------------------------------------------- '''
''' 
    2- The program takes a string and remove the vowels character from it then print its new version 
'''
def remove_vowel(string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    newstr = string;
    for x in string.lower():
        if x in vowels: 
            newstr = newstr.replace(x, "");
    return newstr

string = input("Enter a sentence: ")
new_str = remove_vowel(string)
print("The new sentence without vowels: ")
print(new_str)
