def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1

arr=[20,45,27,47,55,67,75,88,90]
x = 76
result = linearSearch(arr, x)
print("Searching Element is present at index: ", result)

