import copy
import time
import numpy as np


def get_length(distance_matrix, index1, index2):
    return distance_matrix[index1, index2]


def sequence(indices, distance_matrix):
    overall_distance = 0
    for i in range(0, len(indices) - 1):
        overall_distance += get_length(distance_matrix, indices[i], indices[i + 1])
    overall_distance+= get_length(distance_matrix, indices[0], indices[len(indices) - 1])
    return overall_distance


def randomswap_m(m2):
    """
        :param m2:
            np matrix obj, matrix to swap 2 random rows
        :return:
            np matrix obj, m2 with swapped two random rows
    """
    m = copy.copy(m2)
    idx1, idx2 = generate_swap_indexes_m(m2)
    m[idx1], m[idx2] = m[idx2], m[idx1]
    return m


def generate_swap_indexes_m(m):
    return [np.random.randint(1, len(m)), np.random.randint(1, len(m))]


def randomswap_m2(m2):
    """
    :param m2:
        np matrix obj, matrix to swap 2 random rows
    :return:
        np matrix obj, m2 with swapped two random rows
    """
    m = copy.copy(m2)
    where_to_put, what_to_put = generate_swap_indexes_m(m)
    if what_to_put >= where_to_put:
        x = where_to_put
        y = what_to_put
    else:
        x = what_to_put
        y = where_to_put
    reverse = m[x:y]
    reverse = np.flip(reverse, axis=0)
    m[x:y] = reverse
    return m


def randomswap_m3(m2):
    """
    :param m2:
        np matrix obj, matrix to swap 2 random rows
    :return:
        np matrix obj, m2 with swapped two random rows
    """
    m = copy.copy(m2)
    rnd = np.random.randint(4, 8)
    interval = np.random.randint(2, rnd)
    middle = np.random.randint(interval, len(m) - interval - 1)
    temp = copy.copy(m[(middle - interval):middle])
    m[(middle - interval):middle] = m[(middle + 1):(interval + middle + 1)]
    m[(middle + 1):(interval + middle + 1)] = temp
    return m


def calculate_moves2(m, tl, zeros, distance_matrix):
    """
    This is used to calculate every possible swap of 2 rows, and find the best swap
    :param zeros:
        bool, used to specify allowing zero time change swaps
    :param m:
        np matrix obj on which all possible swaps of 2 different rows will be made
    :param tl:
        np matrix obj, size len(m) x len(m), tabu list with blocked swaps
    :return:
        List of 3 ints, first and second are indexes of rows to swap to get best result in time save/loss
        third is how much time is saved/lost by this swap
    """
    dist = sequence(m, distance_matrix)
    move = [0, 0, 99999]
    for i in range(0, len(m)):
        for j in range(i + 1, len(m)):
            if is_not_present_in_tl(tl, i, j):
                m2 = swap(m, i, j)
                delta_time = sequence(m2, distance_matrix) - dist
                if zeros:
                    if delta_time < move[2]:
                        move = [i, j, delta_time]
                else:
                    if delta_time < move[2] and delta_time != 0:
                        move = [i, j, delta_time]
    return move


def swap(mt, x, y):
    """
    :param mt:
        np matrix obj, matrix to swap rows
    :param x:
        int, row index to swap
    :param y:
        int, row index to swap
    :return:
        np matrix obj, with swapped x and y rows
    """
    m = copy.copy(mt)
    m[x], m[y] = m[y], m[x]
    return m


def is_not_present_in_tl(tl, i, j):
    """
    This method checks if the move about to be made is in tabu list (blocked moves list)
    :param tl:
        np matrix obj, tabu list
    :param i:
        int, row index to swap
    :param j:
        int, row index to swap
    :return:
        False if swap is prohibited by Tabu list
        True otherwise
    """
    return 0 == tl[i, j] and 0 == tl[j, i]


def update_tabu_list(tl):
    """
    Updates tabu list after iteration end
    """
    for i in range(0, len(tl)):
        for j in range(0, len(tl)):
            if tl[i][j] > 0:
                tl[i][j] -= 1
    return tl

def initrandomswaps_m(m, n):
    """
    Initiates population size n using initrandomswap on m
    """
    population = []
    for i in range(0, n):
        best_solution = np.arange(1, len(m))
        np.random.shuffle(best_solution)
        population.append(copy.copy(best_solution))
    return population

def select_best_child(solutions, distance_matrix):
    """
    Select best matrix from current population
    """
    mini = sequence(solutions[0],distance_matrix)
    mat = solutions[0]
    for solution in solutions:
        if sequence(solution, distance_matrix) < mini:
            mat = solution
    return mat

def select_best_solutions(population, n, distance_matrix):
    """
    Select pairs to cross from population
    The parents are beeing chosen according to dist. function intervals.
    :param population:
        list of np matrix obj, list from which to chose matrices to cross
    :param n:
        int, size of population
    :return:
        n/2 element list of 2 np matrixes,
        meaning returns n/2 pairs ready to be crossed
    """
    population_with_distances = []
    suma = 0
    # calculate times for everyone in population
    ind = 0
    for parent in population:
        s = sequence(parent, distance_matrix)
        population_with_distances.append([ind, s])
        suma += s
        ind += 1
    # divide time by sum of all times to get the probablilities
    for parent_and_time in population_with_distances:
        parent_and_time[1] = parent_and_time[1] / suma
    # sort population and times by probablilities
    sorted(population_with_distances, key=lambda x: x[1])
    poprzedni = 0
    # change probabilities to distribution
    for parent_and_time in population_with_distances:
        temp = parent_and_time[1]
        parent_and_time[1] = poprzedni + parent_and_time[1]
        poprzedni += temp
    # reverse distribution (the lower the higher change to pick)
    d = []
    for parent_and_time in population_with_distances:
        d.append(parent_and_time[1])
    d.reverse()
    # replace distribution with the reversed one
    reversed_parent_and_time = []
    for i in range(0, len(d)):
        reversed_parent_and_time.append([population_with_distances[i][0], d[i]])
    reversed_parent_and_time.reverse()
    # select pairs from population according to population size and distribution intervals
    selected_population = []
    for i in range(1, int(n / 2) + 1):
        parents = []
        while len(parents) != 2:
            random = np.random.random()
            for parent_and_time in reversed_parent_and_time:
                if parent_and_time[1] > random and parent_and_time[0] not in parents:
                    parents.append(parent_and_time[0])
                    break
            selected_population.append(parents)
    all_pairs = []
    for p in selected_population:
        all_pairs.append([population[p[0]], population[p[1]]])
    return all_pairs


def mutate_children(solutions, rswaps):
    """
    Mutate every matrix in population, meaning make rswaps number of random
    swaps in every matrix in solutions
    """
    for solution in solutions:
        for i in range(0, rswaps):
            solution = randomswap_m(solution)
    return solutions

def cross_indexes(tasks1, tasks2, div1, div2):
    """
    OX crossing
    :param tasks1:
        parent 1
    :param tasks2:
        parent 2
    :param div1:
        crossing point 1
    :param div2:
        crossing point 2
    :return:
        indexes of children crossed by OX
    """
    tasks_m = []
    tasks_s = []
    tasks_e = []
    start = div1
    end = div2
    for i in range(start, end):
        tasks_m.append(tasks1[i])
    for i in range(end, len(tasks1)):
        if tasks2[i] not in tasks_m and tasks2[i] not in tasks_s and tasks2[i] not in tasks_e:
            tasks_e.append(tasks2[i])
    for i in range(0, len(tasks1)):
        if tasks2[i] not in tasks_m and tasks2[i] not in tasks_s and tasks2[i] not in tasks_e:
            tasks_s.append(tasks2[i])
    tasks_rdy1 = tasks_s + tasks_m + tasks_e
    tasks_m = []
    tasks_s = []
    tasks_e = []
    for i in range(start, end):
        tasks_m.append(tasks2[i])
    for i in range(end, len(tasks2)):
        if tasks1[i] not in tasks_m and tasks1[i] not in tasks_s and tasks1[i] not in tasks_e:
            tasks_e.append(tasks1[i])
    for i in range(0, len(tasks2)):
        if tasks1[i] not in tasks_m and tasks1[i] not in tasks_s and tasks1[i] not in tasks_e:
            tasks_s.append(tasks1[i])
    tasks_rdy2 = tasks_s + tasks_m + tasks_e
    return tasks_rdy1, tasks_rdy2


def cross_indexes2(tasks1, tasks2, div1, div2):
    """
    PMX crossing
    :param tasks1:
        parent1
    :param tasks2:
        parent2
    :param div1:
        cross point 1
    :param div2:
        cross point 2
    :return:
        indexes of children crossed by PMX
    """
    tasks_m = []
    tasks_s = []
    tasks_e = []
    start = div1
    end = div2
    swap_map = []
    for i in range(start, end):
        tasks_m.append(tasks1[i])
        swap_map.append([tasks1[i], tasks2[i]])
    for i in range(0, start):
        task = tasks2[i]
        while task in tasks_e or task in tasks_s or task in tasks_m:
            for swapp in swap_map:
                if swapp[0] == task:
                    task = swapp[1]
                    break
        tasks_s.append(task)
    for i in range(end, len(tasks1)):
        task = tasks2[i]
        while task in tasks_e or task in tasks_s or task in tasks_m:
            for swapp in swap_map:
                if swapp[0] == task:
                    task = swapp[1]
                    break
        tasks_e.append(task)

    tasks_rdy1 = tasks_s + tasks_m + tasks_e

    tasks_m = []
    tasks_s = []
    tasks_e = []
    start = div1
    end = div2
    swap_map = []
    for i in range(start, end):
        tasks_m.append(tasks2[i])
        swap_map.append([tasks2[i], tasks1[i]])
    for i in range(0, start):
        task = tasks1[i]
        while task in tasks_e or task in tasks_s or task in tasks_m:
            for swapp in swap_map:
                if swapp[0] == task:
                    task = swapp[1]
                    break
        tasks_s.append(task)
    for i in range(end, len(tasks1)):
        task = tasks1[i]
        while task in tasks_e or task in tasks_s or task in tasks_m:
            for swapp in swap_map:
                if swapp[0] == task:
                    task = swapp[1]
                    break
        tasks_e.append(task)
    tasks_rdy2 = tasks_s + tasks_m + tasks_e

    print(tasks_rdy1)
    print(tasks_rdy2)
    return tasks_rdy1, tasks_rdy2


def produce_children1(parents, div1, div2, cross):
    """
    Cross two parents to obtain 2 children
    :param parents:
        list of two matrices
    :param div1:
        cross point 1
    :param div2:
        cross point 2
    :param cross:
        0 - OX, 1 - PMX crossing
    :return:
        2 new matrices obtained by crossing 2 given matrices
    """
    new_population = []
    for pair in parents:
        if cross == 0:
            ch_indx1, ch_indx2 = cross_indexes(pair[0], pair[1], div1, div2)
        else:
            ch_indx1, ch_indx2 = cross_indexes2(pair[0], pair[1], div1, div2)
        new_population.append(ch_indx1)
        new_population.append(ch_indx2)
    return new_population


def calc_nearest(row, cities):
    mini_index = -1
    mini = 99999
    for i in range(0, len(row)):
        if row[i]<mini and i not in cities:
            mini_index=i
            mini=row[i]
    return mini_index