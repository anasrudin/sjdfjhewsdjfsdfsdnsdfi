# Sorting Algorithm
# https://www.geeksforgeeks.org/radix-sort/
# 
# Algorithm          Time          Space
# Bubble sort        O(n2)         O(1)
# Insertion sort     O(n2)         O(1)
# Selection sort     O(n2)         O(1)
# Quicksort          O(nlog(n))    O(log(n))
# Mergesort          O(nlog(n))    O(n)
# Heapsort           O(nlog(n))    O(1)
# Counting sort      O(n + k)      O(k)
# Radix sort         O(nk)         O(n + k)
# Binary search      O(log(n))


# quicksort & merger sort using D&C algorithmm

def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
 
 
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 19]
bubbleSort(arr) 
print("Bubble Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")




 # Function to do insertion sort
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
# Driver code to test above
insertionSort(arr)
print(" ")
print("Insertion Sorted array is:")
for i in range(len(arr)):
    print ("%d"% arr[i], end=" ")



# quick sort
# Function to find the partition position
def partition(array, low, high):
 
  # Choose the rightmost element as pivot
  pivot = array[high]
 
  # Pointer for greater element
  i = low - 1
 
  # Traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # If element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1
 
      # Swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])
 
  # Swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])
 
  # Return the position from where partition is done
  return i + 1
 
# Function to perform quicksort
def quick_sort(array, low, high):
  if low < high:
 
    # Find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)
 
    # Recursive call on the left of pivot
    quick_sort(array, low, pi - 1)
 
    # Recursive call on the right of pivot
    quick_sort(array, pi + 1, high)
 
   
         
# Driver code
# array = [ 10, 7, 8, 9, 1, 5]
print()
quick_sort(arr, 0, len(arr) - 1)
 
print(f'Quick Sorted array: {arr}')
     


# mergesort
def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

print()
quick_sort(arr, 0, len(arr) - 1)
 
print(f'Merge Sorted array: {arr}')





# heap sort
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
  
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
  
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
  
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
  
        # Heapify the root.
        heapify(arr, n, largest)
  
# The main function to sort an array of given size
  
  
def heapSort(arr):
    n = len(arr)
  
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
  
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
  
  
# Driver code
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("heap Sorted array is")
for i in range(n):
    print("%d" % arr[i],end=" ")



# counting  sort
# The function that sorts the given arr[]
def count_sort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    # Create a count array to store count of individual
    # elements and initialize count array as 0
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]
 
    # Store count of each character
    for i in range(0, len(arr)):
        count_arr[arr[i]-min_element] += 1
 
    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
 
    # Build the output character array
    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1
 
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]
 
    return arr
 
 
# Driver program to test above function

arr = [-5, -10, 0, -3, 8, 5, -1, 10]
ans = count_sort(arr)
print()
print("counting Sorted character array is " + str(ans))








# radix sort
def countingSort(arr, exp1):
  
    n = len(arr)
  
    # The output array elements that will have sorted arr
    output = [0] * (n)
  
    # initialize count array as 0
    count = [0] * (10)
  
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
  
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
  
    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
  
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
  
# Method to do Radix Sort
def radixSort(arr):
  
    # Find the maximum number to know number of digits
    max1 = max(arr)
  
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp > 1:
        countingSort(arr, exp)
        exp *= 10
  
  
# Driver code
arr = [170, 45, 75, 90, 802, 24, 2, 66]
  
# Function Call
radixSort(arr)
print("radix sorted arry")
for i in range(len(arr)):
    print(arr[i],end=" ")