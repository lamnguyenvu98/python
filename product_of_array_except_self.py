def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    """
    input:      [ 4, 3, 2, 1, 2]
    prefix:     [ 12, 24, 48, 48, 76]
    postfix:    [ 24, 24, 12, 4]
    result:     [ 24, 12, 8, 6]
    """
    postfix = [0] * len(nums)
    prefix = [0] * len(nums)
    result = []
    
    prev = 1

    for i in range(0, len(nums)):
        pass
        

    print(prefix)

    prev = 1
    for i in range(len(nums) - 1, -1, -1):
        postfix[i] = prev * nums[i]
        prev = postfix[i]
    
    print(postfix)

    for i in range(len(nums)):
        if i == 0:
            result.append(postfix[i])
        else:
            if i == (len(nums) - 1):
                val = prefix[i - 1]
            else:
                val = prefix[i - 1] * postfix[i + 1]
            result.append(val)
    
    return result

def product_self(nums):
    result = [0] * len(nums)
    prod = 1
    for num in nums:
        prod *= num

    for i in range(len(nums)):
        result[i] = prod // nums[i]

    return result

arr = [4,3,2,1,2]
result = product_self(arr)

print(result)
