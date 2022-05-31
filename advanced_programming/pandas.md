# Pandas

## DataFrame (rows x cols)

## Series (rows x 1)

- Ceating dataframes/series
  - **pd.DataFrame(dict)** - from a dict, keys for columns names, values for data as lists
  - **pd.DataFrame(np.random.rand(20,5))** - 20 rows and 5 columns of random floats
  - **pd.Series(my_list)** - creates a series from an iterable my_list
  - etc...
- Read from file
  - **pd.read_csv(filename)** - from a csv file
  - **pd.read_table(filename)** - from a delimited text file (like TSV)
  - **pd.read_excel(filename)** - from an Excel file
- Indexing/selecting
  - **df[col]** or **df.col**- returns column with label col as Series
  - **df[[col1, col2]]** - returns Columns as a new DataFrame
  - **s.iloc[0]** - selection by position (integer position based)
  - **s.loc[0]** - selection by index (label based)
  - **df.loc[:, :]** and **df.iloc[:, :]** - First argument represents the number of rows and the second for columns
  - etc...
- Viewing
  - **df.head(n)** - first n rows of the DataFrame [__replace head with tail__, you know what you will get]
  - **df.shape** - number of rows and columns
  - **df.info()** - index, datatype and memory
  - **df.describe()** - summary statistics for numerical columns
  - etc...
- Renaming

  - **df.columns = ['a','b','c']** - Renames columns

- Data cleaning

  - **df.drop([col1, col2, col3], inplace = True, axis=1)** - Remove set of column(s)
  - **df.isnull()** - Checks for null Values, Returns Boolean DataFrame
  - **df.isnull().any()** - Returns boolean value for each column, gives True if any null value detected corresponding to that column
  - **df.isnull().sum()** - Returns number of missing values for each column
  - **df.dropna()** - Drops all rows that contain null values
  - **df.dropna(axis=1)** - Drops all columns that contain null values
  - **df.fillna(x)** - Replaces all null values with x
  - **s.replace(1,'one')** - Replaces all values equal to 1 with 'one'
  - **s.replace([1,3], ['one','three'])** - Replaces all 1 with 'one' and 3 with 'three'
  - **df.rename(columns = lambda x: x + '\_1')** - Mass renaming of columns
  - **df.rename(columns = {'old_name': 'new_name'})** - Selective renaming
  - **df.rename(index = lambda x: x + 1)** - Mass renaming of index
  - **df[new_col] = df.col1 + ', ' + df.col2** - Add two columns to create a new column in the same DataFrame

- Apply & Filter
  - **df[df[col] > 0.5]** - Rows where the values in col > 0.5
  - **df[(df[col] > 0.5) & (df[col] < 0.7)]** - Rows where 0.7 > col > 0.5
  - **df[col].apply(lambda x)** - applies a transformation to each item in a column
  - **df.apply(np.mean)** - Applies a function across each column
  - **df.apply(np.max, axis=1)** - Applies a function across each row
  - **df.applymap(lambda arg(s): expression)** - Apply the expression on each value of the DataFrame
  - **df[col].map(lambda arg(s): expression)** - Apply the expression on each value of the column col
  - **Query** - eg: `sortedApps = df.query('Rating >= 1 and Rating < 2')`
- Sort
  - **df.sort_values(col1)** - Sorts values by col1 in ascending order
  - **df.sort_values(col2,ascending=False)** - Sorts values by col2 in descending order
  - **df.sort_values([col1,col2],ascending=[True,False])** - Sorts values by col1 in ascending order then col2 in descending order
- Group by
  - **df.groupby(col)** - Returns a groupby object for values from one column
  - **df.groupby([col1,col2])** - Returns a groupby object values from multiple columns
  - **df.groupby(col1)[col2].mean()** - (Aggregation) Returns the mean of the values in col2, grouped by the values in col1
  - **df.pivot_table(index=col1,values=[col2,col3],aggfunc=mean)** - Creates a pivot table that groups by col1 and calculates the mean of col2 and col3
- Joining & Merging
  - **df1.append(df2)** - Adds the rows in df1 to the end of df2 (columns should be identical)
  - **pd.concat([df1, df2], axis=1)** - Adds the columns in df1 to the end of df2 (rows should be identical)
  - **pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=True)** - where
    - left − A DataFrame object.
    - right − Another DataFrame object.
    - how − One of 'left', 'right', 'outer', 'inner'. Defaults to inner. Each method has been described below.
    - on − Columns (names) to join on. **Must be found in both** the left and right DataFrame objects.
    - left_on − Columns from the left DataFrame to use as keys.
    - right_on − Columns from the right DataFrame to use as keys.
    - left_index − If True, use the index (row labels) from the left DataFrame as its join key(s). In case of a DataFrame with a MultiIndex (hierarchical), the number of levels must match the number of join keys from the right DataFrame.
    - right_index − Same usage as left_index for the right DataFrame.
    - sort − Sort the result DataFrame by the join keys in _lexicographical order_. Defaults to True, setting to False will improve the performance substantially in many cases.
