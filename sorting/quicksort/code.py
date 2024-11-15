def quicksort(array, high, low):
  if low < high:
    pi = partition(array, low, high) #for the first iteration
    quicksort(array, low, pi-1) #update high - this is for left side... bring high down
    quicksort(array, pi+1, high) #update low - this is for right side.... bring low up



def partition(array, low, high):
  pivot = array[high] #here, we are picking the last element. you can use other ways to pick the pivot too.
  i = low - 1
  for j in range(low, high):
    if array[j] < pivot:
      i++ #move the marker as j element is added to smaller side. we're pushing the end of smaller-subarray
      swap(arr, i, j) #swap 

  swap(arr, i+1, high) #swap pivot(highest) with i+1 element(which will be the first element in the largest-subarray)
  return i+1 #return pivots position


def swap(array, a, b):
  array[a], array[b] = array[b], array[a]


