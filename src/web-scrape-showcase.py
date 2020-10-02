########################################################
# DISCLAIMER: FOR EDUCTAIONAL PURPOSES ONLY!
# The following program parses 3 job recruiting websites
# accoring to the users input and returns a list of open
# positions for the user to apply. (This is an example 
# program only with no application) 
#######################################################

import os
import numpy as np
import requests
import logging as log #Reminder: Put this is the API
from bs4 import BeautifulSoup

destinationFile = "./myjobs.txt"
linkdestinationfile = "./links.txt"


# getUserName = input("Enter you name ")


# Get users job search
getJobPosition  = input("What position are you looking for? \n")

# This will be fed into the HTML parser
sep = '-'
rest = getJobPosition.split(sep, 1)[0]
print(rest.lower())
rest = getJobPosition.lower()
print(getJobPosition)


# Get user Zip search
getUserZip = input ("Enter your 5 digit zip code \n")

while (len(getUserZip) != 5): 
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

results = soup.find(id='ResultsContainer')
job_elems = results.find_all('section', class_='card-content')
# 'electrical' in text: needs to made into a string 
searched_jobs = results.find_all('h2',string=lambda text: 'electrical' in text.lower())

f = open(destinationFile,"w")
numjobs = 0


for p_job in searched_jobs:
    link = p_job.find('a')['href']
    #print((p_job.text.strip()))
    f.write(str(p_job.text.strip()) + "\n")
    #f.write(str(link) + "\n")
    numjobs += 1
    #print(f"Please visit here to apply: {link}\n")


## Note ##
# Results from myjob.txt will be the input to the table (SQL)
# Results from myjob.link

print("Finished! Found " + str(numjobs) + " jobs for you. \n")
#print("Please see " + linkdestinationfile + " to view your job positions")
f.close()

f = open(linkdestinationfile,"w")
for p_job in searched_jobs:
    link = p_job.find('a')['href']
    f.write(str(link) + "\n")

    #print(f"Please visit here to apply: {link}\n")
f.close()

cwd = os.getcwd()
#print(cwd)

print("Please see " + cwd + " to view url links and job positions")


