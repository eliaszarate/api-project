from django.shortcuts import render
from django.http import HttpResponse
import os

get_job_file = "./../src/myjobs.txt"

file_count = open(get_job_file,"r")


numjobs = 0
for i in file_count:
    numjobs += 1

number = str(numjobs)

def index(request): 
    return HttpResponse("Hello, Welcome to the front page, the web service has found " + number +  "possible positions for you to apply.\n"
           + "Please see /jobs for the title of the jobs and /jobs/links for the url links." )




#file_content = open(./../scr/jobs.txt, 'r')

#response = HttpResponse(targetfiles.read(), mimetime='text/plain') 
def read_file(request):
    f = open('./../src/myjobs.txt', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")

#response = HttpResponse(targetfiles.read(), mimetime='text/plain') 
def read_links(request):
    f = open('./../src/links.txt', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")

# Create your views here.
