import webbrowser
import requests, bs4, sys
from html5print import HTMLBeautifier
webreq=requests.get("https://www.google.com/search?q=" + " ".join(sys.argv[1:]))
webbrowser.open("https://www.google.com/search?q=" + " ".join(sys.argv[1:]))
status=webreq.raise_for_status()
soupObject=bs4.BeautifulSoup(webreq.text,'html5lib')
results=soupObject.find_all("div",class_="kCrYT")
links=[]
for i in results:
	if i.find(class_="BNeawe s3v9rd AP7Wnd")==None:
		links2=i.find("a")
		if not links2==None:
			links.append(links2)
linktoOpen=min(6,len(links))
for i in range (0,linktoOpen):
	webbrowser.open("https://www.google.com"+links[i].get("href"))
	#print("Mahin")
