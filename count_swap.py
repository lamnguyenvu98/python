from collections import OrderedDict as od
def count_swap(arr, n):
    v = od()
    count = 0
    for i, data in enumerate(arr):
        v[data] = i 
    vec = list(v.items())
    vec.sort()
    print("Sorted: ", vec)
    for i in range(n):
        if (i == vec[i][1]):
            continue
        j = vec[i][1]
        vec[i], vec[j] = vec[j], vec[i]
        if i != vec[i][1]:
            i -= 1
        count += 1
    print("Not sorted: ", vec)
    return count

arr = [4, 3, 2, 1]
n = len(arr)
print("Number of swap: ", count_swap(arr, n))
