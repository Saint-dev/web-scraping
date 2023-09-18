from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

name = input("digite o site: ")
tag = input("Digite a tag: ")
clss = input("digite a class: ")
try:
    html = urlopen(name)
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    res = BeautifulSoup(html.read(),"html5lib")
    tags = res.findAll(tag, {"class": clss})
    for tag in tags:
        print(tag.getText())