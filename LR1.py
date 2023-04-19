def boruvka(matrix):
    # перетворюємо матрицю суміжності у список ребер
    edges = []
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if matrix[i][j] != 0:
                edges.append((i, j, matrix[i][j]))

    # список компонент зв'язності
    components = [{i} for i in range(len(matrix))]

    # цикл по кожній компоненті зв'язності
    while len(components) > 1:
        cheapest = dict.fromkeys(range(len(matrix)))

        # знаходимо найбільш дешеве ребро для кожної компоненти
        for u, v, w in edges:
            cu = next((i for i, component in enumerate(components) if u in component), None)
            cv = next((i for i, component in enumerate(components) if v in component), None)
            if cu != cv:
                if cheapest[cu] is None or cheapest[cu][2] > w:
                    cheapest[cu] = (u, v, w)
                if cheapest[cv] is None or cheapest[cv][2] > w:
                    cheapest[cv] = (u, v, w)

        # додаємо найбільш дешеві ребра до MST та об'єднуємо компоненти
        for u, v, w in filter(lambda x: x is not None, cheapest.values()):
            if u is not None and v is not None:
                cu = next((j for j, component in enumerate(components) if u in component), None)
                cv = next((j for j, component in enumerate(components) if v in component), None)
                if cu != cv:
                    print(f"Added edge ({u}, {v}) with cost {w}")
                    components[cu].update(components[cv])
                    components.pop(cv)

    return components[0]

with open('matrix.txt') as f:
    graph = [list(map(int, row.split())) for row in f.readlines()]

result = boruvka(graph)
print(result)