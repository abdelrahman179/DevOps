""" 
    Name : AbdElrahman Ibrahim Zaki
    Email : abdelrahmanzaki.aez@gmail.com  
    Project : B - Data Format - main file
"""
import datetime
from function import change_date_format

input_dates = []
input_dates = list(input('Enter a date in the format of YYYY/MM/DD: ').split())
for x in input_dates:
    format = "%Y/%m/%d"
    date_time = datetime.datetime.strptime(x, format)
    new_format = date_time.strftime('%Y/%m/%d')


try:
  print(input_dates, " This is the correct date string format. \n")
  output = change_date_format(input_dates)
  print(output)
except ValueError:
  print("This is the incorrect date string format. It should be YYYY/MM/DD")