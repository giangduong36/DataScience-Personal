# Revisit Python Fundamentals

aTuple = (1, 2, 3)
aList = [1, 2, 3]
aList.append("hello")
print(aList)
print([1, 2] + [3, 4])  # Concatenate list
print([1] * 3)  # Repeat lists

# String
x = "This is a string"
print(x + str("!"))
print(x[-1])  # Last element of a string
print(x[-5:-1])  # Slice starting from the 5th element from the end and stopping before the last element
print(x.split(' ')[0])

# Convenient string formatting
mail_record = {'name': 'Christopher Brooks', 'mail': 'brooksch@umich.edu'}

mail_statement = '{}\'s email is  {}'

print(mail_statement.format(mail_record['name'], mail_record['mail']))

# CSV files
import csv

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

print(mpg[:1])
print(len(mpg))  # Number of rows
print(mpg[0].keys())  # List of columns
print(sum(float(d['cty']) for d in mpg)/len(mpg))  # Find the average of a column
print(set(d['cyl'] for d in mpg))  # Unique values in a column

# Date and Time

import datetime as dt
import time as time
print(time.time())  # current time
dtnow = dt.datetime.fromtimestamp(time.time())
print(dtnow)  # Datetime now: dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second

# Lambda
my_function = lambda a, b: a*b
print(my_function(2,10))

# List comprehension
my_list = [num for num in range(0,10) if num % 2 == 0]
print(my_list)

