def binarySearch(arr,sum_value):
    l = 0
    r=len(arr)-1
    while l<=r:
        if (arr[l] + arr[r]) == sum_value:
            return (l,r)
        elif (arr[l] + arr[r]) > sum_value:
            r = r-1
        else:
            l = l + 1
        

#Driver Code
arr=[20,40,60,80,90,120,2410]
sum_value=210
result = binarySearch(arr, sum_value)
print(result)