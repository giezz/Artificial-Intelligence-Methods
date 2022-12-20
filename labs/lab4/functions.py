import numpy as np


def path_cost(path, A):
    path = path.astype(int)
    cost = 0
    for i in range(len(path) - 1):
        cost += A[path[i] - 1, path[i + 1] - 1]
    cost += A[path[len(path) - 1] - 1, path[0] - 1]
    return cost


def mutation(path):
    x1 = np.random.randint(low=0, high=path.size - 1)
    while True:
        x2 = np.random.randint(low=0, high=path.size - 1)
        if x2 != x1:
            break
    temp = path[x1]
    path[x1] = path[x2]
    path[x2] = temp
    return path


def short_distance(path, crossover_result, A):
    curr_index = np.where(crossover_result == 0)[0][0]
    curr_numb = int(crossover_result[curr_index - 1])
    arri = np.where(path == curr_numb)[0][0]
    for i in range(1, crossover_result.shape[0]):
        left_num = int(path[arri - i])
        right_num = int(path[(arri + i) % crossover_result.shape[0]])
        if left_num in crossover_result and right_num in crossover_result:
            continue
        if left_num in crossover_result and right_num not in crossover_result:
            crossover_result[curr_index] = right_num
            return crossover_result
        if left_num not in crossover_result and right_num in crossover_result:
            crossover_result[curr_index] = left_num
            return crossover_result
        left_num_distance = A[curr_numb - 1, left_num - 1]
        right_num_distance = A[curr_numb - 1, right_num - 1]
        if left_num_distance > right_num_distance:
            crossover_result[curr_index] = right_num
            return crossover_result
        else:
            crossover_result[curr_index] = left_num
            return crossover_result
    return crossover_result


def crossover(path1, path2, A):
    if path1.shape[0] != path2.shape[0]:
        raise Exception("path1 length != path 2 length")
    crossover_result = np.zeros(path1.shape[0])
    crossover_result[0] = np.random.choice(path1)
    for i in range(crossover_result.shape[0] - 1):
        if i == 0 or i % 2 == 0:
            crossover_result = short_distance(path1, crossover_result, A)
        else:
            crossover_result = short_distance(path2, crossover_result, A)
    return crossover_result


def generate_descendants(parents, A):
    descendants = []
    for j in range(parents.shape[0]):
        p1 = parents[j]
        for k in range(j + 1, parents.shape[0]):
            p2 = parents[k]
            child = crossover(p1[0], p2[0], A)
            descendants.append(child)
    return descendants


def generate_initial_population(amount, shape, A):
    population = np.zeros((amount, 2)).astype(np.ndarray)
    for i in range(amount):
        arange = np.arange(1, shape + 1)
        np.random.shuffle(arange)
        population[i, 0] = arange
        population[i, 1] = path_cost(arange, A)
    return population


def genetic_algorithm(parents_amount, crossovers, mutation_chance, A):
    n = A.shape[0]
    tmp_parent = np.array(generate_initial_population(parents_amount, n, A))
    for i in range(crossovers):
        descendants = generate_descendants(tmp_parent, A)
        tmp = np.zeros((len(descendants), 2)).astype(np.ndarray)
        for j in range(tmp.shape[0]):
            var = np.random.randint(0, 101)
            if var <= mutation_chance * 100:
                descendants[j] = mutation(descendants[j])
            tmp[j, 0] = descendants[j]
            tmp[j, 1] = path_cost(descendants[j], A)
        tmp = tmp[np.argsort(tmp[:, 1])]
        tmp_parent = tmp[0:n, :]
    return tmp_parent
