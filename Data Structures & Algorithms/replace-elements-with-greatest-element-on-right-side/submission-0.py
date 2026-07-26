class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_value_so_far = -1 # Keeps track of the largest value seen as iterating over array

        # Reversed array and starting from end of array to count greatest element         
        for index in range(len(arr) - 1, -1, -1): # Range takes input start, stop, step
            tmp = arr[index] # Assign the temporary variable to array
            arr[index] = max_value_so_far # Assign the array to the max value found so far
            max_value_so_far = max(tmp, max_value_so_far)
        
        return arr


        
             
        