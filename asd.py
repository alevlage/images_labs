arr = np.zeros(11,11)
size = 11
for i in range(size):
    for j in range(size):
        if (i==j):
            arr[i][j] = 1
        elif (j==(len(arr) - i)):
            arr[i][j] = 1