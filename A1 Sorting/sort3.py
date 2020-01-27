# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 00:52:17 2020

@author: jeffl
"""

import sys
import csv
import time


def BubbleSort(A):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(1,len(A)):
            if int(A[i-1][0]) > int(A[i][0]):
                A[i-1], A[i] = A[i], A[i-1]
                swapped = True


def OptimizedBubbleSort(A):
    n = len(A)
    while n > 1:
        newn = 0
        for i in range(1,n):
            if int(A[i-1][0]) > int(A[i][0]):
                A[i-1], A[i] = A[i], A[i-1]
                newn = i           
        n = newn 
        
inputfile = (sys.argv[1])
#inputfile = 'a1.small.csv'
#inputfile = 'a1.large.csv'

with open(inputfile) as f:
    reader = csv.reader(f)
    input_data = list(reader)
    
    OptimizedBubbleSort(input_data)
    print(input_data)
   
# =============================================================================
#     size = [1000, 5000, 10000, 20000, 28000]
#     for i in range(0,len(size)):
#         output_data = input_data[0:size[i]]
#         start_time = time.time()
#         OptimizedBubbleSort(output_data)
#         end_time = time.time()
#         print("sample size: %d with running time: %.8f" %(size[i], end_time - start_time))                
# =============================================================================
