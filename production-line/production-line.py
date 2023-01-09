# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 17:44:10 2023

@author: wifry
"""

import csv

data = []

with open("./inputs/level_1/level_1_1.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    data.append(row)
    
n = int(data[0][0])
threshold = int(data[1][0])
pixel_values = data[2]
valid_images = 0
label_array = []
print("threshold: " + str(threshold))
count = 0


for j, image in enumerate(data[2:]):
    non_zero_pixels = 0
    naughty_pixels = 0
    for i, pixel in enumerate(data[j+2]):
        if int(pixel) != 0:
            non_zero_pixels += 1
        if int(pixel) <= threshold and int(pixel) != 0:
            spleb.append(int(pixel))
            naughty_pixels += 1
        count += 1
    if naughty_pixels <= non_zero_pixels/2:
        valid_images += 1
        
    print("image " + str(j+1))
    print("non-zero pixels in image: " + str(non_zero_pixels))
    print("max allowed naughty pixels: " + str(non_zero_pixels/2))
    print("naughty pixels in image " + str(j+1) + " : " + str(naughty_pixels))
    print(count)
    print("\n")
    
            
        
print(str(valid_images))
