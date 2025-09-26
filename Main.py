
import random
import time
import math
import matplotlib.pyplot as plt
import numpy as np


#===================================
# Sorting Algorithms
#===================================

def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)  # array length
    swapped = True
    x = -1 # counter offset
    while swapped:
        swapped = False #assume sorted
        x = x + 1 #shrinks range each loop
        for i in range(1, n - x):
            if arr[i -1] > arr[i]: # compares neighbors
                swap (i -1, i)     # swaps if out of order
                swapped = True
    return arr

def merge_sort(arr):
    if len(arr) <= 1: # base case
        return arr

    mid = len(arr) // 2 # splits
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:]) # sorts halves
    return merge(left, right, arr.copy()) # merge halves using merge helper function

def merge(left, right, merged):  # merge helper function
    left_cursor, right_cursor = 0, 0  # pointers into left and right arrays
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1  # moves left pointer
        else:
            merged[left_cursor + right_cursor] = right[left_cursor]
            right_cursor += 1 # moves right pointer

    for left_cursor in range(left_cursor, len(left)):  # copy remaining left
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):  # copy remaining right
        merged[left_cursor + right_cursor] = right[left_cursor]

    return merged # returns merged sorted array

#===================================
# Timer
#===================================

def time_once(alg_func, data):
    start = time.perf_counter() # starts timer
    out = alg_func(data[:]) # run algorithm on copy
    end = time.perf_counter() # end timer
    if out != sorted(data): # correctness check
        raise AssertionError("Sort failed correctness check.")
    return end - start # returns time

def time_many(alg_func, size_list, case_gen, trials = 1):
    results = [] # holds 'times'
    for n in size_list: # loop over input sizes
        total = 0.0
        for _ in range(trials): # run multiple trials
            data = case_gen(n)
            total += time_once(alg_func, data)
        results.append(total / trials) # avg runtime
    return results # list of runtimes

#===================================
# Data generators for best/worst/avg
#===================================

def gen_best(n, alg_name):
    return list(range(n))

def gen_worst(n, alg_name):
    return list(range(n, 0, -1))

def gen_avg(n, alg_name):
    return [random.randint(0, 10**6) for _ in range(n)]

#===================================
# Menu / Prompting
#===================================

ALGOS = {
    1: ("Bubble Sort", bubble_sort), # menu choice #1
    2: ("Merge Sort", merge_sort),   # menu choice #2
                                     # menu choice #3
                                     # menu choice #4
}

CASES = {
    1.("Best Case", gen_best),   # case #1
    2.("Average Case", gen_avg), # case #2
    3.("Worst Case", gen_worst), # case #3
}

DEFAULT_SIZES = [100, 1000, 10000, 100000]




