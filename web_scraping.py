import requests 
from bs4 import BeautifulSoup
import csv 
from itertools import zip_longest

job_title = []
company_name = []
locations_name = []
job_skill = []
links = []
dates= []


# 2nd step use requests use requests to fetch the url
result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")

#3rd step save page content/markup
src = result.content
# print(src)

# 4th step create soup object parse 
soup = BeautifulSoup(src , "lxml")
# print(soup)


# 5th step find the elements containing info we eed 
#-- job titles , job skills , company names , location names 

job_titles = soup.find_all("h2" , {"class":"css-m604qf"})    
company_names = soup.find_all("a" , {"class":"css-17s97q8"})  
locations_names = soup.find_all("span" , {"class":"css-5wys0k"})
job_skills = soup.find_all("div" , {"class":"css-y4udm8"})
 

# 6th step loop over returned lists to extract needed info into other lists
for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    
    # here are relative links 
    # X.com+ "/jobs/... "

    links.append("https://wuzzuf.net" + job_titles[i].find("a").attrs['href'])
    company_name.append(company_names[i].text)
    locations_name.append(locations_names[i].text)
    job_skill.append(job_skills[i].text)
 
 

# 7th step create csv file and fill it with values
file_list = [job_title , company_name , locations_name , job_skill ,links]
exported = zip_longest( *file_list)

with open("C:/Users/moayy/OneDrive/Desktop/webscraping/job_search_scrape.csv", "w" , newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["job title" , "company name", "location" , "skills" ,"links"])
    wr.writerows(exported)
 

