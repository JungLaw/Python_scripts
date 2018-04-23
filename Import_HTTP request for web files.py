"""
(1) Performing HTTP requests in Python using urllib
  Task: perform a GET request to extract information from our teach page; 
        package and send the request and then catch the response.
"""

# Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "http://www.datacamp.com/teach/documentation"

# Package the GET request to the url using Request()
request = Request(url)

# Send request and catch the response in the variable 'response' with the function urlopen().
response = urlopen(request)

# Print the datatype of response
print(type(response))           # OUTPUT: <class 'http.client.HTTPResponse'>

# Close the response!
response.close()




"""
(2) Printing HTTP request results in Python using urllib
  Task: 
  - Send the request and catch the response in the variable response with the function urlopen().
  - Extract the response using the read() method and store the result in the variable html.
  - Print the string html.
  - Hit submit to perform all of the above and to close the response
  
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
html = response.read()      # Returns the html as a string

# Print the html
print(html)

# Close the response
response.close()




"""
(3) Performing HTTP requests in Python using 'requests'
  NOTE: 'requests' requires less code than 'urlopen'; don't have to close out
        the output is more reader-friendly
 
  
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





