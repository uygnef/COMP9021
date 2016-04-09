import sys
import os
import csv

filename = 'HNP_Data.csv'
indicator_of_interest = 'Newborns protected against tetanus (%)'
first_year = 1960
number_of_years = 56
max_value = None
countries_for_max_value_per_year = {}

with open(filename) as f:
    reader = csv.reader(f)
    s=(f.readline()).split(',')
    C=[]
    max_value=''
    for line in reader:
        if line[2] == indicator_of_interest:
            i=4
            while 4<=i<len(line):
                if line[i] > max_value:         
                    max_value=line[i]
                    max_value_per_year=[]
                    max_value_per_year.append([line[0],s[i]])
                elif line[i]==max_value and max_value !='':
                    max_value_per_year.append([line[0],s[i]])
                i=i+1
    p=0
    for data in max_value_per_year:
        if not data[1] in countries_for_max_value_per_year:
            countries_for_max_value_per_year[data[1]]=[data[0]]
        else:
            countries_for_max_value_per_year[data[1]].append(data[0])
for year in sorted(countries_for_max_value_per_year):
        print('    {}: {}'.format(year, countries_for_max_value_per_year[year]))
                    
                    
                
            
