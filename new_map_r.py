def map_r(squares, points):
    import time
    result = []
    start_time = time.time()
    def bins(arr, num, start, stop):
        if start >= stop:
            return stop
        mid = (start + stop) // 2
        if arr[mid] == num or (arr[mid] < num < arr[mid+1]):
            return mid
        elif arr[mid] < num:
            return bins(arr, num, mid + 1, stop)
        else:
            return bins(arr, num, start, mid - 1)

    def print_matrix(matrix):
        for mat in range(len(matrix)):
            print(matrix[mat])

    square_num = len(squares)
    sq_x_points = []
    sq_y_points = []
    x_points = []
    y_points = []
    for sq in squares:
        sq_x_points.append([sq[0], sq[2]])
        sq_y_points.append([sq[1], sq[3]])
        x_points.append(sq[0])
        x_points.append(sq[2])
        y_points.append(sq[1])
        y_points.append(sq[3])
    x_points = sorted(list(x_points))
    y_points = sorted(list(y_points))

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

    end_prepair = time.time() - start_time
    start_time = time.time()

    for point in points:
        if ((point[0] < x_points[0] or point[0] >= x_points[-1])
                or (point[1] < y_points[0] or point[1] >= y_points[-1])):
            result.append(0)
        else:
            x = bins(x_points, point[0], 0, len(x_points))
            y = bins(y_points, point[1], 0, len(y_points))
            result.append(map_sq[x][y])

    end_search = time.time() - start_time
    return result, end_prepair, end_search
