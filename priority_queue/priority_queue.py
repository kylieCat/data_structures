from time import time

class Job(object):
    def __init__(self, value='Print job', priority=1):
        self.value = value
        self.priority = priority
        self.time_created = int(time())

class PriorityQueue(object):
    def __init__(self, jobs=None):
        self._iterations = 0
        if jobs:
            self.jobs = jobs
            self._sort()
        else:
            self.jobs = []
    
    def _switch(self, p_index, c_index):
        self.jobs[p_index], self.jobs[c_index] = self.jobs[c_index], self.jobs[p_index]
        
    def _adjust_priority(self):
        current_time  = int(time())
        for job in self.jobs:
            if current_time - job.time_created > 10:
                job.priority += 5
        
    def _sort(self):
        for index, element in enumerate(self.jobs):
           # import pdb; pdb.set_trace()
            if self._iterations > 5:
                self._adjust_priority()
                self._iterations = 0
            p_index = (index - 1) >> 1 if (index - 1) >> 1 > 0  else 0
            if element.priority > self.jobs[p_index].priority:
                self._switch(p_index, index)
                self._sort()

    def pop(self):
        if self.jobs:
            job = self.jobs.pop(0)
            self._iterations += 1
            self._sort()
            return job
        else:
            raise IndexError
            
    
    def insert(self, item):
        self.jobs.append(item)
        #import pdb; pdb.set_trace()
        self._iterations += 1
        self._sort()
        
    def peek(self):
        return self.jobs[0]