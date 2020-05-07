array = ['G', 'B', 'R', 'R', 'B', 'R', 'G']

for i in range(len(array) - 1):
    a, b = array[i]
    if a == 'G':
        print(a, b)