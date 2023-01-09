# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 17:01:23 2023

@author: wifry
"""
import numpy as np

input = "2.45 90.00"
input = input.split()
wheel_base = float(input[0])
steering_angle = float(input[1])
turn_radius = round(wheel_base/np.sin(np.deg2rad(steering_angle)),2)
print(turn_radius)