"""Imports Made here"""
import requests
from bs4 import BeautifulSoup as bs

"""Function to take input from the users.txt file"""
def get_users(read_file_location):
    handle = open(read_file_location,'r')
    data = handle.read()
    lines = data.split('\n')
    for line in lines:
        if line[0] == '#' or line[0] == ' ':
            lines.remove(line) 
    handle.close()
    return lines

"""Function to fetch data from github and convert data into details"""
def fetch_details(user,output_location):
    """Input and Initializing done here"""
    url = 'https://github.com/'+user
    contributions = " "
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    total_repos=""
    """data into local variables within try except to handle exceptions and enter data accordingly """
    try:
        try:
            profile_image = soup.find('img',{"alt":"Avatar"})['src']
        except:
            profile_image = soup.find('img',{"itemprop":"image"})['src']  
    except:
        profile_image = "Not Found"
    try:
        name = soup.find('span',{"class":"p-name vcard-fullname d-block overflow-hidden"}).text
    except:
        name = " "
    total_repos=""
    try:
        repo_str = soup.find('a',{"data-tab-item":"repositories"}).text
        x=repo_str.split()
        for i in x:
            total_repos = i +' '+ total_repos
    except:
        repo_str = soup.find('span',{"class":"Counter js-profile-repository-count"})
    try:
        contributions_in_last_year = (soup.find('h2',{'class':"f4 text-normal mb-2"})).text
        """Data manipulitation done to ease the output"""
        contributionsList =(contributions_in_last_year).split()
        contributions = (contributions).join(contributionsList)
        cont = True
    except:
        cont = False
    write_into_file(output_location,[name,user,url,profile_image,total_repos,contributions],cont,False)

"""Function to write data into output file"""
def write_into_file(write_file_location,details,cont,done):
    if done:
        with open(write_file_location,'a') as file:
            file.write(details)
            return

    if not cont:
        details.pop()
    with open(write_file_location,'a') as file:
        for line in details:
            file.write(line)
            file.write("\n")
        file.write("\n")

    