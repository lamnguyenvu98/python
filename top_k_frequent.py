def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # O(n)
    val_arr = [[] for _ in range(len(nums) + 1)]
    hashmap = {}

    for num in nums: # n
        hashmap[num] = 1 + hashmap.get(num, 0)
    
    for num, count in hashmap.items(): # n
        val_arr[count].append(num)
     
    top_k = []
    
    print(val_arr)

    for i in range(len(val_arr) - 1, 0, -1):
        for n in val_arr[i]:
            top_k.append(n)
            if len(top_k) == k:
                return top_k

arr = [4,1,-1,2,-1,2,3]
arr_test = [1,1,1,2,2,3]
k = 2

res = topKFrequent(arr, k)

print(res)
