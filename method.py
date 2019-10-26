import numpy as np


def init_matrix():
    size = 3
    mat = np.zeros((size, size))

    for i in range(size):
        for j in range(size):
            mat[i][j] = float(input("Input mat[" + str(i) + "][" + str(j) + "]: "))

    return mat


def init_vector():
    vector = np.zeros((3, 1))

    for i in range(3):
        vector[i] = float(input("Input x[" + str(i) + "]: "))

    return vector


def calc_next_x(a, x):
    return a@x


def calc_lambda(x1, x0):
    val1 = x1[0] * x0[0] + x1[1] * x0[1] + x1[2] * x0[2]
    val2 = x0[0] * x0[0] + x0[1] * x0[1] + x0[2] * x0[2]
    return val1/val2


def matrix_module(mat):
    size = len(mat[0])
    sum = 0
    val_arr = []
    for i in range(size):
        for j in range(size):
            sum += abs(mat[i][j])
        val_arr.append(sum)
        sum = 0

    return max(val_arr)


def find_max_lambda(a, x0, ell):
    x1 = calc_next_x(a, x0)
    lambda1 = calc_lambda(x1, x0)
    x2 = calc_next_x(a, x1)
    lambda2 = calc_lambda(x2, x1)

    while abs(lambda2 - lambda1) > ell:
        x1 = calc_next_x(a, x2)
        lambda1 = calc_lambda(x1, x2)
        x2 = calc_next_x(a, x1)
        lambda2 = calc_lambda(x2, x1)

    return lambda2


def find_min_lambda(a, x0, ell):
    module_a = matrix_module(a)
    b = module_a * np.eye(3) - a
    lambda_max_b = find_max_lambda(b, x0, ell)
    return module_a - lambda_max_b

