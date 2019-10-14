import numpy as np
import random


def create():
    return np.reshape(np.matrix([random.randint(-1, 1) for i in range(0, 16)]), (4, 4))

def createRegular():
    m = None
    det = 0
    while det == 0:
        m = create()
        m[0:1, :] = 1
        m[1:2, :] = [1, -1, 0, 0]
        m[2:3, :] = [0, 0, 1, -1]
        det = np.linalg.det(m)
    return m


def createSingular():
    m = None
    det = 10
    while det > 0.1:
        m = create()
        m[0:1, :] = 1
        m[1:2, :] = [1, -1, 0, 0]
        det = abs(np.linalg.det(m))
    return m


DAY_OF_MONTH=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def checkBirthday(mat):
    results = dict()
    for i in range(0, 12):
        for j in range(0, DAY_OF_MONTH[i]):
            m1, m2 = divmod(i+1, 10)
            d1, d2 = divmod(j+1, 10)
            v = np.asmatrix([m1, m2, d1, d2]).transpose()
            r = np.matmul(mat, v)
            results[str(r.tolist())] = v
    return len(results) == 365, results


DAY_OF_MONTH_LEAP=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def checkBirthdayLeap(mat):
    results = dict()
    for i in range(0, 12):
        for j in range(0, DAY_OF_MONTH_LEAP[i]):
            m1, m2 = divmod(i+1, 10)
            d1, d2 = divmod(j+1, 10)
            v = np.asmatrix([m1, m2, d1, d2]).transpose()
            r = np.matmul(mat, v)
            results[str(r.tolist())] = v
    return len(results) == 366, results


def createBirthdayMatrix():
    cnt = 0
    while True:
        mat = createSingular()
        ok, ndict = checkBirthday(mat)
        if ok:
            leap, ldict = checkBirthdayLeap(mat)
            return mat, ndict, ldict
        cnt += 1
        if (cnt % 1000) == 0:
            print(cnt)


def chapter1():
    print(createRegular())


def main():
    mat, ndict, ldict = createBirthdayMatrix()
    print(mat)
    v1 = np.matmul(mat, np.asmatrix([0, 6, 1, 6]).transpose())
    v2 = np.matmul(mat, np.asmatrix([0, 2, 2, 9]).transpose())
    print(np.linalg.det(mat))
    print(ldict[str(v1.tolist())].transpose())
    print(ndict[str(v1.tolist())].transpose())
    print(ldict[str(v2.tolist())].transpose())
    print(ndict[str(v2.tolist())].transpose())


if __name__ == '__main__':
    main()
