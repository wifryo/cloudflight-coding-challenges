# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 11:39:31 2023

@author: wifry
"""

import numpy as np

def mars_rover():
    # Full circle test
    #input = "1.09 4 9.86 10 9.86 10 9.86 10 9.86 10"
    # Other test in brief pdf
    #input = "1.00 3 1.00 15.00 1.00 0.00 1.00 -15.00"
    # First proper test - answer is "3.52 2.37 111.94"
    #input = "1.00 1 5.00 23.00"
    # Second test - answer is 5.58 11.27 76.55
    #input = "1.00 3 6.00 23.00 10.00 -23.00 23.50 23.00"
    # Third test - answer is "14.13 18.39 118.63"
    #input = "0.50 2 10.00 0.00 500.00 3.00"
    # Fourth test - answer is 1.59 29.83 0.00
    # input="2.70 3 5.00 10.00 5.00 -10.00 20.00 0.00"
    # Fifth test - answer is -15.44 19.63 283.63
    #input="4.20 1 -100.00 -12.00"
    # Sixth test - answer is 0.97 32.94 357.82
    input = "9.53 10 -1.00 1.00 -2.00 2.00 3.00 -3.00 4.00 4.00 5.00 -5.00 6.00 6.00 7.00 7.00 -8.00 8.00 9.00 9.00 10.00 -10.00"
    
    # Split input and assign to variables; cast to floats
    input = input.split()
    wheel_base = float(input[0])
    segments = float(input[1])
    # Cut out first two elements
    input = input[2:]
    
    x = 0
    y = 0
    direction = 0
    
    count = 0
   
    # Iterate through each pair of values
    for i, element in enumerate(input):
        if i % 2 == 0:
            # Assign distance and angle variables
            distance = float(input[i])
            steering_angle = float(input[i+1])
            steering_abs = np.abs(steering_angle)
            turn_radius = wheel_base/np.sin(np.deg2rad(steering_abs))
            if steering_angle == 0:
                # Redo with rotation matrix
                x += distance * np.sin(np.deg2rad(direction))
                y += distance * np.cos(np.deg2rad(direction))
                print("position after move " + str(count+1) + ": x=" + str(round(x,2)) + " y=" + str(round(y,2)))
            
            if steering_angle > 0 or steering_angle < 0:
            
                new_direction = distance/(turn_radius*(np.pi/180)) 
                rotated_x = 0
                rotated_y = 0

                print("move " + str(count+1))
                print("direction: " + str(round(direction,2)))
                print("new direction: " + str(round(new_direction,2)))
                
                # Calculate vector for current move without considering existing position/angle
                # X function includes origin modification - not sure if correct
                new_x = np.sign(steering_angle)*(turn_radius - (turn_radius * np.cos(np.deg2rad(new_direction))))
                new_y = turn_radius * np.sin(np.deg2rad(new_direction))
                print("before vector rotation:")
                print("change in x: " + str(round(new_x,2)) + ", change in y: " + str(round(new_y,2)))

                # Rotate vector using direction we started at at beginning of this iteration
               
                rotated_x = np.cos(np.deg2rad(direction))*new_x + np.sin(np.deg2rad(direction))*new_y
                rotated_y = -np.sin(np.deg2rad(direction))*new_x + np.cos(np.deg2rad(direction))*new_y
                print("after vector rotation:")
                print("change in x: " + str(round(rotated_x,2)) + ", change in y: " + str(round(rotated_y,2)))
                
                # Set new direction if steering angle negative
                if steering_angle<0:
                    new_direction = 360-new_direction
                
                # Set direction that rover is facing at end of move
                
                direction = (direction + new_direction)%360
                x += rotated_x 
                y += rotated_y
                
                print("position after move " + str(count+1) + ": x=" + str(round(x,2)) + " y=" + str(round(y,2)))

                    
            count += 1
            print("direction: " + str(round(direction,2)))
            print("\n")
 
                  
    print(str(round(x,2)) + " " + str(round(y,2)) + " " + str(round((direction),2)))

    
mars_rover()