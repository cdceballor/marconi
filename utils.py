def tovalidxy(y, marks):
    n = marks.count(True)

    validx = [None] * n
    validy = [None] * n

    cnt = 0
    for i in range(len(y)):
        if marks[i]:
            validx[cnt] = i
            validy[cnt] = y[i]
            cnt += 1

    return validx, validy

def repair(y, marks, fn):
    for i in range(len(y)):
        if not marks[i]:
            y[i] = fn(i)

def invalidx(matches):
    return [i for i in range(len(matches)) if not matches[i]]

def replace(y, indexes, newvalues):
    for index, newval in zip(indexes, newvalues):
        y[index] = newval