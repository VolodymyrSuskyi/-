def branch_and_bound(path, length, available, distances):
    global bestLength, bestPath

    if not available:
        length += distances[path[-1]][path[0]]
        if length < bestLength:
            bestLength = length
            bestPath = path.copy()
        return

    if length >= bestLength:
        return

    lastCity = path[-1]

    for i in range(len(available)):
        city = available[i]
        newLength = length + distances[lastCity][city]

        if newLength < bestLength:
            newPath = path.copy()
            newPath.append(city)
            newAvailable = available.copy()
            newAvailable.pop(i)
            branch_and_bound(newPath, newLength, newAvailable, distances)

with open('matrix.txt') as f:
    distances = [list(map(int, row.split())) for row in f.readlines()]

bestLength = float('inf')
bestPath = []

branch_and_bound([0], 0, [1, 2, 3, 4, 5], distances)

print(bestLength)
print(bestPath)
