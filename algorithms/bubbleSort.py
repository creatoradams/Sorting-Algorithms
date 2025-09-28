class bubbleSort:
    def bubble_sort(self, arr):

        # local helper to swap in-place
        def swap(i, j):
            arr[i], arr[j] = arr[j], arr[i]

        n = len(arr)  # array length
        swapped = True
        x = -1 # counter offset for shrinking range

        while swapped:
            swapped = False # assume sorted
            x = x + 1 # shrink range each loop
            for i in range(1, n - x):
                if arr[i - 1] > arr[i]: # compare neighbors
                    swap(i - 1, i) # swap if out of order
                    swapped = True
        return arr
