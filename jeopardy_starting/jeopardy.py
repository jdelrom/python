import string
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)
pd.set_option('display.max_rows', None)

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
# answer = in_question(['what', 'is'])
# print(answer)
# searchfor = ['(?=.*King)(?=.*England)']
# new_df = df[df.Question.str.contains('|'.join(searchfor))]
# print(new_df.Question.head())
# new_df.style
# print(new_df.head())

# We may want to eventually compute aggregate statistics, like .mean()
# on the " Value" column. But right now, the values in that column are 
# strings. Convert the " Value" column to floats. If you’d like to, you 
# can create a new column with the float values.

# Now that you can filter the dataset of question, use your new 
# column that contains the float values of each question to find the 
# “difficulty” of certain topics. For example, what is the average 
# value of questions that contain the word "King"?

# Make sure to use the dataset that contains the float values as the 
# dataset you use in your filtering function.

def omit_comma(string):
    if string.find(',') != -1:
        index = string.find(',')
        new_string = string[:index] + string[index+1:]
        return new_string
    else:
        return string

def change_to_float(string):
    if string != 'None':
        split_str = string.split('$')
        # print(split_str)
        format_string = omit_comma(split_str[-1])
        # print(format_string)
        return float(format_string)
    else:
        return string

# df[df.Value.apply(change_to_float)]
not_null_value_df = df[df.Value != 'None']
# print(len(df))
# print(len(not_null_value_df))
# print(not_null_value_df.Value)

df['value_num'] = df.apply(lambda row: 
  change_to_float(row['Value']),
  axis=1)
  
# print(df.head())
## what is the average value of of questions that contain the word King
## write a function that does this
def average_value_word(word):
    question_df = in_question(word)
    only_values_df = question_df[question_df.Value != 'None']
    average_value = only_values_df.value_num.mean()
    return round(average_value) 

# print(average_value_word('King'))

#  Write a function that returns the count of the unique answers to all of the questions in a dataset. For example, 
# after filtering the entire dataset to only questions containing the word "King", we could then find all of the 
# unique answers to those questions. The answer “Henry VIII” appeared 3 times and was the most common answer.

def count_unique_answers(word):
    question_df = in_question(word)
    unique_df = question_df.Answer.unique()    
    return unique_df

print(count_unique_answers('King'))