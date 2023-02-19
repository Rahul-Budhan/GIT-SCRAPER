"""Imports Made here"""
from classes import *
from datetime import datetime

"""Set input and output location"""
input_location = './doc/users.txt'
output_location = './doc/info.txt'
currentDateAndTime = datetime.now()
time_now = currentDateAndTime.strftime("%H:%M:%S")


"""Read input file and get user names"""
all_users = get_users(input_location)
total_users = len(all_users)
for user in all_users:
    log_data = fetch_details(user,output_location)
write_into_file(output_location,str(total_users)+" User Details added at "+(time_now)+" ",False,True)
print("Execution Successfull")