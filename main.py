"""Imports Made here"""
import requests
from bs4 import BeautifulSoup as bs

"""Input and Initializing done here"""
github_user = input('Input GitHub User: \n')
url = 'https://github.com/'+github_user
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


print("Profile :",url, end=" \n")
print("Image Url"," :",profile_image, end=" \n")
print(total_repos,end=" \n")
print(contributions)