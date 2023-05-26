from bs4 import BeautifulSoup
import requests

htmlText = requests.get('https://buff.163.com/market/csgo#tab=selling&page_num=1').text
soup = BeautifulSoup(htmlText, 'html.parser')
itemUL = soup.find('ul')
print(itemUL.encode('utf-8'))
# print(itemUL.encode('utf-8', errors="ignore"))





































# jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
# for job in jobs:
#     publishedDate = job.find('span', class_ = 'sim-posted').span.text
#     if 'few' in publishedDate:
#         companyName = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
#         skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
#         moreInfo = job.header.h2.a["href"]

#         print(f"COMPANY NAME: {companyName.strip()}")
#         print(f"REQUIRED SKILLS: {skills.strip()}")
#         print(f"LINK TO JOB: {moreInfo}")

#         print("")
#         print("")