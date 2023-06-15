# Лабораторная работа по алгоритмам #2
Все алгоритмы запускаются в main файле. В файле read_info Лежит функция чтения данных о точках и прямоугольниках. А во всех остальных лежат алгоритмы решений

# Генерация данных
```python
def data_gen(a_count, just_N=76283):
    import random
    rand_mas = [1559, ..., 12689] # массив простых чисел
    squares = []
    points = []
    for i in range(a_count):
        squares.append([10 * i, 10 * i, 10 * (2 * a_count - i), 10 * (2 * a_count - i)])

    for i in range(a_count):
        points.append([((random.choice(rand_mas) * i) ** 31) % (20 * just_N),
                       ((random.choice(rand_mas) * i) ** 31) % (20 * just_N)])

    return squares, points
```
# map_r - Решение при помощи карты координат
```python
map_sq = []
    for i in range(len(x_points)):
        map_sq.append([])
        for k in range(len(y_points)):
            map_sq[i].append(0)

    for sq in range(square_num):
        for i in range(bins(x_points, sq_x_points[sq][0], 0, len(x_points)),
                       bins(x_points, sq_x_points[sq][1], 0, len(x_points))):
            for j in range(bins(y_points, sq_y_points[sq][0], 0, len(y_points)),
                           bins(y_points, sq_y_points[sq][1], 0, len(y_points))):
                map_sq[i][j] += 1
```
Проверка точек
```python
    for point in points:
        if ((point[0] < x_points[0] or point[0] >= x_points[-1])
                or (point[1] < y_points[0] or point[1] >= y_points[-1])):
            result.append(0)
        else:
            x = bins(x_points, point[0], 0, len(x_points))
            y = bins(y_points, point[1], 0, len(y_points))
            result.append(map_sq[x][y])
```
# pereb_resh - Решение перебором
Перебираем для каждой точки все прямоугольники и считаем все, в которые она входит.
```python
def pereb_r(parms, points):
    import time
    result = []
    start_time = time.time()
    for point in points:
        m = 0
        for parm in parms:
            if (parm[0] <= point[0] < parm[2]) and (parm[1] <= point[1] < parm[3]):
                m += 1
        result.append(m)
    return result, 0, time.time() - start_time
```
# tree_r - Решение при помощи дерева отрезков
Структура дерева и "добавление" к дереву прямоугольника.
```python
    class Tree:
        def __init__(self, left_gr=None, right_gr=None, left_ch=None, right_ch=None, cargo=0, ):
            self.cargo = cargo
            self.left_ch = left_ch
            self.right_ch = right_ch
            self.left_gr = left_gr
            self.right_gr = right_gr
            
        def plus_to_tree(self, start_index, end_index, num):
            if self is None:
                return self
            tree = Tree(self.left_gr, self.right_gr, self.left_ch, self.right_ch, self.cargo)
            if tree.left_gr >= start_index and tree.right_gr <= end_index:
                tree.cargo += num
            elif tree.right_gr >= start_index or tree.left_gr <= end_index:
                if not tree.left_ch is None:
                    tree.left_ch = tree.left_ch.plus_to_tree(start_index, end_index, num)
                if not tree.right_ch is None:
                    tree.right_ch = tree.right_ch.plus_to_tree(start_index, end_index, num)
            return tree
```
Добавление новых деревьев в массив деревьев.
Для каждой координаты мы сначала добавляем новый прямоугольник к дереву, потом добавляем этот прямоугольник к очереди прямоугольников. А после удаляем из учёта дерева все прямоугольники, кончающиеся на данной координате.
```python
    for sq in q_x_points:
        while sq_ind < len(squares) and squares[sq_ind][0] == sq:
            sort_time = time.time() * 100
            new_tree = new_tree.plus_to_tree(bins(q_y_points, squares[sq_ind][1], 0, len(q_y_points)),
                                             bins(q_y_points, squares[sq_ind][3], 0, len(q_y_points)), 1)
            sum_sotr_time += time.time() * 100 - sort_time

            que.append(squares[sq_ind])
            que.sort(key=therd_arg)
            sq_ind += 1
        while len(que) > 0 and sq >= que[0][2]:
            sort_time = time.time() * 100
            new_tree = new_tree.plus_to_tree(bins(q_y_points, que[0][1], 0, len(q_y_points)),
                                             bins(q_y_points, que[0][3], 0, len(q_y_points)), -1)
            sum_sotr_time += time.time() * 100 - sort_time
            que.pop(0)
        Tree_mas.append(new_tree)
```
Проверка точкек
```python
    for p in points:
        if p[0] < q_x_points[0] or p[0] > q_x_points[-1]:
            result.append(0)
            continue
        if p[1] < q_y_points[0] or p[1] > q_y_points[-1]:
            result.append(0)
            continue
        x = bins(q_x_points, p[0], 0, len(q_x_points))
        y = bins(q_y_points, p[1], 0, len(q_y_points))
        if y > len(q_y_points) // 2:
            y += 1
        result.append(Tree_mas[x].sum_tree(y))
```
# Графики и выводы

