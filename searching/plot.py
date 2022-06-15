import matplotlib.pyplot as plt
import numpy as np
  
# create data
x = np.linspace(0.1, 10.0, num=100)
y1 = x
  
# plot lines
plt.plot(x, y1, label = "y1 = x")
plt.plot(x, x*x, label = "n^2")
plt.plot(x, x*(np.log(x)), label = "nlog(n)")
plt.plot(x, np.log(x), label = "log(n)")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
# plt.legend()
plt.show()

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