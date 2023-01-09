# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 15:50:14 2023

@author: wifry
"""

# Program to display the Fibonacci sequence up to n-th term

iterations = int(input("How many iterations? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if iterations <= 0:
   print("Please enter a positive integer")

# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < iterations +1:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1