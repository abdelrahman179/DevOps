
''' 
    Name : AbdElrahman Ibrahim Zaki 
    Task : Assignment 1 
    email : abdelrahmanzaki.aez@gmail.com  
'''

''' ---------------------------------------------------------------------------------------------------------------------------------- '''
''' 
    10- Ask the user for his name then confirm that he has entered his name 
    (not an empty string/integers). then proceed to ask him for his email and print all this data
'''
import re


def validate_email(email):
    if (re.search(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', email)):
        print("Your email is "+ email)

    else:
        print("Invalid Email")

def validate_name(name):
    regex_name = re.compile(r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',
                            re.IGNORECASE)
    if regex_name.search(name):
        print("Your name is "+ name)

    else:
        print("Invalid Name")

name = input("Enter Your Name: ")
email = input("Enter Your Email: ")
validate_name(name)
validate_email(email)
    
