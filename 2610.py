
nums = [1, 3, 4, 1, 2, 3, 1]

# Step 1: Count frequency using a dictionary
freq = {}
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# Step 2: Build the answer list
ans = []

while True:
    layer = []
    found = False  # flag to check if we added anything in this layer

    for key in freq:
        if freq[key] > 0:
            layer.append(key)
            freq[key] -= 1
            found = True  # we found at least one item to include

    if not found:
        break  # nothing left to add

    ans.append(layer)

print(ans)
             