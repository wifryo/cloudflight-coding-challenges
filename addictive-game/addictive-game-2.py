# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 12:06:28 2023

@author: wifry
"""

import csv
import numpy as np

data = ""

with open("./inputs/level2/level2-3.in", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    data = row
    
data = data[0].split()
rows = int(data[0])
cols = int(data[1])
number_of_positions = int(data[2])
positions_colours = data[3:]
parsed_data = []

# Parse data into array of dicts
for i, position in enumerate(positions_colours):
    if i%2 == 0:
        position = int(position)
        if position%cols == 0:
            row = int(position/cols - 1)
        else:
            row = position//cols
        column = position - (row * cols)
        colour = int(positions_colours[i+1])
        parsed_data.append({"row": row+1, "column": column, "colour": colour})
        print("position: " + str(position) + ", row: " + str(row+1) + ", column: " + str(column) + ", colour: " + str(colour))
        
number_of_colours = number_of_positions//2

colour_pairs = []

# Sort data into pairs of positions with matching colours
for colour in range(number_of_colours):
    colour = colour+1
    new_pair = []
    for i, position in enumerate(parsed_data):       
        if parsed_data[i]["colour"] == colour:
            new_pair.append(position)            
    colour_pairs.append(new_pair)

distances = []

for pair in colour_pairs:
    distances.append((np.abs(pair[0]["row"] - pair[1]["row"])) + (np.abs(pair[0]["column"] - pair[1]["column"])))
    
            
outputstring = ""
for i, item in enumerate(distances):
    outputstring += str(item) 
    if i < len(distances)-1:
        outputstring += " "
    
print(outputstring)


