import matplotlib.pyplot as plt
import time
import random

# Recursive binary search
def binarySearch(arr, left, right, key):
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binarySearch(arr, left, mid - 1, key)
    else:
        return binarySearch(arr, mid + 1, right, key)

# Test sizes
sizes = [1000, 2000, 3000, 4000, 5000]
times = []
key = 4000  # key to search

# Measure execution time for each size
for n in sizes:
    arr = sorted(random.sample(range(1, n * 2), n))  # sorted array
    start = time.time()
    binarySearch(arr, 0, n - 1, key)
    end = time.time()
    times.append((end - start) * 1000)  # convert to ms

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(sizes, times, marker='o', linestyle='-', color='b')
plt.title("Binary Search Execution Time vs Array Size")
plt.xlabel("Array Size")
plt.ylabel("Execution Time (ms)")
plt.grid(True)
plt.show()
