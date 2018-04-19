"""
(1) Performing HTTP requests in Python using urllib
  Task: perform a GET request to extract information from our teach page; 
        package and send the request and then catch the response.
"""

# Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "http://www.datacamp.com/teach/documentation"

# This packages the request: request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

# Print the datatype of response
print(type(response))

# Close the response!
response.close()

# <class 'http.client.HTTPResponse'>


"""
(2) Printing HTTP request results in Python using urllib
  Task: 
  
"""

# Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "http://www.datacamp.com/teach/documentation"

# This packages the request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

# Extract the response: html
html = response.read()

# Print the html
print(html)


"""
(3) Performing HTTP requests in Python using 'requests'
  Task: 
  
"""

# Import package
import requests

# Specify the url: url
url = "http://www.datacamp.com/teach/documentation"

# Packages the request, send the request and catch the response: r
  ## Package the request to the URL, send the request and catch the response with a single function requests.get(),
r = requests.get(url)

# Extract the response: text
  ## Use the text attribute of the object r to return the HTML of the webpage as a string.
text = r.text

# Print the html
print(text)





