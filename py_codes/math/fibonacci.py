#!/usr/bin/env python

def matrixMult(A, B):
    return ([A[0][0] * B[0][0] + A[0][1] * B[1][0],
             A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0],
             A[1][0] * B[0][1] + A[1][1] * B[1][1]])

def matrixExp(A, e):
    if not e:
            return [[1,0],[0,1]]
    elif e % 2:
            return matrixMult(A, matrixExp(A, e-1))
    else:
            sq = matrixExp(A, e / 2)
            return matrixMult(sq, sq)

def fibonacci(n):
    if n == 0:
        return 0
    M = [[1,1],[1,0]]
    return matrixExp(M, n - 1)[0][0]

if __name__ == "__main__":
    for i in xrange(20):
        print i, fibonacci(i)
