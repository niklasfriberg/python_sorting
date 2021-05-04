import numpy as np
import math
import time

print("Enter array size: ")
array_size = int(input())
test_array = np.random.randint(0, 20, size = array_size)
print("starting array:  ", test_array)


def insertion_sort(array):
    i = 1
    while i < len(array):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            #swapping the value of [j - 1] and [j]
            array[j - 1], array[j] = array[j], array[j - 1]
            j = j - 1
        i = i + 1
    return array

starttime = time.perf_counter()
print("insertion sort:  ", insertion_sort(test_array))
print("time to sport: {} seconds.".format(str(time.perf_counter() - starttime)))

def bubble_sort(array):
    n = len(array)
    while n <= 1:
        new_n = 0
        i = 1
        for int in range(i, n - 1):
            if array[i - 1] > array[i]:
                #swapping values of [i - 1] and [i]
                array[i - 1], array[i] = array[i], array[i - 1]
                new_n = i
        n = new_n
    return array

starttime = time.perf_counter()
print("bubble_sort:     ", bubble_sort(test_array))
print("time to sport: {} seconds.".format(str(time.perf_counter() - starttime)))

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left,right, array)

def merge(left, right, array):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    
    return array


starttime = time.perf_counter()
print("merge sort:      ", merge_sort(test_array))
print("time to sport: {} seconds.".format(str(time.perf_counter() - starttime)))

# Using hoares partition scheme
def quick_sort(array, lo = 0, hi = None):
    if hi == None:
        hi = len(array) - 1
    
    if lo < hi:
        p = partition(array, lo, hi)
        quick_sort(array, lo, p)
        quick_sort(array, p + 1, hi)

    return array

def partition(array, lo, hi):
    pivot = array[math.floor((hi + lo) / 2)]
    i = lo - 1
    j = hi + 1
    while True:
        i += 1
        while array[i] < pivot:
            i += 1
        j -= 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]
        

starttime = time.perf_counter()
print("quick sort:      ", quick_sort(test_array))
print("time to sport: {} seconds.".format(str(time.perf_counter() - starttime)))

def heap_sort(array):
    n = len(array)
    for i in range(n, -1, -1):
        heapify(array, n, i)
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array

def heapify(array, n, count):

    max_int = count
    
    left = 2 * count + 1
    right = 2 * count + 2
    if left < n and array[count] < array[left]:
        max_int = left
    if right < n and array[max_int] < array[right]:
        max_int = right
    if max_int != count:
        array[count], array[max_int] = array[max_int], array[count]
        heapify(array, n, max_int)


starttime = time.perf_counter()
print("heap sort:       ", heap_sort(test_array))
print("time to sport: {} seconds.".format(str(time.perf_counter() - starttime)))

"""
Visualization of sorting
"""
"""
algo = heap_sort(test_array)

fig, ax = plt.subplots()
ax.set_title("Heap sort")
bar_rec = ax.bar(range(len(test_array)), test_array, align="edge")
text = ax.text(0.02, 0.95, "", transform=ax.TransAxes)
epochs = [0]

def update_plot(array, rec, epochs):
    for rec, val in zip(rec, array):
        rec.set_height(val)
    epochs[0] += 1
    text.set_text("No of operations :{}".format(epochs[0]))

anim = animation.FuncAnimation(fig, func=update_plot, fargs=(bar_rec, epochs), frames=algo, interval=1, repeat=False)
plt.show()
"""