import numpy as np
from scipy.io import loadmat
from sklearn import svm
from collections import OrderedDict
from process_email import process_email
from process_email import email_features
from process_email import get_dictionary

# task1
with open('email.txt', 'r') as file:
    email = file.read().replace('\n', '')
print(email)

# task2
proc_email = process_email(email)
# for i in proc_email:
#     print(i, end=' ')

# task 3
features = email_features(proc_email)
print(f"Длина вектора признаков: {len(features)}")
print(f"Количество ненулевых результатов: {sum(features > 0)}")

# task 4
data = loadmat("train.mat")
X = data["X"]
y = data["y"].flatten()
print('Тренировка SVM-классификатора с линейным ядром...')
clf = svm.SVC(C=0.1, kernel='linear', tol=1e-3)
model = clf.fit(X, y)
p = model.predict(X)
accuracy = (1 - np.mean(p != y.ravel())) * 100
print(f"Точность на обучающей выборке: {accuracy}%")

# task 5
data = loadmat('test.mat')
X = data['Xtest']
y = data['ytest'].flatten()
p = model.predict(X)
accuracy = (1 - np.mean(p != y.ravel())) * 100
print('Точность на тестовой выборке: ', accuracy)

# task 6
t = sorted(list(enumerate(model.coef_[0])), key=lambda e: e[1], reverse=True)
d = OrderedDict(t)
idx = list(d.keys())
weight = list(d.values())
dictionary = get_dictionary()
print('Топ-15 слов в письмах со спамом: ')
for i in range(15):
    print(' %-15s (%f)' % (dictionary[idx[i]], weight[i]))

# task 7
with open('email2.txt', 'r') as file:
    email2 = file.read().replace('\n', '')
proc_email2 = process_email(email2)
features2 = email_features(proc_email2)
p2 = model.predict([features2])
accuracy = np.mean(p2 == features2) * 100
accuracy = np.round(accuracy, 3)
print(f'Вероятность, что письмо - спам: {accuracy}%')
