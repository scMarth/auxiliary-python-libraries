# This example demonstrates how to define a job that takes multiple arguments

import sys
sys.path.insert(0, '../../')
import best_effort_multiprocessing_pool
import os, multiprocessing

def job(arg):
    input_number = arg[0]
    translate_table = arg[1]
    return translate_table[input_number]


if __name__ == '__main__':
    some_map = { \
        1 : 'one', \
        2 : 'two', \
        3 : 'three', \
        4 : 'four' \
    }

    be_pool = best_effort_multiprocessing_pool.BestEffortPool(100)

    some_list = [1, 2, 3, 4, 1, 2, 3, 4, 3, 2, 1]

    job_args = []

    for i in some_list:
        job_args.append([i, some_map])

    print("Starting processes...")
    multiprocessing_results = be_pool.run(job, job_args)
    print("Processes finished...")

    for result in multiprocessing_results:
        print(result)