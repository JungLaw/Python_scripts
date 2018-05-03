
===========================
(1) INDEXING MULTIPLE LEVELS OF A MULTI-INDEX (INNERMOST INDEX)

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
