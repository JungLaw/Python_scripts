(1) EXTRACTING DATA WITH A MULTI-INDEX

'''
TASK:
- Print sales.loc[['CA', 'TX']]. Note how New York is excluded.
- Print sales['CA':'TX']. Note how New York is included.
'''
# Print sales.loc[['CA', 'TX']]
sales.loc[['CA', 'TX']]

=======
(2) SETTING & SORTING A MULTI-INDEX

'''
INSTRUCTIONS
- Create a MultiIndex by setting the index to be the columns ['state', 'month'].
- Sort the MultiIndex using the .sort_index() method.
- Print the sales DataFrame. 
'''

# Reference/Checks:
  sales.index
  sales.index.names

# Set the index to be the columns ['state', 'month']: sales
sales = sales.set_index(['state', 'month'])

# Sort the MultiIndex: sales
sales = sales.sort_index()

# Print the sales DataFrame
print(sales)


========
**(3) Using .loc[] with nonunique indexes**

'''
It is always preferable to have a meaningful index that uniquely identifies each row.
Even though pandas does not require unique index values in DataFrames, it works better if the index values are indeed unique.

INSTRUCTIONS:
  * Set the index of sales to be the column 'state'.
	* Print the sales DataFrame to verify that indeed you have an index with state values.
  * Access the data from 'NY' and print it to verify that you obtain two rows.

'''
# Reference/Checks:
  sales.index

# Set the index to the column 'state': sales
sales = sales.set_index(['state'])

# Print the sales DataFrame
print(sales)

'''    month  eggs  salt  spam
state                         
CA         1    47  12.0    17
CA         2   110  50.0    31
NY         1   221  89.0    72
NY         2    77  87.0    20
TX         1   132   NaN    52
TX         2   205  60.0    55  '''

# Access the data from 'NY'
print(sales.loc['NY'])

'''    month  eggs  salt  spam
state                         
NY         1   221  89.0    72
NY         2    77  87.0    20  '''


===========================
(4) INDEXING MULTIPLE LEVELS OF A MULTI-INDEX (INNERMOST INDEX)

'''
The trickiest of all these lookups are when you want to access some inner levels of the index. 
In this case, you need to use slice(None) in the slicing parameter for the outermost dimension(s) instead of the usual : (or pd.IndexSlice). 

INSTRUCTIONS:
- Look up data for the New York column ('NY') in month 1.
- Look up data for the California and Texas columns ('CA', 'TX') in month 2.
- Look up data for all states in month 2. Use (slice(None), 2) to extract all rows in month 2.

'''
# Reference/Checks:
  sales.head()
  sales.index
  sales.index.names

# Look up data for NY in month 1: NY_month1
NY_month1 = sales.loc[('NY','1')]

# Look up data for CA and TX in 'month' 2: CA_TX_month2
CA_TX_month2 = sales.loc[(['CA','NY'],2),:]

# Look up data for all 'states' in 'month' 2: all_month2
all_month2 = sales.loc[(slice(None), 2),:]           # .loc[(tuple), rows]

'''          eggs  salt  spam
state month                  
CA    2       110  50.0    31
NY    2        77  87.0    20
TX    2       205  60.0    55'''
