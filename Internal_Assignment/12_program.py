def get_min_diff(arr, n, k):
    arr.sort()
    ans = arr[n-1] - arr[0]
    
    smallest = arr[0] + k
    largest = arr[n-1] - k
    
    for i in range(n-1):
        min_h = min(smallest, arr[i+1] - k)
        max_h = max(largest, arr[i] + k)
        
        if min_h < 0:
            continue
            
        ans = min(ans, max_h - min_h)
        
    return ans

arr = [1, 5, 8, 10]
k = 2
n = len(arr)
print("Minimize Heights Diff:", get_min_diff(arr, n, k))