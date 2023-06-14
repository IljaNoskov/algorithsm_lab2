def tree_r(parms, points):
    result = []

    class Tree:
        def __init__(self, left_gr=None, right_gr=None, left_ch=None, right_ch=None, cargo=0, ):
            self.cargo = cargo
            self.left_ch = left_ch
            self.right_ch = right_ch
            self.left_gr = left_gr
            self.right_gr = right_gr

    def bins(arr, num, start, stop):
        if start >= stop:
            return start
        mid = (start + stop) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            return bins(arr, num, mid + 1, stop)
        else:
            return bins(arr, num, start, mid - 1)

    def print_tree(tree, end="\n"):
        if tree == None: return
        if end == "\n":
            print(tree.left_gr, tree.right_gr, tree.cargo, sep=",")
        else:
            print(tree.left_gr, tree.right_gr, tree.cargo, sep=",", end=end + "  ")
        print_tree(tree.left_ch, end="")
        print_tree(tree.right_ch)

    def bild_tree(start_ind, end_ind):
        if start_ind >= end_ind:
            return Tree(start_ind, end_ind)
        else:
            mid_ind = (start_ind + end_ind) // 2
            left = bild_tree(start_ind, mid_ind)
            right = bild_tree(mid_ind + 1, end_ind)
            root = Tree(start_ind, end_ind, left, right)
            return root

    def therd_arg(mas):
        return mas[2]

    def plus_to_tree(t_tree, start_index, end_index, num) -> Tree:
        if t_tree == None:
            return t_tree
        tree = Tree(t_tree.left_gr, t_tree.right_gr, t_tree.left_ch, t_tree.right_ch, t_tree.cargo)
        if tree.left_gr >= start_index and tree.right_gr <= end_index:
            tree.cargo += num
        elif tree.right_gr >= start_index or tree.left_gr <= end_index:
            tree.left_ch = plus_to_tree(tree.left_ch, start_index, end_index, num)
            tree.right_ch = plus_to_tree(tree.right_ch, start_index, end_index, num)
        return tree

    def is_childe(tree):
        return (tree.left_ch is not None) or (tree.right_ch is not None)

    def sum_tree(tree, y_point):
        if tree == None:
            return 0
        sum = tree.cargo
        mid_ind = (tree.left_gr + tree.right_gr) // 2
        if mid_ind >= y_point:
            return sum + sum_tree(tree.left_ch, y_point)
        else:
            return sum + sum_tree(tree.right_ch, y_point)

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
    new_tree = bild_tree(q_y_points[0], q_y_points[-1])
    sq_ind = 0
    for sq in q_x_points:
        while sq_ind < len(squares) and squares[sq_ind][0] == sq:
            new_tree = plus_to_tree(new_tree, squares[sq_ind][1], squares[sq_ind][3], 1)
            que.append(squares[sq_ind])
            que.sort(key=therd_arg)
            sq_ind += 1
        while len(que) > 0 and sq >= que[0][2]:
            new_tree = plus_to_tree(new_tree, que[0][1], que[0][3], -1)
            que.pop(0)
        Tree_mas.append(new_tree)

    for p in points:
        if p[0] < q_x_points[0] or p[0] > q_x_points[-1]:
            print(0, end=' ')
            continue
        if p[1] < q_y_points[0] or p[1] > q_y_points[-1]:
            print(0, end=' ')
            continue
        result.append(sum_tree(Tree_mas[bins(q_x_points, p[0], 0, len(q_x_points))], p[1]))
    return result
