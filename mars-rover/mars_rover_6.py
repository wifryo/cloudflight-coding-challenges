# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 15:55:34 2023

@author: wifry
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 11:39:31 2023

@author: wifry
"""

# UUID for level 6
uuid = "5b1bb8d9-9d11-45d5-afa8-6dea80baf923"
parameters = "3.60 14.00 148.80 148.80 1.50"
parameters = parameters.split()
wheel_base = float(parameters[0])
max_steering_angle = float(parameters[1])
target_x = float(parameters[2])
target_y = float(parameters[3])
target_radius = float(parameters[4])

# https://rover.codingcontest.org/rover/sensor/5b1bb8d9-9d11-45d5-afa8-6dea80baf923
# https://rover.codingcontest.org/rover/5b1bb8d9-9d11-45d5-afa8-6dea80baf923
# https://rover.codingcontest.org/rover/create?map=L6_MK2SP4RO&username=wifryo&contestId=practice
# https://rover.codingcontest.org/rover/move/5b1bb8d9-9d11-45d5-afa8-6dea80baf923?distance=0&steeringAngle=0

import numpy as np
import requests




def mars_rover():
    # Input is (distance steering_angle)*n
    input = "10 14 1.5 14 60 0 8 14 40 0 11 -14 4.3 -14 10 0 30 0 5 14 4 14"
    
    # Split input and assign to variables; cast to floats
    input = input.split()
    
    x = 0
    y = 0
    direction = 0
    
    count = 0
    #Uncomment below function call to run ALL moves in above input string
    #perform_moves(input)

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
    required_x_change = target_x - x
    required_y_change = target_y - y
    print("type of required x change:" + str(type(required_x_change)))
    ideal_angle = 90 - np.rad2deg(np.arctan(required_y_change/required_x_change))
    print("current ideal angle: " + str(round(ideal_angle,2)))
    target_distance = np.sqrt(np.square(required_x_change) + np.square(required_y_change))
    print("distance from target at ideal angle: " + str(round(target_distance,2)))

def perform_moves(input):
    for i, element in enumerate(input):
        if i % 2 == 0:
            distance = round(float(input[i]),2)
            angle = round(float(input[i+1]),2)
            move_rover(distance, angle)
            

def move_rover(distance, angle):
    response = (requests.get('https://rover.codingcontest.org/rover/move/' + uuid + '?distance=' + str(distance) + '&steeringAngle=' + str(angle))).text
    print(str(response))
    print("\n")
    sensor_information()

def sensor_information():
    sensor = (requests.get('https://rover.codingcontest.org/rover/sensor/' + uuid)).text
    sensor = sensor.split()
    angle = 110/14
    for i, element in enumerate(sensor):
        print(str(round(angle*i - 55)) + " degrees obstacle at " + str(element))
    
mars_rover()
move_rover(39.6,0)
#sensor_information()
