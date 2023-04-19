def check_isomorphic(mass1, mass2):
    # Перевіряємо кількість вершин та ребер у графах
    if len(mass1) != len(mass2) or sum(sum(m) for m in mass1) != sum(sum(m) for m in mass2):
        return False

    # Знаходимо характеристичні числа графів
    char1 = sorted([sum(m) for m in mass1])
    char2 = sorted([sum(m) for m in mass2])

    # Порівнюємо характеристичні числа
    if char1 != char2:
        return False

    # Створюємо словник для зберігання відображення вершин з першого графа в другий
    mapping = {}

    # Перебираємо всі вершини першого графа
    for i in range(len(mass1)):
        # Знаходимо список сусідів для поточної вершини в обох графах
        neighbors1 = [j for j in range(len(mass1[i])) if mass1[i][j] == 1]
        neighbors2 = [j for j in range(len(mass2[i])) if mass2[i][j] == 1]

        # Сортуємо списки сусідів за їх ступенями
        neighbors1.sort(key=lambda x: sum(mass1[x]))
        neighbors2.sort(key=lambda x: sum(mass2[x]))

        # Перевіряємо, чи відображення на вершини другого графа для цієї вершини з першого графа
        # вже існує, якщо ні, то додаємо його в словник
        if tuple(neighbors1) in mapping:
            if mapping[tuple(neighbors1)] != tuple(neighbors2):
                return False
        else:
            mapping[tuple(neighbors1)] = tuple(neighbors2)

    return True

with open('matrix.txt') as f:
    mass1 = [list(map(int, row.split())) for row in f.readlines()]
with open('matrix2.txt') as f:
    mass2 = [list(map(int, row.split())) for row in f.readlines()]

if check_isomorphic(mass1, mass2):
    print("Графи ізоморфні")
else:
    print("Графи неізоморфні")