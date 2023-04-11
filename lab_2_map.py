def bins(arr, num, start=0, stop=-1):
    if stop == -1:
        stop = len(arr)-1
    if start >= stop:
        return start
    mid = (start+stop)//2
    if arr[mid] == num:
        return mid
    elif arr[mid] < num:
        return bins(arr, num, mid+1, stop)
    else:
        return bins(arr, num, start, mid-1)

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(*matrix[i])
    print()

# Собираем данные (координаты квадратов и точек)
square_num=int(input())
sq_x_point=[]
sq_y_point=[]
set_x=set()
set_y=set()
for square in range(square_num):
    line = input().split()
    for i in range(len(line)):
        line[i]=int(line[i])
    sq_x_point.append([line[0], line[2]])
    sq_y_point.append([line[1], line[3]])
    set_x.add(line[0])
    set_x.add(line[2])
    set_y.add(line[1])
    set_y.add(line[3])
point_num=int(input())
point_mas=[]
for point in range(point_num):
    line = input().split()
    for i in range(len(line)):
        line[i] = int(line[i])
    point_mas.append(line)

x_points = list(set_x)
y_points = list(set_y)
#print(x_points,y_points)

map_sq = []
for i in range(len(x_points)*2):
    map_sq.append([])
    for k in range(len(y_points)*2):
        map_sq[i].append(0)

for sq in range(square_num):
    #print(bins(x_points, sq_x_point[sq][0]), bins(x_points, sq_x_point[sq][1]))
    for i in range(bins(x_points, sq_x_point[sq][0])*2, bins(x_points, sq_x_point[sq][1])*2+1):
        for j in range(bins(y_points, sq_y_point[sq][0])*2, bins(y_points, sq_y_point[sq][1])*2+1):
            map_sq[i][j] += 1
#print_matrix(map_sq)

for point in point_mas:
    if ((point[0]<x_points[0] or point[0]>x_points[-1])
            or (point[1]<y_points[0] or point[1]>y_points[-1])):
        print(0,end=' ')
    else:
        x = bins(x_points, point[0])
        y = bins(y_points, point[1])
        #print(x, y, *point, end=' ')
        if x_points[x] == point[0]:
            x *= 2
        elif x_points[x] >= point[0]:
            x = x*2-1
        else:
            x = x*2+1
        if y_points[y] == point[1]:
            y *= 2
        elif y_points[y] >= point[1]:
            y = y*2-1
        else:
            y = y*2+1
        print(map_sq[x][y], end=' ')