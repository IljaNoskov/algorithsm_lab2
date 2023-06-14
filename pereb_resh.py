def pereb_r(parms, points):
    result = []
    for point in points:
        m = 0
        for parm in parms:
            if (parm[0] <= point[0] < parm[2]) and (parm[1] <= point[1] < parm[3]):
                m += 1
        result.append(m)
    return result
