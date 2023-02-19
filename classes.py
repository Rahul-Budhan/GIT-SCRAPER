"""Imports Made here"""
import requests
from bs4 import BeautifulSoup as bs

def read(read_file_location):
    handle = open(read_file_location,'r')
    total_users = 0
    for line in handle:
        if line[0] =='#':
            continue
        total_users+=1
    UserNames = [str]*total_users
    handle.close()
    print(UserNames)
    return UserNames

def fetch_details(user):
    """Input and Initializing done here"""
    url = 'https://github.com/'+user
    contributions = " "
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    """data into local variables"""
    profile_image = soup.find('img',{'alt':'Avatar'})['src']
    total_repos = soup.find('span',{'class':'Counter','data-view-component':'true'})['title']
    contributions_in_last_year = (soup.find('h2',{'class':"f4 text-normal mb-2"})).text


    """Data manipulitation done to ease the output"""
    contributionsList =(contributions_in_last_year).split()
    contributions = (contributions).join(contributionsList)

    return {'profile_image':profile_image,'total_repos':total_repos,'contributions':contributions}


def write(write_file_location, details):
    handle = open(write_file_location)


    print("Profile :",url, end=" \n")
    print("Image Url"," :",profile_image, end=" \n")
    print(total_repos,end=" \n")
    print(contributions)

    