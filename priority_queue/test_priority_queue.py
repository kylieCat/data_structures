from random import randint
from time import sleep
import pytest
from priority_queue import Job, PriorityQueue

@pytest.fixture(scope='function')
def make_jobs():
    return [Job(priority=(i)) for i in [3,3,4,9,7,7,9,9,7,8]]
    
@pytest.fixture(scope='function')
def new_pq():
    pq = PriorityQueue()
    for index,value in enumerate([3,3,4,9,7,7,9,9,7,8]):
        pq.insert(Job(priority=value))
        if not index % 3:
            pq._iterations = 0
    pq._iterations = 0
    return pq

def test_job():
    j = Job()
    assert j.value == 'Print job'
    assert j.priority == 1
    h = Job('Math operation', 5)
    assert h.value == 'Math operation'
    assert h.priority == 5
    i = Job(priority=5)
    assert i.value == 'Print job'
    assert i.priority == 5
    
def test_priority_queue(make_jobs):
    pq = PriorityQueue()
    assert pq.jobs == []
    assert pq._iterations == 0
    pq = PriorityQueue(make_jobs)
    temp = [p.priority for p in pq.jobs]
    assert temp == [9,9,9,7,8,3,7,3,7,4]
    
def test_insert(new_pq):
    pq = new_pq
    assert [job.priority for job in pq.jobs] == [9,9,9,7,8,3,7,3,7,4]
    
def test_empty_pop():
    pq = PriorityQueue()
    with pytest.raises(IndexError):
        pq.pop()
    
def test_pop(new_pq):
    pq = new_pq
    assert pq._iterations == 0
    assert pq.pop().priority == 9
    assert pq._iterations == 1
    assert pq.pop().priority == 9
    assert pq._iterations == 2
    
    
def test_assign_priority(new_pq):
    pq = new_pq
    priorities = [job.priority for job in pq.jobs]
    print(priorities)
    for job in pq.jobs:
        job.time_created -= 100
    pq._adjust_priority()
    assert [job.priority for job in pq.jobs] == [p+5 for p in priorities]
 
def test_assign_priority_via_insert():   
    new_pq = PriorityQueue()
    for _ in range(4):
        new_pq.insert(Job(priority=1))
    new_pq.jobs[3].time_created -= 100
    new_pq.insert(Job(priority=1))
    assert [job.priority for job in new_pq.jobs] == [6, 1, 1, 1, 1]
    new_pq.jobs[3].time_created -= 100
    new_pq._iterations = 4
    new_pq.insert(Job(priority=1))
    assert [job.priority for job in new_pq.jobs] == [11, 6, 1, 1, 1, 1]
    
def test_assign_priority_via_pop():
    new_pq = PriorityQueue()
    for _ in range(4):
        new_pq.insert(Job(priority=1))
    new_pq.jobs[3].time_created -= 100
    new_pq.pop()
    assert [job.priority for job in new_pq.jobs] == [6, 1, 1]
    new_pq.jobs[2].time_created -= 100
    new_pq._iterations = 4
    new_pq.pop()
    assert [job.priority for job in new_pq.jobs] == [6, 1]

def test_assign_priority_via_insert():
    new_pq = PriorityQueue()
    for i in range(5):
        new_pq.insert(Job(priority= i+1))
    new_pq.jobs[-1].time_created -= 100
    new_pq.insert(Job(priority=6))
    assert [job.priority for job in new_pq.jobs] == [8,5,6,1,4,2]

def test_assign_priority_via_pop():
    new_pq = PriorityQueue()
    for i in range(5):
        new_pq.insert(Job(priority= i+1))
    new_pq.jobs[-1].time_created -= 100
    new_pq.insert(Job(priority=6))
    new_pq.pop()
    assert [job.priority for job in new_pq.jobs] == [6,5,1,4,2]

    
    
    
    
    
    
    
    
    