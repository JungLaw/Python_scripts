"""
<Turning a webpage into data using BeautifulSoup>

(1) Parsing HTML with BeautifulSoup
  Task:  use the BeautifulSoup package to parse, prettify and extract information from HTML. 
"""

# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
"""Package the request to the URL, send the request and catch the response with a single function requests.get(), assigning the response to the variable r."""

r = requests.get(url)

# Extracts the response as html: html_doc
""" Use the text attribute of the object r to return the HTML of the webpage as a string; store the result in a variable html_doc."""

html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)  # presents page in a readable manner
soup.body.text                  # test code

# Prettify the BeautifulSoup object using .prettify() method: pretty_soup
pretty_soup = soup.prettify()

# Print the response
print(pretty_soup)

# Try later
bold = soup.finaAll('b') # find all bold text and return a list
print(bold)

================================================

"""
(2) Turning a webpage into data using BeautifulSoup: getting the text

"""

# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Get the title of Guido's webpage: guido_title
## Extract the title from the HTML soup using the attribute title
guido_title = (soup.title)                             ## Incorrect -> guido_title = soup.title()

# Print the title of Guido's webpage to the shell
print(guido_title)

# Get Guido's text: guido_text
## Extract the text from the HTML soup using the method get_text()
guido_text = (soup.get_text())                         ## Incorrect-> guido_text = soup.get_text()   

# Print Guido's text to the shell
print(guido_text)


==========================================

"""
(3) Getting the hyperlinks
 
"""

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

=========================

### Try Later

# find all links in the document

soup.findAll(id-"para2")[0].text
soup.findAll(['b', 'p'])

soup.findAll({'b': True, 'p': True})


# 
links = soup.find('a')   # returns 1st match it gets -use findAll

print(links['href'] + " is the url and " + links.text + " is the text")


### In [7]: links = soup.find('a') 
### In [8]: print(links['href'] + " is the url and " + links.text + " is the text")
pics.html is the url and  is the text



# Use find in various ways 

# findParents, findNextSiblings, findPreviousSiblings
# findNext, findPrevious and findAllNext and findAllPrevious

