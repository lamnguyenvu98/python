size = 3
arr = [1, 2 ,3, 5, 6, 7 , 9]

window = arr[:size]

result = []
result.append(sum(window))

for i in range(size, len(arr)):
    if len(window) == size:
        window.pop(0)

    if len(window) < size:
        window.append(arr[i])

    result.append(sum(window))

print(arr)
print(result)
