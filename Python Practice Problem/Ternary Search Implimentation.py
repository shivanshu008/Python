#function Definition
def TernarySearch(arr, i, j,key):
    #Compute the values of mid1 and mid2

    mid1=i+(j-i)//3
    mid2=j-(j-i)//3
    
    while i <=j:
        if arr[mid1] == key:
            return mid1
        elif arr[mid2] == key:
            return mid2
        
        #first part of the ternary search
        elif key < arr [mid1]:
            return TernarySearch(arr,i,mid1-1,key)
        
        #Third Part of ternary search
        elif key > arr[mid2]:
            ##Recursive Call
            return TernarySearch(arr,mid2+1,j,key)
        
        #Second part of ternary search
        else:
            ##Recursive call
            return TernarySearch(arr,mid1+1,mid2-1,key)
        
        #if searching element is not present in the array
    return -1

#Driver Code
arr=[20,25,47,56,59,63,65,79,82]
i = 0
j = len(arr)-1
key=int(input('Enter the number to be found: '))
#function Calling
position = TernarySearch(arr,i,j,key)
print(position) 