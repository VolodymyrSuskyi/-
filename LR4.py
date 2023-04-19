def breadth_first_search(source, sink, graph):
    visited = [False] * len(graph)
    queue = [source]
    visited[source] = True
    parent = [-1] * len(graph)

    while queue:
        current = queue.pop(0)
        for i in range(len(graph)):
            if not visited[i] and graph[current][i] > 0:
                queue.append(i)
                parent[i] = current
                visited[i] = True

    return visited[sink], parent


def max_flow(source, sink, graph):
    parent = [-1] * len(graph)
    max_flow = 0

    while True:
        has_path, parent = breadth_first_search(source, sink, graph)
        if not has_path:
            break

        path_flow = float('inf')
        i = sink
        while i != source:
            j = parent[i]
            path_flow = min(path_flow, graph[j][i])
            i = j

        i = sink
        while i != source:
            j = parent[i]
            graph[j][i] -= path_flow
            graph[i][j] += path_flow
            i = j

        max_flow += path_flow

    return max_flow

with open('matrix.txt') as f:
    graph = [list(map(int, row.split())) for row in f.readlines()]

source = 0
sink = 5
max_flow_val = max_flow(source, sink, graph)
for i in range(len(graph)):
    print(graph[i])
print("Max flow:", max_flow_val)