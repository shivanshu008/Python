#Binary Search Algorithm Using Recursion
#function Definition
def binarySearch(arr, x,i,j):
    while i<=j:
        mid = i +(j-1)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            #search Space - mid+1 to j
            #right side of the mid
            return binarySearch(arr, x,mid+1,j)
        else :
            #left side of the mid
            #search space - i to mid-1
            return binarySearch(arr, x, i, mid-1)
    return -1

#Driver Code
arr=[20,30,40,50,60,70,80,90]
x=80
i=0
j=len(arr)-1
#Function Call
result = binarySearch(arr, x, i, j)
print("Searching element is present at location",result)