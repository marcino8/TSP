import Calc as c
import numpy as np
import time
import matplotlib.pyplot as plt


def sa(start_T, red_T, geom, inside_iter, no_change_number, neigh, file_to_read):
    """
    :param neigh:
        type of searched neighbourhood:
            1 - swaps of 2 points
            2 - reversing order of points between 2 points
            3 - multiswaping a few points by center point
    :param init_swap:
        bool, if true, swaps loaded from file solution
    :param start_T:
        float, start temperature
    :param red_T:
        float, number to reduce T every outside loop
    :param geom:
        bool, if true, temperature reduction is given as: t = t / (1 + red_T * t)
        if false emperature reduction is given as: t = t * red_T
    :param inside_iter:
        int, number of inside iterations
    :param no_change_number:
        int, after how many iterations without change of result should the loop break
    :param file_to_read:
        string, directory to read from
    :param file_to_save:
        string, directory to save to
    :return:
        Saves matrix calculated by SA algorithm
    """
    file_to_save = file_to_read.replace(".csv", "_startT_") + str(start_T) + "_red_" + str(red_T) \
                   + "_geom_" + str(geom) + "_iter_" + str(inside_iter) + "_nochange_" + str(
        no_change_number) + "_neigh_" + str(neigh)
    m = np.genfromtxt(file_to_read, delimiter=',')
    solution = np.arange(1, len(m))
    np.random.shuffle(solution)
    t = start_T
    distances = []
    if geom:
        stop = 0.01
    else:
        stop = 0.00001
    while t > stop:
        start = time.time()
        distances.append(c.sequence(solution, m))
        print("TEMPERATURE", t, c.sequence(solution, m))
        no_change = 0
        for i in range(1, inside_iter):
            if neigh == 1:
                s2 = c.randomswap_m(solution)
            elif neigh == 2:
                s2 = c.randomswap_m2(solution)
            elif neigh == 3:
                s2 = c.randomswap_m3(solution)
            else:
                rnd = np.random.randint(1, 4)
                if rnd == 1:
                    s2 = c.randomswap_m(solution)
                elif rnd == 2:
                    s2 = c.randomswap_m2(solution)
                else:
                    s2 = c.randomswap_m3(solution)
            t1 = c.sequence(solution, m)
            t2 = c.sequence(s2, m)
            delta_time = t2 - t1
            if delta_time < 0:
                solution = s2
                no_change = 0
            elif np.random.random() < np.exp((-1) * delta_time / t):
                solution = s2
                no_change = 0
            else:
                no_change += 1
            if no_change > no_change_number:
                break
        print("time per outside iter :", time.time() - start)
        if geom:
            t = t / (1 + red_T * t)
        else:
            t = t * red_T
    file_to_save = file_to_save + "_wynik_" + str(int(c.sequence(solution, m))) + ".csv"
    np.savetxt(file_to_save, solution, delimiter=",")
    print("FINAL FOR ", t, "T START ", inside_iter, "INSIDE ITERATIONS ", red_T, "REDUCTION ", "SAVED TO ",
          file_to_save)
    return distances


def ts(s, inside_iter, file_to_read, file_to_save, allow_zeros=False):
    """
    :param allow_zeros:
        bool, if true, allows TS to make swaps that result in no change in overall time
    :param init_swap:
        bool, if true, swaps loaded from file solution
    :param headers:
        bool, if true, deletes headers
    :param s:
        int, how many iterations are swaps blocked
    :param inside_iter:
        int, how many swaps to make
    :param file_to_read:
        string, directory to read from
    :param file_to_save:
        string, directory to save to
    :return:
        Saves matrix calculated by TS algorithm
    """
    m = np.genfromtxt(file_to_read, delimiter=',')
    tabu_list = np.zeros((len(m), len(m)))
    solution = np.arange(1, len(m))
    np.random.shuffle(solution)
    best_solution = solution
    dist = []
    for i in range(1, inside_iter):
        start = time.time()
        print(i)
        tm = c.sequence(solution, m)
        dist.append(tm)
        print(tm)
        move = c.calculate_moves2(solution, tabu_list, allow_zeros, m)
        print(move)
        solution = c.swap(solution, move[0], move[1])
        tabu_list = c.update_tabu_list(tabu_list)
        tabu_list[move[0], move[1]] = s
        tm = c.sequence(best_solution, m)
        tm2 = c.sequence(solution, m)
        if tm - tm2 > 0:
            best_solution = solution
        print("time per inside iter :", time.time() - start)
    dist.append(c.sequence(solution, m))
    file_to_save = file_to_save.replace(".csv", "_wynik_") + str(c.sequence(best_solution, m)) + ".csv"
    np.savetxt(file_to_save, best_solution, delimiter=",")
    print(c.sequence(best_solution, m))
    print("FINAL FOR ", s, "BLOCKS ", inside_iter, "INSIDE ITERATIONS ", "SAVED TO ", file_to_save)
    return dist


def ihc(outside_iter, indide_iter, no_change_number, neigh, file_to_read):
    """
    :param init_swap:
        bool, if true, swaps loaded from file solution
    :param headers:
        bool, if true, deletes headers
    :param outside_iter:
        int, number of outside iter
    :param indide_iter:
        int, number of inside iter
    :param no_change_number:
        int, after how many iterations without change of result should the loop break
    :param file_to_read:
        string, directory to read from
    :param file_to_save:
        string, directory to save to
    :return:
         Saves matrix calculated by IHC algorithm
    """
    file_to_save = file_to_read.replace(".csv", "_outside_") + str(outside_iter) + "_inside_" + str(indide_iter) \
                   + "_nochange_" + str(no_change_number) + "_neigh_" + str(neigh)
    m = np.genfromtxt(file_to_read, delimiter=',')
    best_solution = np.arange(1, len(m))
    np.random.shuffle(best_solution)
    distances = []
    for j in range(0, outside_iter):
        start = time.time()
        distances.append(c.sequence(best_solution, m))
        print("OUTSIDE ITER:", j)
        solution = np.arange(1, len(m))
        np.random.shuffle(solution)
        no_change = 0
        for i in range(0, indide_iter):
            if neigh == 1:
                s2 = c.randomswap_m(solution)
            elif neigh == 2:
                s2 = c.randomswap_m2(solution)
            elif neigh == 3:
                s2 = c.randomswap_m3(solution)
            else:
                rnd = np.random.randint(1, 4)
                if rnd == 1:
                    s2 = c.randomswap_m(solution)
                elif rnd == 2:
                    s2 = c.randomswap_m2(solution)
                else:
                    s2 = c.randomswap_m3(solution)
            t1 = c.sequence(solution, m)
            t2 = c.sequence(s2, m)
            delta_time = t2 - t1
            if delta_time < 0:
                solution = s2
                no_change = 0
            else:
                no_change += 1
            if no_change > no_change_number:
                break
        tm = c.sequence(best_solution, m)
        tm2 = c.sequence(solution, m)
        if tm - tm2 > 0:
            best_solution = solution
        print(c.sequence(best_solution, m))
        print("time per outside iter :", time.time() - start)
    file_to_save = file_to_save + "_wynik_" + str(int(c.sequence(best_solution, m))) + ".csv"
    np.savetxt(file_to_save, best_solution, delimiter=",")
    print("FINAL FOR ", indide_iter, "INSIDE ITER ", outside_iter, "OUTSIDE ITER ", "WITH NO CHANGE ", no_change_number,
          "SAVED TO ", file_to_save)
    return distances


def ga(population_size, iterations, mutations, div1, div2, cross, select, file_to_read):
    file_to_save = file_to_read.replace(".csv",
                                        "") + f"_GA_pop_{population_size}_epoch_{iterations}_mutate_{mutations}_cross_{cross}_crosspoints_{div1}_{div2}"
    distance_matrix = np.genfromtxt(file_to_read, delimiter=',')
    population = c.initrandomswaps_m(distance_matrix, population_size)
    best = c.select_best_child(population, distance_matrix)
    print(best, c.sequence(best, distance_matrix))
    distances = []
    averages = []
    epoch = 1
    while epoch < iterations:
        if select == 0:
            parents = c.select_best_solutions2(population, population_size)
        else:
            parents = c.select_best_solutions(population, population_size, distance_matrix)

        children = c.produce_children1(parents, div1, div2, cross)
        population = c.mutate_children(children, mutations)
        pretender = c.select_best_child(population, distance_matrix)
        pr_time = c.sequence(pretender, distance_matrix)
        best_time = c.sequence(best, distance_matrix)
        if pr_time < best_time:
            best = pretender
        avg = 0
        for s in population:
            avg += c.sequence(s, distance_matrix)
        avg /= len(population)
        epoch += 1
        print(best_time, avg, epoch)
        distances.append(best_time)
        averages.append(avg)
    file_to_save = file_to_save + "_wynik_" + str(c.sequence(best, distance_matrix)) + ".csv"
    np.savetxt(file_to_save, best, delimiter=",")
    plt.plot(np.linspace(1, len(distances), len(distances)), distances, label="best distance")
    plt.plot(np.linspace(1, len(averages), len(averages)), averages, label="average")
    title = f"GA {iterations} EPOCH, {population_size} POPULATION, MUTATIONS {mutations}, CROSSING {cross}"
    plt.xlabel("Epoch")
    plt.ylabel("Distance")
    plt.title(title)
    plt.legend()
    plt.savefig(file_to_save.replace(".csv",".jpeg"))
    plt.clf()


def knn(start_city, file_to_read):
    distance_matrix = np.genfromtxt(file_to_read, delimiter=',')
    distance_matrix = np.delete(distance_matrix, 0, axis=0)
    distance_matrix = np.delete(distance_matrix, 0, axis=1)
    distance_matrix[distance_matrix == 0] = 99999
    print(distance_matrix)
    cities = []
    city = start_city
    cities.append(city)
    print(distance_matrix[0])
    while len(cities) < len(distance_matrix):
        nearest = c.calc_nearest(distance_matrix[city], cities)
        city = nearest
        cities.append(city)
        print(cities)
    print(len(cities))
    print(c.sequence(cities, np.genfromtxt(file_to_read, delimiter=',')))
    return cities
