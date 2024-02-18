arr = [1, 2, 3, 5, 9, 10, 12, 15]

val = 3

def binary_search(arr, val):
    left = 0
    right = len(arr) - 1
    
    index = None
    mid = 0

    while True:
        if left > right: break
        mid = (right + left) // 2
        print(f"left: {left}, right: {right}, mid: {mid}, value: {arr[mid]}")
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    
    return index

index = binary_search(arr, val)
print(arr)

if index is None:
    print("Value {} is not existed".format(val))
else:
    print("Value {} is at index {}".format(val, index))

