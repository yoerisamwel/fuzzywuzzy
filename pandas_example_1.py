import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# creating the dictionaries
dict1 = {'name': ["aparna", "pankaj", "Geeku",
                  "geeks for geeks"]}

dict2 = {'name': ["aparn", "arup", "Pankaj",
                  "geeks for for geeks",
                  "geeks for geeks", "Geek"]}

# converting to pandas dataframes
dframe1 = pd.DataFrame(dict1)
dframe2 = pd.DataFrame(dict2)

# empty lists for storing the matches
# later
mat1 = []
mat2 = []
p = []

# printing the pandas dataframes
print("First dataframe:\n", dframe1,
      "\nSecond dataframe:\n", dframe2)

# converting dataframe column
# to list of elements
# to do fuzzy matching
list1 = dframe1['name'].tolist()
list2 = dframe2['name'].tolist()

# taking the threshold as 80
threshold = 80

# iterating through list1 to extract
# it's closest match from list2
for i in list1:
    mat1.append(process.extractOne(
        i, list2, scorer=fuzz.token_set_ratio))
dframe1['matches'] = mat1

# iterating through the closest matches
# to filter out the maximum closest match
for j in dframe1['matches']:
    if j[1] >= threshold:
        p.append(j[0])
    mat2.append(",".join(p))
    p = []

# storing the resultant matches back
# to dframe1
dframe1['matches'] = mat2
print("\nDataFrame after Fuzzy matching using token_set_ratio():")
dframe1