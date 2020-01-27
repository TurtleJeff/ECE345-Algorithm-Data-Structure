# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 19:49:30 2020

@author: jeffl
"""

import sys
import csv
#import timeit
import time


def InsertionSort(A):
    for i in range(1,len(A)):
        key = int(A[i][0])
        values = A[i]
        j = i - 1
        while j > -1 and int(A[j][0]) > key:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = values     
    return


inputfile = (sys.argv[1])
#inputfile = 'a1.small.csv'
#inputfile = 'a1.large.csv'

with open(inputfile) as f:
    reader = csv.reader(f)
    input_data = list(reader)
    
    InsertionSort(input_data)
    print(input_data)
    
    
# =============================================================================
#     size = [1000, 5000, 10000, 20000, 28000]
#     for i in range(0,len(size)):
#         output_data = input_data[0:size[i]]
#         start_time = time.time()
#         InsertionSort(output_data)
#         end_time = time.time()
#         print("sample size: %d with running time: %.8f" %(size[i], end_time - start_time))
# =============================================================================


# =============================================================================
# for i in range(1,len(input_data)):
#     key = int(input_data[i][0])
#     values = input_data[i]
#     j = i - 1
#     while j > -1 and int(input_data[j][0]) > key:
#         input_data[j+1] = input_data[j]
#         j = j - 1
#     input_data[j+1] = values        
# =============================================================================
    
