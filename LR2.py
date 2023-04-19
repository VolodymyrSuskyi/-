import numpy as np

# матриця відстаней між містами


def DFS(u, visited, distance, adj):
    visited[u] = True
    for v in range(len(adj)):
        if adj[u][v] != 0 and not visited[v]:
            distance[0] += adj[u][v]
            DFS(v, visited, distance, adj)

def findShortestPath(adj):
    visited = [False] * len(adj)
    distance = [0]
    DFS(0, visited, distance, adj)
    for i in range(len(adj)):
        if not visited[i]:
            return -1
    return distance[0]
with open('matrix.txt') as f:
    adj = [list(map(int, row.split())) for row in f.readlines()]

V = len(adj)
shortestPath = findShortestPath(adj)
if shortestPath != -1:
    print("Shortest path for postman: " + str(shortestPath))
else:
    print("Not found")