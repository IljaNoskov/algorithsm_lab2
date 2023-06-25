def tree_r(parms, points):
    import time
    result = []
    start_time = time.time()

    def therd_arg(mas):
        return mas[2]

    def bins(arr, num, start, stop):
        if start >= stop:
            return start
        mid = (start + stop) // 2
        if arr[mid] == num or (arr[mid] < num < arr[mid + 1]):
            return mid
        elif arr[mid] < num:
            return bins(arr, num, mid + 1, stop)
        else:
            return bins(arr, num, start, mid - 1)

    class Tree:
        def __init__(self, left_gr=None, right_gr=None, left_ch=None, right_ch=None, cargo=0, ):
            self.cargo = cargo
            self.left_ch = left_ch
            self.right_ch = right_ch
            self.left_gr = left_gr
            self.right_gr = right_gr

        def print_tree(self, end="\n"):
            if self == None: return
            if end == "\n":
                print(self.left_gr, self.right_gr, self.cargo, sep=",")
            else:
                print(self.left_gr, self.right_gr, self.cargo, sep=",", end=end + "  ")
            self.left_ch.print_tree(end="")
            self.right_ch.print_tree()

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

        def is_child(self):
            return (self.left_ch is not None) or (self.right_ch is not None)

        def sum_tree(self, y_point):
            if self is None:
                return int(0)
            sum_t = self.cargo
            mid_ind = (self.left_gr + self.right_gr) // 2
            if mid_ind >= y_point:
                if not self.left_ch is None:
                    return sum_t + self.left_ch.sum_tree(y_point)
            else:
                if not self.right_ch is None:
                    return sum_t + self.right_ch.sum_tree(y_point)
            return sum_t

    def build_tree(start_ind, end_ind) -> Tree:
        if start_ind >= end_ind:
            return Tree(start_ind, end_ind)
        else:
            mid_ind = (start_ind + end_ind) // 2
            left = build_tree(start_ind, mid_ind)
            right = build_tree(mid_ind + 1, end_ind)
            root = Tree(start_ind, end_ind, left, right)
            return root

    q_num = len(parms)
    q_x_points = []
    q_y_points = []
    q_mas = []
    for q in range(q_num):
        if parms[q][1] not in q_y_points:
            q_y_points.append(parms[q][1])
        if parms[q][3] not in q_y_points:
            q_y_points.append(parms[q][3])

        if parms[q][0] not in q_x_points:
            q_x_points.append(parms[q][0])
        if parms[q][2] not in q_x_points:
            q_x_points.append(parms[q][2])

    q_y_points = sorted(q_y_points)
    q_x_points = sorted(q_x_points)

    que = []
    squares = sorted(parms)
    Tree_mas = []
    new_tree = build_tree(0, len(q_y_points) - 1)
    sq_ind = 0
    sum_sotr_time = 0
    for sq in q_x_points:
        while sq_ind < len(squares) and squares[sq_ind][0] == sq:
            sort_time = time.time() * 100
            new_tree = new_tree.plus_to_tree(bins(q_y_points, squares[sq_ind][1], 0, len(q_y_points)),
                                             bins(q_y_points, squares[sq_ind][3], 0, len(q_y_points))-1, 1)
            sum_sotr_time += time.time() * 100 - sort_time

            que.append(squares[sq_ind])
            que.sort(key=therd_arg)
            sq_ind += 1
        while len(que) > 0 and sq >= que[0][2]:
            sort_time = time.time() * 100
            new_tree = new_tree.plus_to_tree(bins(q_y_points, que[0][1], 0, len(q_y_points)),
                                             bins(q_y_points, que[0][3], 0, len(q_y_points))-1, -1)
            sum_sotr_time += time.time() * 100 - sort_time
            que.pop(0)
        Tree_mas.append(new_tree)

    prepare_time = time.time() - start_time
    start_time = time.time()

    for p in points:
        if p[0] < q_x_points[0] or p[0] > q_x_points[-1]:
            result.append(0)
            continue
        if p[1] < q_y_points[0] or p[1] > q_y_points[-1]:
            result.append(0)
            continue
        x = bins(q_x_points, p[0], 0, len(q_x_points))
        y = bins(q_y_points, p[1], 0, len(q_y_points))
        result.append(Tree_mas[x].sum_tree(y))
    search_time = (time.time() * 100 - start_time * 100) / 100
    sum_sotr_time /= 100
    return result, prepare_time, search_time, sum_sotr_time
