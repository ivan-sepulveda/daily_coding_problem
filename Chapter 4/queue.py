from collections import deque

queue = deque()

queue.append(4)  # Traditionally called enqueue
queue.append(5)  # Traditionally called enqueue
queue.appendleft(6)

print(queue)

queue.popleft()  # 6  # Traditionally called dequeue
queue.pop()  # 5

print(queue)
