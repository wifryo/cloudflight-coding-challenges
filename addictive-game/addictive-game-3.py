# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 12:06:28 2023

@author: wifry
"""

import csv
import numpy as np

data = ""



with open("./inputs/level3/level3-1.in", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    data = row

# Parse data into relevant lists & variables
data = data[0].split()
rows = int(data[0])
cols = int(data[1])
number_of_positions = int(data[2])
number_of_colours = number_of_positions//2
end_of_positions_index = number_of_positions*2+3
positions_colours = data[3:end_of_positions_index]
number_of_paths = data[end_of_positions_index]
path_data = data[end_of_positions_index+1:]

parsed_data = []

# Parse position data into array of dicts
# Note: rows begin with 0 but output is expected to begin with 1
for i, position in enumerate(positions_colours):
    if i%2 == 0:
        position = int(position)
        if position%cols == 0:
            row = int(position/cols - 1)
        else:
            row = position//cols
        column = position - (row * cols)
        colour = int(positions_colours[i+1])
        parsed_data.append({"row": row, "column": column, "colour": colour})
        

colour_pairs = []

# Sort position data into pairs of positions with matching colours
for colour in range(number_of_colours):
    colour = colour+1
    new_pair = []
    for i, position in enumerate(parsed_data):       
        if parsed_data[i]["colour"] == colour:
            new_pair.append(position)            
    colour_pairs.append(new_pair)

distances = []

# Create array of Manhattan distances
for pair in colour_pairs:
    distances.append((np.abs(pair[0]["row"] - pair[1]["row"])) + (np.abs(pair[0]["column"] - pair[1]["column"])))
    
# Parse path data
colour = int(path_data[0])
starting_position = int(path_data[1])
length = int(path_data[2])
path = path_data[3:]
current_column = 0
current_row = 0

# Find initial column/row from position
if starting_position%cols == 0:
    starting_row = int(starting_position/cols - 1)
else:
    starting_row = starting_position//cols
starting_column = starting_position - (starting_row * cols)

print("starting row: " + str(starting_row))
print("starting column: " + str(starting_column))

# Find initial colour
starting_colour = 0
for pair in colour_pairs:
    for position in pair:
        if position["row"] == starting_row and position["column"] == starting_column:
            starting_colour = position["colour"]

# Intialise some variables
all_steps = []
current_row = starting_row
current_column = starting_column

#Follow path, ha ha
for step in path:
    match step:
        case 'N':
            current_row -= 1
        case 'E':
            current_column += 1
        case 'S':
            current_row += 1
        case 'W':
            current_column -= 1
    all_steps.append({"row": current_row, "column": current_column})

# Variable to store index of invalid step (if applicable)
invalidity_index = 0

# Check if final position matches the colour of initial position
colour_match = False

for i, pair in enumerate(colour_pairs):
    for position in pair:
        if position["row"] == current_row and position["column"] == current_column and position["colour"] == starting_colour:
            print("Colour matches")
            colour_match = True
    

hit_wrong_colour = False
out_of_bounds = False
hit_self = False

for i, step in enumerate(all_steps):
    # Check if any step goes out of bounds
    if step["row"] < 0 or step["row"] > rows or step["column"] < 0 or step["column"] > cols:
        print("Out of bounds")
        out_of_bounds = True
        
        # If invalidity index has already been assigned, but current invalid index is smaller, use smaller value
        if invalidity_index > i + 1:
            invalidity_index = i + 1
        elif invalidity_index == 0:
            invalidity_index = i + 1

    # Check if any step hits a point of another colour
    for position in parsed_data:
        if step["row"] == position["row"] and step["column"] == position["column"] and starting_colour != position["colour"]:
            hit_wrong_colour = True
            # If invalidity index has already been assigned, but current invalid index is smaller, use smaller value
            if invalidity_index > i + 1:
                invalidity_index = i + 1
            elif invalidity_index == 0:
                invalidity_index = i + 1
            

# Check if any step hits a previous step
for i, step in enumerate(reversed(all_steps)):
    index = len(all_steps) - i - 1
    #print("index: " + str(index) + ", step: " + str(step))
    if step["row"] == starting_row and step["column"] == starting_column:
        hit_self = True
        # If invalidity index has already been assigned, but current invalid index is smaller, use smaller value
        if invalidity_index > index + 1:
            invalidity_index = index + 1
        elif invalidity_index == 0:
            invalidity_index = index + 1
    for j, steb in enumerate(all_steps[:index]):
        #print("subindex: " + str(j) + ", step: " + str(steb))
        if step == steb:
            hit_self = True
            # If invalidity index has already been assigned, but current invalid index is smaller, use smaller value
            if invalidity_index > index + 1:
                invalidity_index = index + 1
            elif invalidity_index == 0:
                invalidity_index = index + 1
        
print("colour match: " + str(colour_match) + ", hit wrong colour: " + str(hit_wrong_colour) + ", out of bounds: " + str(out_of_bounds) + ", hit self: " + str(hit_self))
validity = -1
if colour_match and not hit_wrong_colour and not hit_self and not out_of_bounds:
    validity = 1

# Output is "code index/length" where code is 1 for valid and -1 for invalid paths; index is the index of step that caused invalidity
# Otherwise if valid OR if the path ends in the wrong place return the path length
print("validity: " + str(validity))
print("invalidity index: " + str(invalidity_index))
output_string = str(validity)
second_output_term = ""
if validity == 1 or (not colour_match and not hit_wrong_colour and not hit_self and not out_of_bounds ):
    second_output_term = str(len(path))
elif validity == -1:
    second_output_term = str(invalidity_index)
output_string += " " + second_output_term
    
print(output_string)


