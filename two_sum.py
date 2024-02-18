arr = [1, 2, 4, 6, 8]

s = 8

def two_sum(arr, s):
    left = 0
    right = len(arr) - 1
    
    total = 0

    while left <= right:
        val_1 = arr[left]
        val_2 = arr[right]
        total = val_1 + val_2

        if total == s:
            return [left, right]
        elif total > s:
            right -= 1
        else:
            left += 1

    return

result = two_sum(arr, s)

print(arr)
print(result)
