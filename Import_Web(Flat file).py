""" 
(1) How to Import/Download an online flatfile in Python
    Task: import a file from the web, save it locally and load it into a DataFrame 
"""

# Import a function called urlretrieve from the request subpackage of the urllib package, 
from urllib.request import urlretrieve

# Assign the relevant URL as a string to the variable url.
url = 'http:// website address.csv'

# Use the urlretrieve function to write the contents of the url to a file 'winequality-white dot csv' (note: saving the file locally).
urlretrieve(url, 'winequality-white.csv')

# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())



"""
(2) Opening and reading flat files from the web
Task: load a file from the web into a DataFrame without first saving it locally, you can do that easily using pandas. 
"""

# Packages
import matplotlib.pyplot as plt
import pandas as pd

# URL of the file -> Assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Read file into a DataFrame: df
#   - Read file into a DataFrame df using pd.read_csv(); the separator in the file is ';'

df = pd.read_csv(url, sep = ";")

# Print the head of the DataFrame (note: exactly the same output as above)
print(df.head())

# Plot first column of df
#   - plot histogram of the first feature in the DataFrame df.
pd.DataFrame.hist(df.ix[:, 0:1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()
