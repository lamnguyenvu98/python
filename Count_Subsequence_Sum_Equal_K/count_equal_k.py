def subsetSum(arr, n, i,sum, count):
    if (i == n):
        if (sum == 0):
            count += 1
            arr_output.append(list(curr))
        return count
    
    curr.append(arr[i])  
    count = subsetSum(arr, n, i + 1, sum - arr[i], count)
    curr.pop()
    count = subsetSum(arr, n, i + 1, sum, count)
    return count
  
arr_output = []
curr = []
arr = [1, 2, 3, 5]
sum = 4
n = len(arr)
  
print("Number of subsets: ",subsetSum(arr, n, 0, sum, 0))
print("All subsets are: ", arr_output)
