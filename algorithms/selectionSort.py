import numpy as np

""" Return a new sorted array with selection sort 
    takes an array and returns a new array thats sorted
"""
class SelectionSort:
    @staticmethod
    def sort(arr: np.ndarray) -> np.ndarray:
        # work on a list copy to keep original unchanged
        work = arr.tolist()
        n = len(work)

        # move through one step at a time
        for i in range(n-1):
            minIndex = i
            for j in range(i+1, n): # find index of the smallest element
                if work[j] < work[minIndex]:
                    minIndex = j
            if minIndex != i: # swap smallest found with the first of the unsorted
                work[i], work[minIndex] = work[minIndex], work[i]
        # convert back to a numpy array and return
        return np.array(work)