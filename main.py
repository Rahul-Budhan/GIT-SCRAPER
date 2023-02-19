"""Imports Made here"""
from classes import *


input_location = './doc/users.txt'
output_location = './doc/info.txt'
all_users = read(input_location)
# total_users = len(all_users)
for user in all_users:
    current_user = str(user)
    log_data = {user,fetch_details(current_user)}
write(output_location, log_data)



# print("Profile :",url, end=" \n")
# print("Image Url"," :",profile_image, end=" \n")
# print(total_repos,end=" \n")
# print(contributions)