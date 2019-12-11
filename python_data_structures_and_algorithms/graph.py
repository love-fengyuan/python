# _*_ coding: utf-8 _*_

from collections import deque

GRAPH = {
    'A': ['B', 'F'],
    'B': ['C', 'I', 'G'],
    'C': ['B', 'I', 'D'],
    'D': ['C', 'I', 'G', 'H', 'E'],
    'E': ['D', 'H', 'F'],
    'F': ['A', 'G', 'E'],
    'G': ['B', 'F', 'H', 'D'],
    'H': ['G', 'D', 'E'],
    'I': ['B', 'C', 'D'],
}



class Queue(object):

    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)
    
    def pop(self):
        return self._deque.popleft()

    def __len__(self):
        return len(self._deque)

# 广度优先算法
def bfs(graph, start):
    search_queue = Queue()
    search_queue.push(start)
    searched = set()
    while search_queue:
        cur_node = search_queue.pop()
        if cur_node not in searched:
            print(cur_node)
            searched.add(cur_node)
            for node in graph[cur_node]:
                search_queue.push(node)

print('BFS:')
bfs(GRAPH, 'A')


# 深度优先算法
DFS_SEARCHED = set()

def dfs(graph, start):
    if start not in DFS_SEARCHED:
        print(start)
        DFS_SEARCHED.add(start)
    for node in graph[start]:
        if node not in DFS_SEARCHED:
            dfs(graph, node)

print('dfs:')
dfs(GRAPH, 'A')

# 使用递归，栈改写

class Stack(object):

    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)
    
    def pop(self):
        return self._deque.popleft()

    def __len__(self):
        return len(self._deque)


def dfs_use_stack(graph, start):
    stack = Stack()
    stack.push(start)
    searched = set()
    while stack:
        cur_node = stack.pop()
        if cur_node not in searched:
            print(cur_node)
            searched.add(cur_node)
            for node in reversed(graph[cur_node]):
                stack.push(node)


print('dfs_use_stack')
dfs_use_stack(GRAPH, 'A')



# BFS(breadth first search) 广度优先搜索
# DFS(depdth first search) 深度优先搜索