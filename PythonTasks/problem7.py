
''' 
    Name : AbdElrahman Ibrahim Zaki 
    Task : Assignment 1 
    email : abdelrahmanzaki.aez@gmail.com  
'''

''' ---------------------------------------------------------------------------------------------------------------------------------- '''
''' 
   7- write a function that takes a number as an argument and if the number divisible by 3 return 
    "Fizz" and if it is divisible by 5 return "buzz" and if it is divisible by both return "FizzBuzz" 
'''
def function(num):
    if(num % 3 == 0 and num % 5 == 0):
        print("FizzBuzz")
    elif(num % 5 == 0 and num % 3 != 0):
        print("Buzz")
    elif(num % 3 == 0 and num % 5 != 0):
        print("Fizz")
    else:
        print("The number is not divisible neither by 3 nor by 5")


number = int(input("Enter a number: "))
function(number)