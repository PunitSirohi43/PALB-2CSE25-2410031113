def find_duplicate(nums):
    # Floyd's Cycle Finding Algorithm (Tortoise and Hare)
    tortoise = nums[0]
    hare = nums[0]
    
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
            
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]
        
    return hare

nums = [1, 3, 4, 2, 2]
print("Duplicate Number:", find_duplicate(nums))