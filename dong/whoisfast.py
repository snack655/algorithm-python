import time

def list_pop():
    n = int(input())
    lst = [10000000] * n

    s = time.time()
    print(f'시작 : {s}')
    lst.pop(0)
    e = time.time()

    print(f'끝 : {e}')

    interval = e - s
    print(str(n) + ':' + str(interval))

from queue import Queue

def queue_pop():
    n = int(input())
    q = Queue()
    for i in range(n):
        q.put(i) # q.put(i, 1)
    
    s = time.time
    print(f'시작 : {s}')
    while not q.empty():
        q.get()
    e = time.time()
    print(f'끝 : {e}')
    interval = e - s
    print(str[n] + ":" + str(interval))

from collections import deque

def deque_pop():
    n = int(input())
    dq = deque([1] * n)

    s = time.time()
    print(f'시작 : {s}')
    while dq: # 'collections.deque' object has no attribute 'empty'
        dq.popleft()
    e = time.time()
    print(f'끝 : {e}')

    interval = e - s
    print(str(n) + ':' + str(interval))

list_pop()
queue_pop()
deque_pop()