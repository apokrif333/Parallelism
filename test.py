from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool

import numpy as np
import multiprocessing
import time


def writer(filename, n):
    start = time.time()
    print("Let's run: ", time.time())
    with open(filename, 'w') as file:
        for i in range(n):
            file.write('1')

        print("Finish: ", time.time() - start)


def mega_array(length: int, name: str):
    start = time.time()
    print("Let's run: ", time.time())

    temp_list = []
    for i in range(length):
        temp_list.append(i)

    print(len(temp_list))
    print("Finish: ", time.time() - start)

    return temp_list


def f(x, y):
    return x*y


if __name__ == '__main__':
    cores = 6

    # multiprocessing.Process
    # writer('test.txt', 5_000_000 * cores)

    # for i in range(cores):
    #     t = multiprocessing.Process(target=writer, args=(f'test{i}.txt', 5_000_000))
    #     t.start()
    #
    # print("All Threads are queued, let's see when they finish!")

    # multiprocessing.Pool
    # print(len(mega_array(5_000_000 * cores)))
    # input()
    #
    # p = multiprocessing.Pool(cores)
    # return_to_list = p.map(mega_array, [5_000_000] * cores)
    #
    # print(len(list(np.concatenate(return_to_list))))

    values = [5_000_000] * cores
    names = ['names'] * cores
    p = multiprocessing.Pool(cores)
    array = p.starmap(mega_array, zip(values, names))

    print(len(array))
    print('я уже тут')

