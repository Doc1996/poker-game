def C(AP, MI):
    try:
        if AP[MI.POO+1].coins >= 0:
            MI.POO += 1
    except:
        MI.POO = 0

    return AP[MI.POO]


def sort(L, index):
    while True:
        for i in range(0, len(L)-1):
            if L[i][index] > L[i+1][index]:
                L.append(L[i])
                del L[i]

        k = 0
        for i in range(0, len(L)-1):
            if L[i][index] <= L[i+1][index]:
                k += 1

        if k == len(L)-1:
            break

    return L
