# Step 1 receive user input. user input is also amount of further inputs

n = int(input())
# Step 2 initialize a loop counter 'i' and also initialize a variable to keep adding length.
i = 0
currentLength = 0

# Step 3 loop for every input. for each input add to current length.
while i < n:
    a = int(input())
    currentLength = currentLength + a
    i += 1

# Step 4 for each add you lose 1 cm, so current length must be subtracted by n - 1
currentLength = currentLength - (n-1)
print(currentLength)
