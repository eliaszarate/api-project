########################################################
# DISCLAIMER: FOR EDUCTAIONAL PURPOSES ONLY!
# The following program parses 3 job recruiting websites
# accoring to the users input and returns a list of open
# positions for the user to apply. (This is an example 
# program only with no application) 
#######################################################

import requests
import logging as log #Reminder: Put this is the API
from bs4 import BeautifulSoup


# Get users job search
getJobPosition  = input("What position are you looking for? \n")
#getJobRole = input("What Role are you looking for?") # To implement
getUserZip = input ("Enter your 5 digit zip code \n")

if len(getUserZip) != 5: 
    getUserZip = input("Invalid zip code. Please enter a 5 digit zip code: \n")

# Example: https://www.monster.com/jobs/search/?q=Mechnical&where=95111
URL_monster = 'https://www.monster.com/jobs/search/?q=' + getJobPosition + '&where=' + getUserZip 
URL_remote = 'https://remote.co/remote-jobs/' + getJobPosition 
URL_indeed = 'https://www.indeed.com/jobs?q=' + getJobPosition + '&l=' + getUserZip

'''
print(URL_monster) # for debugging 
print(URL_remote) # for debugging
print(URL_indeed) # for debugging
'''

# Makes a web page request and returns a status code
page = requests.get(URL_monster)


#creates an object named beautiful soup to parse html input
soup = BeautifulSoup(page.content, 'html.parser')
print(page.content)

results = soup.find(id='ResultsContainer')

#print(page.text)
#print(soup.text)
#print(results.prettify())
job_elems = results.find_all('section', class_='card-content')
python_jobs = results.find_all('h2',string=lambda text: 'electric' in text.lower())

#for job_elem in job_elems:
#    title_elem = job_elem.find('h2', class_='title')
#    company_elem = job_elem.find('div', class_='company')
#    location_elem = job_elem.find('div', class_='location')
#    if None in (title_elem, company_elem, location_elem):
#        continue
#    print(title_elem.text.strip())
#    print(company_elem.text.strip())
#    print(location_elem.text.strip())
#    print()
for p_job in python_jobs:
    link = p_job.find('a')['href']
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")

