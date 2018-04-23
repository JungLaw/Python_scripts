""" 
(1) Import/Download an online flatfile in Python
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
Task: load a file from the web into a DataFrame without first saving it locally.
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


"""
(3) Importing non-flat files (Excel) from the web
    Task: 
    Note: (a) in order to import all sheets you need to pass None to the argument 'sheetname'
    (b) the output of pd.read_excel() is a Python dictionary with 
    sheet names as keys and 
    corresponding DataFrames as corresponding values.
"""

# Import package
import pandas as pd

# Assign url of file: url
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# Read in all sheets of Excel file: xl
xl = pd.read_excel(url,sheetname = None )       # 'sheetname = None' to import all sheets in excel file 

# Print the sheetnames to the shell
print(xl.keys())

# Print the head of the first sheet (using its name, NOT its index)
print(xl['1900'].head())

