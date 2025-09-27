import random
import time
from algorithms import bubbleSort
from algorithms import mergeSort
import math
import matplotlib.pyplot as plt
import numpy as np
# generate random numbers
import numpy as np


# Selection Sort Algorithm

# Display runtime table for each size array

# graph the number of comparisons performed and time spent with data size




""" ------ Data generators for best/worst/avg ------- """


def gen_best(n, alg_name):
    return list(range(n))

def gen_worst(n, alg_name):
    return list(range(n, 0, -1))

def gen_avg(n, alg_name):
    return [random.randint(0, 10**6) for _ in range(n)]




""" -------- Menu / Prompting --------- """

ALGOS = {
    1: ("Bubble Sort", bubbleSort), # menu choice #1
    2: ("Merge Sort", mergeSort),   # menu choice #2
                                     # menu choice #3
                                     # menu choice #4
}

CASES = \
{
    ("Best Case", gen_best),   # case #1
    ("Average Case", gen_avg), # case #2
    ("Worst Case", gen_worst), # case #3
}

DEFAULT_SIZES = [100, 1000, 10000, 100000]




