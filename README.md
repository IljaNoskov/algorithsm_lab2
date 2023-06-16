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
Размер матрица равен количеству точек по x * количество точек по y. А дальше добавляем +1 для каждой области, которую перекрывает каждое значение карты.
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
##### Проверка точек
Проверяем, что точка входит в матрцу, а после ищем координату по каждой из осей в этой матрице.
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
##### Структура дерева и "добавление" к дереву прямоугольника.
Дерево имеет сумму (количесто прямоугольников в промежутке), двух потомков и границы промежутка.
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
##### Добавление новых деревьев в массив деревьев.
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
##### Проверка точкек
Опроделяем, входит ли наша точка хоть в один прямоугольник. После ищем соответствующее дерево и соответствущий индек в этом дереве и добавляем значение этого узла.
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
Таблица с графиками и данными.
https://docs.google.com/spreadsheets/d/1Ki-PE-TQWDd7N7cYA9GxE48JqQVPAcve-c0c7U0acMg/edit?usp=sharing

##### Общее время работы
![image](https://github.com/IljaNoskov/algorithsm_lab2/assets/99073996/0f9a581c-7501-406f-8299-e28819ff0ba6)

##### Время подготовки
![image](https://github.com/IljaNoskov/algorithsm_lab2/assets/99073996/b9d4708f-755e-4d25-90f4-5c8ab10e4397)

##### Время поиска ответов для точек
![image](https://github.com/IljaNoskov/algorithsm_lab2/assets/99073996/20243fbb-74c8-484b-a46e-1fd3f42cd8fe)

По графикам видно, что самым эффективным алгоритмом на данных с равным количеством точек и прямоугольников является алгоритм перебора. Решение при помощи матрицы в сотни раз медленне. Решение при помощи дерева отрезков на этих данных очень близко ко времени решения перебором.

#### Вывод:
M - количество прямоугольников, N - количество точек.
###### 1) Время подготовки 
Для этих данных не учитывается время считывания данных.
На графике наиболее отчётливо выделяется время посмтроения карты. Именно этот алгоритм занимает больше всего времени, также имеет наибольшую ассимптотику и в теории O(m^3). График подготовки для решения перебором представляет собой прямую y = 0, так как в этом алгоритме нет подготовки данных. 
###### 2) Поиск решения для точек
Тут учитывается только перебор точек и поиск решения для каждой по соответствующему алгоритму. На графике отчётливо выделяется график решения перебором. Именно он занимает больше всего времени, а его асимптотика O(M*N). Другие же графики совсем не отличаются друг от друга и тоже близки к прямой y = 0. Вероятно, время поиска ответов для точек будет меньше для алгоритма картой, но это будет заметно только на большем количестве точек. Маловероятно, что эта разница во времени будет критической.
###### 3) Общее время
Тут учитывается время работы всего алгоритма. На данных соотношении M:N ~ 1:1 лучшим алгоритмом будет алгоритм перебора. От него заметно, но не сильно отстаёт алгоритм решения при помощи дерева. А алгоритм решения матрицей работает не в пример долго. Очевидно, что при изменении этого соотношения в сторону увеличения количества точек сделает выбор алгоритма дерева предпочтительнее.

#### Итог.
Самый медленный алгоритм - алгоритм решения картой.
Самый быстрый на близких M и N,а также на N > M- полный перебор.
Самый быстрый на M >> N - алгоритм решения при помощи дерева отрезков.
