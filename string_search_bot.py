#!/usr/bin/python3.7
import re
import requests
import urllib.request
from threading import Thread

total_links = []
valid_urls = []
initial_count = 0
total_input = int(input('\n\n\033[1m Please enter the number of webpages you have: \033[0m '))
search_string = str.lower(input('\033[1m Enter the String you want to search: \033[0m '))
print("\n \033[1m Now, start entering your webpage links followed by pressing Enter......\033[0m \n")

while initial_count < total_input:
    input_url = input()
    total_links.append(input_url)
    initial_count += 1

input_split = int(total_input / 2)
first_stage_link = total_links[:int(input_split)]
second_stage_link = total_links[int(input_split):]

def initial(url):
    web_response = requests.get(url)
    if web_response.status_code==200:
        html_content = urllib.request.urlopen(url).read().decode('utf-8')
        matches = re.search(search_string, html_content)
        if matches:
            valid_urls.append(url)


class First_search(Thread):
    def run(self):
        for url in first_stage_link:
            try:
                initial(url)
            except:
                pass

class Second_search(Thread):
    def run(self):
        for url in second_stage_link:
            try:
                initial(url)
            except:
                pass        

first_object = First_search()
second_object = Second_search()
first_object.start()
second_object.start()
first_object.join()
second_object.join()

f = open('output.txt', 'w')
f.write('List of all the web links in which "'+ search_string+ '" is present:- \n\n')

for link in valid_urls:
    f.write(link+"\n")
f.close()

print("\n \033[1m The resultant links has been successfully exported to output.txt file, \
in your default current directory. \033[0m\n\n")
