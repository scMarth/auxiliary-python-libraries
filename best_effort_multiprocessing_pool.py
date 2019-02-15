# doesn't really work because of the need for if __name__ == '__main__':

import multiprocessing

class BestEffortPool(object):
    __processes = []
    __input_index = 0
    __q = multiprocessing.Queue()
    __MAX_GROUP_SIZE = 100
    
    def __join_and_terminate_processes(self, pid):
        dead_processes = [p for p in self.__processes if p.pid == pid][0]
        dead_processes.join()
        dead_processes.terminate()

    def __init__(self, num_processes):
        self.__MAX_GROUP_SIZE = num_processes

    '''
    It seems like this function can't be private for Python 3.6.5 or below
    (or 2.7.10 or below).. but a private function, i.e. def __job_function
    will work in 3.7.2 or 2.7.15

    Either that or this is Windows specific...?
    '''
    def job_function(self, target_function, input_index, input_arg, q):
        result = target_function(input_arg)
        q.put([input_index, result, multiprocessing.current_process().pid])


    '''
    Runs the pool of processes

    target_function - the target function to run

    '''
    def run(self, target_function, input_set):
        if __name__ == 'best_effort_multiprocessing_pool':

            results = []

            self.__input_index = 0

            while self.__input_index < len(input_set) or len([p for p in self.__processes if p.is_alive()]) > 0 or not self.__q.empty():
                
                # start a new process unless the maximum pool size has been reached or if there are no more inputs
                if len(multiprocessing.active_children()) < self.__MAX_GROUP_SIZE and self.__input_index < len(input_set):
                    curr_input = input_set[self.__input_index]
                    p = multiprocessing.Process(target=self.job_function, args=(target_function, self.__input_index, curr_input, self.__q)) # see note above job_function
                    self.__input_index += 1
                    self.__processes.append(p)
                    p.start()

                # empty the queue and join processes that have finished
                while not self.__q.empty():
                    input_index, result, pid = self.__q.get()
                    self.__join_and_terminate_processes(pid)
                    results.append([input_index, result])
            return results