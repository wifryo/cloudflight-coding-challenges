# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 12:06:28 2023

@author: wifry
"""

import csv

data = ""

with open("./inputs/level1/level1-3.in", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    data = row
    
data = data[0].split()
rows = int(data[0])
cols = int(data[1])
number_of_positions = int(data[2])
positions = data[3:]
output = []

for position in positions:
    position = int(position)
    if position%cols == 0:
        row = int(position/cols - 1)
    else:
        row = position//cols
    column = position - (row * cols)
    output.append(row+1)
    output.append(column)
    print("position: " + str(position) + ", row: " + str(row+1) + ", column: " + str(column))
    
outputstring = ""
for i, item in enumerate(output):
    outputstring += str(item) 
    if i < len(output)-1:
        outputstring += " "
    
print(outputstring)