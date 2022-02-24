import string
import pandas as pd
pd.set_option('display.max_colwidth', None)
df = pd.read_csv('jeopardy_starting/jeopardy.csv')
# print(df.columns)
df = df.rename(columns={
    'Show Number': 'Show Number',
    ' Air Date': 'Air Date',
    ' Round': 'Round',
    ' Category': 'Category',
    ' Value': 'Value',
    ' Question': 'Question',
    ' Answer': 'Answer'
})
# print(df.columns)

# Write a function that filters the dataset for questions that contains 
# all of the words in a list of words. For example, when the list 
# ["King", "England"] was passed to our function, the function returned 
# a DataFrame of 152 rows. Every row had the strings "King" and "England" 
# somewhere in its " Question".

# Note that in this example, we found 152 rows by filtering the entire 
# dataset. You can download the entire dataset at the start or end of 
# this project. The dataset used on Codecademy is only a fraction of the 
# dataset so you won’t find as many rows.

# Test your function by printing out the column containing the question 
# of each row of the dataset.

def in_question(string_list):
    template = '(?=.*'
    search_for = ''
    for i in range(len(string_list)):
        search_for += template + string_list[i] + ')' 
    new_df = df[df.Question.str.contains('|'.join([search_for]))]
    return new_df
    print(search_for)

# print(['this', 'a'] in 'Hello this is a test')
# print()
answer = in_question(['King', 'England'])
print(answer.Question.head())
# searchfor = ['(?=.*King)(?=.*England)']
# new_df = df[df.Question.str.contains('|'.join(searchfor))]
# print(new_df.Question.head())
# new_df.style
# print(new_df.head().Question)