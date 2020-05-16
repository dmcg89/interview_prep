def k_largest(arr, k): 
    arr.sort(reverse = True) 
    for i in range(k): 
        print (arr[i])  
  
# Driver program 
arr = [5, 1, 3, 6, 8, 2, 4, 7]
# n = len(arr) 
k = 3
k_largest(arr, k) 
  