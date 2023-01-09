# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 17:21:19 2023

@author: wifry
"""

import numpy as np

def mars_rover():
    input = "1.00 5.00 23.00"
    
    # Split input and assign to variables; cast to floats
    input = input.split()
    wheel_base = float(input[0])
    distance = float(input[1])
    steering_angle = float(input[2])
    steering_abs = np.abs(steering_angle)

    
    if steering_angle == 0:
        x = 0.00
        y = distance
        new_direction = 0.00
        print(str(x) + " " + str(y) + " " + str(round((new_direction),2)))
        return
    
    
    turn_radius = wheel_base/np.sin(np.deg2rad(steering_abs))
    new_direction = distance/(turn_radius*(np.pi/180)) 
    
    print("wheel base: " + str(wheel_base) + " distance: " + str(distance) + " steering angle: " + str(steering_angle) + " turn radius: " + str(turn_radius))
    
        
    new_direction = new_direction%360
    
    # x = r - rcos(angle)
    # y = rsin(angle)
    x = np.sign(steering_angle)*(turn_radius - (turn_radius * np.cos(np.deg2rad(new_direction))))
    y = turn_radius * np.sin(np.deg2rad(new_direction))
    
    # Set direction if steering angle negative
    if steering_angle<0:
        new_direction = 360-new_direction      
         
    print(str(round(x,2)) + " " + str(round(y,2)) + " " + str(round((new_direction),2)))
    
mars_rover()