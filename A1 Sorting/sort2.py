# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 00:32:02 2020

@author: jeffl
"""

import sys
import csv
import time
import random

def QuickSort(A, p, r):
    if p<r:
        q = Partition(A, p, r);
        QuickSort(A, p, q-1)
        QuickSort(A, q+1,r)
        

def Partition(A, p, r):
    x = int(A[r][0]);
    i = p-1
    for j in range (p, r):
         if int(A[j][0]) <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


inputfile = (sys.argv[1])
#inputfile = 'a1.small.csv'
#inputfile = 'a1.large.csv'


with open(inputfile) as f:
    reader = csv.reader(f)
    input_data = list(reader)
    
    QuickSort(input_data,0,len(input_data)-1)
    print(input_data)
# =============================================================================
#     size = [1000, 5000, 10000, 20000, 28000]
#     for i in range(0,len(size)):
#         output_data = input_data[0:size[i]]
#         start_time = time.time()
#         QuickSort(output_data,0,len(output_data)-1)
#         end_time = time.time()
#         print("sample size: %d with running time: %.8f" %(size[i], end_time - start_time))   
# =============================================================================
