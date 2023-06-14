def data_gen(a_count, just_N=103, p_x=76283, p_y=75797):
    squares = []
    points = []
    for i in range(a_count):
        squares.append([10 * i, 10 * i, 10 * (2 * just_N - i), 10 * (2 * just_N - i)])

    for i in range(a_count):
        points.append([((p_x * i) ** 31) % (20 * just_N),
                       ((p_y * i) ** 31) % (20 * just_N)])

    return squares, points
