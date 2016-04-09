# Uses Heath Nutrition and Population statistics, avalaible at
# http://datacatalog.worldbank.org, stored in the file HNP_Data.csv,
# assumed to be stored in the working directory.
# Prompts the user for an Indicator Name. If it exists and is associated with
# a numerical value for some countries or categories, for some the years 1960-2015,
# then finds out the maximum value, and outputs:
# - that value;
# - the years when that value was reached, from oldest to more recents years;
# - for each such year, the countries or categories for which that value was reached,
#   listed in lexicographic order.
# 
# Written by *** and Eric Martin for COMP9021


import sys
import os
import csv


filename = 'HNP_Data.csv'
if not os.path.exists(filename):
    print('There is no file named {} in the working directory, giving up...'.format(file_name))
    sys.exit()

indicator_of_interest = input('Enter an Indicator Name: ')

first_year = 1960
number_of_years = 56
max_value = None
countries_for_max_value_per_year = {}

with open(filename) as csvfile:
    reader = csv.reader(csvfile)
    s=(csvfile.readline()).split(',')
    C=[]
    max_value=-5
    max_value_per_year=[]
    for line in reader:
        if line[2] == indicator_of_interest:
            i=4
            while 4<=i<len(line):
                if line[i]=='':
                    i=i+1
                    continue
                if float(line[i].replace(',','')) > float(max_value):
                    max_value=line[i]
                    max_value_per_year=[]
                    max_value_per_year.append([line[0],s[i]])
                elif line[i]==max_value and max_value !='':
                    max_value_per_year.append([line[0],s[i]])
                i=i+1
        
    for data in max_value_per_year:
        if not data[1] in countries_for_max_value_per_year:
            countries_for_max_value_per_year[data[1]]=[data[0]]
        else:
            countries_for_max_value_per_year[data[1]].append(data[0])
    if max_value==-5:
        max_value = None
            
if max_value == None:
    print('Sorry, either the indicator of interest does not exist or it has no data.')
else:
    print('The maximum value is:', max_value)
    print('It was reached in these years, for these countries or categories:')
    for year in sorted(countries_for_max_value_per_year):
        print('    {}: {}'.format(year, countries_for_max_value_per_year[year]))
