# kadane algorithm (Dynamic programming)
from typing import List
import sys

def maxSubArray(self, nums: List[int]) -> int:
    localmax = 0
    globalmax = -sys.maxsize - 1
    for i in range(len(nums)):
        localmax+=nums[i]
        globalmax = max(globalmax, localmax)
        if localmax<0:
            localmax=0
    return globalmax


a = [-2, 11, -4, 13, -5, 2]
b = [1, -3, 4, -2, -1, 6]
print(maxSubArray("a", a))
print(maxSubArray("b", b))


# Divide and conccuer
def maxCrossingSum(arr, l, m, h):
 
    # Include elements on left of mid.
    sm = 0
    left_sum = -10000
 
    for i in range(m, l-1, -1):
        sm = sm + arr[i]
 
        if (sm > left_sum):
            left_sum = sm
 
    # Include elements on right of mid
    sm = 0
    right_sum = -1000
    for i in range(m + 1, h + 1):
        sm = sm + arr[i]
 
        if (sm > right_sum):
            right_sum = sm
 
    # Return sum of elements on left and right of mid
    # returning only left_sum + right_sum will fail for [-2, 1]
    return max(left_sum + right_sum, left_sum, right_sum)
 
 
# Returns sum of maximum sum subarray in aa[l..h]
def maxSubArraySum(arr, l, h):
 
    # Base Case: Only one element
    if (l == h):
        return arr[l]
 
    # Find middle point
    m = (l + h) // 2
 
    # Return maximum of following three possible cases
    # a) Maximum subarray sum in left half
    # b) Maximum subarray sum in right half
    # c) Maximum subarray sum such that the
    #     subarray crosses the midpoint
    return max(maxSubArraySum(arr, l, m),
               maxSubArraySum(arr, m+1, h),
               maxCrossingSum(arr, l, m, h))
 
 

lena=len(a)
lenb= len(b)
max_sum = maxSubArraySum(a, 0, lena-1)
print("Maximum contiguous sum is ", max_sum)
max_sum2 = maxSubArraySum(b, 0, lenb-1)
print("Maximum contiguous sum is ", max_sum2)
