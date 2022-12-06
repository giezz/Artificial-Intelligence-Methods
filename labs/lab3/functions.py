import numpy as np


def compute_cost(X, y, theta):
    m = X.shape[0]
    X_ones = np.c_[np.ones((m, 1)), X]
    h_x = X_ones * theta
    difference = np.power(h_x - y, 2)
    sum_ = np.sum(difference)
    cost = 1 / (2 * m) * sum_
    return cost


def gradient_descent(X, y, alpha, iterations):
    m = X.shape[0]
    X_ones = np.c_[np.ones((m, 1)), X]
    n = X_ones.shape[1]
    theta = np.matrix(np.ones(n)).T
    theta[0] = 0
    J_theta = np.matrix(np.zeros(iterations)).T

    temp_theta = theta
    for i in range(iterations):
        h_x = X_ones * temp_theta
        difference = np.power(h_x - y, 2)
        sum_ = np.sum(difference)
        J_theta[i] = 1 / (2 * m) * sum_
        temp_theta = temp_theta - alpha * 1 / m * np.dot(X_ones.T, (h_x - y))

    return J_theta, temp_theta
