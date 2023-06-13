def read_all():
    def read_pram():
        n = int(input())
        mas = []
        for i in range(n):
            s = input().split()
            mas.append([int(s[0]), int(s[1]), int(s[2]), int(s[3])])
        return mas

    def read_point():
        n = int(input())
        mas = []
        for i in range(n):
            s = input().split()
            mas.append([int(s[0]), int(s[1])])
        return mas

    prams = read_pram()
    points = read_point()
    return prams, points
