import sys
from collections import deque

n, m = map(int, input().split(" "))

count = 0
time = sys.maxsize

queue = deque()
queue.append()

def solution(q, times):
    a = q.popleft()
    if a == n:
