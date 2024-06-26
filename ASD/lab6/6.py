"""
Алгоритм Крускала — это алгоритм построения минимального остовного дерева в связном взвешенном неориентированном 
графе. 
Алгоритм Крускала работает по следующему принципу:
1. Создаем список всех ребер и сортируем его по возрастанию весов.
2. Создаем пустое дерево и множество, содержащее все вершины графа.
3. Берем ребро из отсортированного списка ребер с наименьшим весом и проверяем, не создает ли оно цикл в дереве.
Если ребро не создает цикла, добавляем его в дерево, а вершины, соединяемые этим ребром, объединяем в одно множество.
4. Повторяем шаг 3 для каждого ребра в отсортированном списке до тех пор, пока не будут рассмотрены все ребра или пока 
дерево не станет остовным.
В результате работы алгоритма получаем минимальное остовное дерево графа, состоящее из всех вершин и соединенных
наименьшим возможным числом ребер.
"""



with open('matrix.txt', "r") as f:
    n = int(f.readline().strip())
    matrix = [[int(j) for j in f.readline().strip().split()] for i in range(n)]


edges = []
for i in range(n):
    for j in range(i+1, n):
        if matrix[i][j] != 0:
            edges.append((i, j, matrix[i][j]))


edges.sort(key=lambda elem: elem[2])



result = []

sets = [{i} for i in range(n)]



def find_set(vertex):
    for s in sets:
        if vertex in s:
            return s
    return None



for e in edges:
    u, v, w = e
    set1 = find_set(u)
    set2 = find_set(v)
    if set1 != set2:
        result.append(e)
        sets.remove(set1)
        sets.remove(set2)
        sets.append(set1.union(set2))
        print(sets)
print(result)

print("Минимальное остовное дерево состоит из следующих ребер:")
for e in result:
    print("Ребро между вершинами {} и {}, вес ребра: {}".format(e[0], e[1], e[2]))