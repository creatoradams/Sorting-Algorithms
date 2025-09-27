from typing import List, Sequence, MutableSequence
import random
import numpy as np

class QuickSort:

    # Quick Sort Algorithm
    @staticmethod
    def sort(arr: np.ndarray) -> np.ndarray: # instance method that tkes an array and returns it sorted
        work = arr.tolist() # copy data into a python list to leave og unchanged

        def qs(a, lo, hi):
            if lo >= hi:
                return
            pivot = a[(lo + hi) // 2] # choose middle element. use floor division to get true int
            i, j = lo, hi # used to scan from both ends
            while i <= j: # partition loop, move elements left or right
                while a[i] < pivot: i += 1 # move left pointer until element >= pivot
                while a[j] > pivot: j -= 1 # move right pointer until element <= pivot
                if i <= j: # if pointers havent met, swap
                    a[i], a[j] = a[j], a[i]
                    i += 1;
                    j -= 1
            if lo < j: qs(a, lo, j) # sort left
            if i < hi: qs(a, i, hi) # sort right

        qs(work, 0, len(work) - 1) # start quicksort on the entire list
        return np.array(work) # convert back to Numpy array and return



