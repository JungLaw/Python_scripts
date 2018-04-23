'''
Use BeautifulSoup package to parse, prettify and extract information from HTML, then extract information from HTML soup. 

Task: 
Create the HTML response object html_doc.
Soupify it using the function BeatifulSoup() and to assign the resulting soup to the variable soup.
Extract the title from the HTML soup soup using the attribute title and assign the result to guido_title.
Print the title of Guido's webpage to the shell using the print() function.
Extract the text from the HTML soup using the method get_text() and assign to guido_text.
Hit submit to print the text from Guido's webpage to the shell.

'''
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
soup = BeautifulSoup(html_doc)

# Get the title of Guido's webpage: guido_title
guido_title = (soup.title)

# Print the title of Guido's webpage to the shell
print(guido_title)                                      # <title>Guido's Personal Home Page</title>

# Get Guido's text: guido_text
guido_text = (soup.get_text())                          

# Print Guido's text to the shell
print(guido_text)


'''


'''
