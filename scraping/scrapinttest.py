# from turtle import clear
import os
import requests
from bs4 import BeautifulSoup
import urllib.parse
from pathlib import Path

# load_url = "http://python.cyber.co.kr/pds/books/python2nd/test1.html"
load_url = "https://hosupark.github.io/mechanimalinfo"
# load_url = "https://entertain.naver.com/home"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# print(soup.find("title").text)
# print(soup.find("h2").text)
# print(soup.find("h1").text)

# with open("mechanimalinfo.txt", "w") as f:
#     f.write(html.text)

# mlist = soup.find(class_="rank_lst")

# linklist_file = open("./PythonWorkspace/scraping/link_list.txt", "w")

# for element in mlist.find_all("a"):
#     print(element.text)
#     url = element.get("href")
#     link_url = urllib.parse.urljoin(load_url, url)
#     print(link_url)
#     linklist_file.write(element.text + "\n")
#     linklist_file.write(link_url + "\n")
#     linklist_file.write("\n")

# linklist_file.close()

imagefolder = Path("./PythonWorkspace/scraping/Image")
imagefolder.mkdir(exist_ok=True)
os.chdir(imagefolder)

for element in soup.find_all("img"):
    url = element.get("href")
    imgname = element.get("src")
    image_url = urllib.parse.urljoin(load_url, url) + "/" + imgname
    print(image_url)
    imgdata = requests.get(image_url)
    
    with open(imgname, "wb") as f:
        f.write(imgdata.content)
