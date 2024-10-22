## Method Definition
## Time Complexity : O ( n^ 2)
def SelectionSort(arr):
    n = len(arr)
    for i in range (n):
        min_index = i
        for j in range (i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
                arr[i],arr[min_index] = arr[min_index], arr[i]
    return arr

## Driver Code
arr = [70,56,23,19,25,37,48]
result = SelectionSort(arr)
print("Sorted array after applying Selection Sort: ",result)