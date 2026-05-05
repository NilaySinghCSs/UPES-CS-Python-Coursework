L = [12, -3, 7, 0, 12, 45, -3, 9, 0, 21]

unique_list = []
for item in L:
    if item not in unique_list:
        unique_list.append(item)

positives = []
zeros = []
negatives = []

for item in unique_list:
    if item > 0:
        positives.append(item)
    elif item == 0:
        zeros.append(item)
    else:
        negatives.append(item)

positives.sort()
negatives.sort(reverse=True)
reordered_list = positives + zeros + negatives

total = sum(reordered_list)
mean = total / len(reordered_list)

sorted_L = list(reordered_list)
sorted_L.sort()
n = len(sorted_L)
if n % 2 == 0:
    median = (sorted_L[n//2 - 1] + sorted_L[n//2]) / 2
else:
    median = sorted_L[n//2]

frequency = {}
for item in L:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

max_count = 0
mode = L[0]
for key in frequency:
    if frequency[key] > max_count:
        max_count = frequency[key]
        mode = key

sorted_unique = list(unique_list)
sorted_unique.sort()
second_smallest = sorted_unique[1]
second_largest = sorted_unique[-2]

rebuilt_list = [x for x in reordered_list]

print("Original List:", L)
print("Reordered List:", reordered_list)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Second Smallest:", second_smallest)
print("Second Largest:", second_largest)
print("Rebuilt List:", rebuilt_list)