import sys

import scipy.io as sio
import numpy as np
import lib.svm as svm


def task1():
    mat = sio.loadmat("dataset1.mat")
    y = np.float64(mat["y"])
    x = np.float64(mat["X"])
    svm.visualize_boundary_linear(x, y, "", "Данные из файла dataset1.mat")


def task2(C):
    mat = sio.loadmat("dataset1.mat")
    y = np.float64(mat["y"])
    x = np.float64(mat["X"])
    model = svm.svm_train(x, y, C, svm.linear_kernel, 0.001, 20)
    svm.visualize_boundary_linear(x, y, model, f"Разделяющая граница при C = {C}")


def task3(C):
    task2(C)


def task4():
    svm.contour(1)
    svm.contour(4)


def task5():
    mat = sio.loadmat("dataset2.mat")
    y = np.float64(mat["y"])
    x = np.float64(mat["X"])
    svm.visualize_boundary_linear(x, y, "", "Данные из файла dataset2.mat")


def task6():
    mat = sio.loadmat("dataset2.mat")
    y = np.float64(mat["y"])
    x = np.float64(mat["X"])
    C = 1.0
    sigma = 0.1
    gaussian = svm.partial(svm.gaussian_kernel, sigma=sigma)
    gaussian.__name__ = svm.gaussian_kernel.__name__
    model = svm.svm_train(x, y, C, gaussian)
    svm.visualize_boundary(x, y, model)


def task7():
    data2 = sio.loadmat('dataset3.mat')
    Xval = data2['Xval']
    yval = data2['yval']
    y2 = np.float64(data2['y'])
    X2 = data2['X']
    svm.visualize_boundary_linear(X2, y2, None, title="Задание 7. Обучающая выборка")
    svm.visualize_boundary_linear(Xval, yval, None, title="Задание 7. Тестовая выборка")


def task8(C, sigma):
    data2 = sio.loadmat('dataset3.mat')
    y = np.float64(data2['y'])
    x = data2['X']
    gaussian = svm.partial(svm.gaussian_kernel, sigma=sigma)
    gaussian.__name__ = svm.gaussian_kernel.__name__
    model = svm.svm_train(x, y, C, gaussian)
    svm.visualize_boundary(x, y, model)


def task9():
    data2 = sio.loadmat('dataset3.mat')
    Xval = data2['Xval']
    yval = data2['yval']
    y = np.float64(data2['y'])
    X = data2['X']

    minError = sys.maxsize
    C = 0
    sigma = 0

    for C_ in [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30]:
        for sigma_ in [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30]:
            gaussian_ = svm.partial(svm.gaussian_kernel, sigma=sigma_)
            gaussian_.__name__ = svm.gaussian_kernel.__name__
            model_ = svm.svm_train(X, y, C_, gaussian_)

            ypred = svm.svm_predict(model_, Xval)

            error = np.mean(ypred != yval.ravel())
            if error < minError:
                minError = error
                C = C_
                sigma = sigma_

    print(error)
    gaussian = svm.partial(svm.gaussian_kernel, sigma=sigma)
    gaussian.__name__ = svm.gaussian_kernel.__name__
    model = svm.svm_train(X, y, C, gaussian)
    svm.visualize_boundary(X, y, model)


if __name__ == '__main__':
    task1()
    task2(1)
    task3(100)
    task4()
    task5()
    task6()
    task7()
    task8(1, 0.5)
    task9()
