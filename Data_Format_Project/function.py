""" 
    Name : AbdElrahman Ibrahim Zaki
    Email : abdelrahmanzaki.aez@gmail.com  
    Project : B - Data Format - function file
"""
def change_date_format(date_format): 
    new_list = []
    for x in date_format:
        new_list.append(x.replace("/",""))
    return new_list