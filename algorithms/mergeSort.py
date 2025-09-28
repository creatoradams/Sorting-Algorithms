from typing import List

class MergeSort:
        """ This method does the divide and conquer step """
        def sort(self, a: List[int]) -> List[int]:
            if len(a) <= 1:
                return a[:]
            mid = len(a) // 2 # get the middle
            left = self.sort(a[:mid]) # sort left half
            right = self.sort(a[mid:]) # sort right half
            return self.merge(left, right) # merge both sorted halves into one list

        """ This takes the 2 sorted lists and combines them into one sorted list by repeatedly 
                picking the smaller leading element
        """
        def merge(self, a: List[int], b: List[int]) -> List[int]: # used to merge 2 already sorted list
            i = j = 0 # pointers
            out: List[int] = [] # output list in ascending order
            while i < len(a) and j < len(b): # iterate while both lists still have elements
                if a[i] < b[j]:
                    out.append(a[i]) # append from a
                    i += 1 # move a's pointer
                else:
                    out.append(b[j]) # append from b
                    j += 1 # advance b's pointer
            out.extend(a[i:]) # append anything left from a
            out.extend(b[j:]) # append anything left from b
            return out # finally a fully sorted list