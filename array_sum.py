array = [2, 33, 83, 8, 3, 74, 9, 3, 4, 4]
array2 = [2, 33, 83, 8, 3, 74, 9, 3, 4, 4]

new_list = [array[0]]
for i in range(1, len(array)):
    new_list.append(new_list[i - 1] + array[i])
print(new_list)

# Alternative approach
for i in range(1, len(array)):
    array2[i] += array2[i - 1]
print(array2)