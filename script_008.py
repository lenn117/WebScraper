import urllib2
from bs4 import BeautifulSoup

# Open webpage
webpage = urllib2.urlopen("http://inadaybooks.com/justiceleague/")

# Convert to BeautifulSoup
soup = BeautifulSoup(webpage, "html.parser")

# Get the contents container div
divContainer = soup.find("div", {"id":"container"})
divBlock = divContainer.findAll("div", {"class":"block"})
divSep = divBlock[3].findAll("div", {"class":"separator"})
print divSep