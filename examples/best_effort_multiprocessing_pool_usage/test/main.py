import sys
import best_effort_multiprocessing_pool
import os, multiprocessing

def job(input_number):
    if input_number in [3, 5, 16]: # randomly kill some processes
        os.kill(multiprocessing.current_process().pid, 9)
    return str(input_number) + " hey"

if __name__ == '__main__':

    be_pool = best_effort_multiprocessing_pool.BestEffortPool(100)

    print("Starting processes...")
    multiprocessing_results = be_pool.run(job, range(0,20))
    print("Processes finished...")

    for result in multiprocessing_results:
        print(result)