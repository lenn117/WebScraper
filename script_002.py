import urllib2
from bs4 import BeautifulSoup

# Open webpage
webpage = urllib2.urlopen("http://inadaybooks.com/justiceleague/")

print BeautifulSoup(webpage)