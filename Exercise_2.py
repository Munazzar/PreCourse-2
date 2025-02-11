# Python program for implementation of Quicksort Sort 
# time complexity = O(nlog(n))
# space complexity= O(n) 
# give you explanation for the approach
# [10, 7, 8, 9, 1, 5] 
# [5, 7, 1, 9, 8, 10] 
# [1, 5, 7, 8, 9, 10] 

[]
def partition(arr,low,high, pivot):
  while low<=high:
        while arr[low]<pivot:
            low+=1
        while arr[high]> pivot:
            high-=1
        if low<=high:
            arr[low], arr[high]=arr[high], arr[low]
            low+=1
            high-=1

  return low
    
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low>=high:
        return 
    pivot= arr[int((high+low)/2)]

    index=partition(arr, low, high, pivot)
    quickSort(arr, low, index-1)
    quickSort(arr, index, high)
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
