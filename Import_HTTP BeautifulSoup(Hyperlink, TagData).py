'''
Use BeautifulSoup to obtain a list of all hyperlinks (using tags)

TASK:
Use the method find_all() to find all hyperlinks in soup, remembering that 
		○ hyperlinks are defined by the HTML tag <a>; 
		○ store the result in the variable a_tags.
The variable a_tags is a results set: your job now is to enumerate over it using a for loop and print the actual URLs of the hyperlinks; 
to do this, for every element link in a_tags, you want to print() link.get('href').

'''

# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Print the title of Guido's webpage
print(soup.title)

# Find all 'a' tags (which define hyperlinks): a_tags
a_tags = soup.find_all('a')                       # hyperlinks are defined by the HTML tag <a>

# Print the URLs to the shell
for link in a_tags:
    print(link.get('href'))
