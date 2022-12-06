import numpy as np
import matplotlib.pyplot as plt

from labs.lab3.functions import compute_cost, gradient_descent

data = np.matrix(np.loadtxt('ex1data1.txt', delimiter=','))
X = data[:, 0]
y = data[:, 1]
plt.plot(X, y, 'bo')
plt.title('Зависимость прибыли ности от численности')
plt.xlabel('Численность')
plt.ylabel('Прибыль')
plt.show()
theta = np.matrix([1, 2]).T

print(compute_cost(X, y, theta))

J_theta, theta = gradient_descent(X, y, 0.02, 500)
print(theta)
plt.plot(J_theta)
plt.title('Снижение ошибки при градиентном спуске')
plt.xlabel('Итерация')
plt.ylabel('Ошибка')
plt.show()

# task 5
population = np.array([1., 9., 3])
prediction = np.squeeze(np.asarray(theta[1] * population + theta[0]))
print(f"prediction of income: {prediction}")

# task 6
plt.plot(X, y, 'bo')
plt.title('Зависимость прибыль ности от численности')
plt.xlabel('Численность')
plt.ylabel('Прибыль')
x = np.arange(min(X), max(X))
f_x = np.squeeze(np.asarray(theta[1] * x + theta[0]))
plt.plot(x, f_x, 'g--')
plt.show()

# ---part 2---

# task 7
data = np.matrix(np.loadtxt('ex1data2.txt', delimiter=','))
X = data[:, 0]
y = data[:, 1]
z = data[:, 2]

m_X = np.mean(X, axis=0)
s_X = np.std(X, axis=0)
X = (X - m_X) / s_X

m_y = np.mean(y, axis=0)
s_y = np.std(y, axis=0)
y = (y - m_y) / s_y

m_z = np.mean(z, axis=0)
s_z = np.std(z, axis=0)
z = (z - m_z) / s_z

x_y = np.c_[X, y]


J_theta, theta = gradient_descent(x_y, z, 0.02, 500)
print(f"prediction of income: {prediction}")
print(theta)
plt.plot(J_theta)
plt.title('Снижение ошибки при градиентном спуске')
plt.xlabel('Итерация')
plt.ylabel('Ошибка')
plt.show()

# task 9
x_y_ones = np.c_[np.ones((x_y.shape[0], 1)), x_y]
mnk = np.dot(np.linalg.pinv(np.dot(x_y_ones.T, x_y_ones)),
             np.dot(x_y_ones.T, z))
print(mnk)






