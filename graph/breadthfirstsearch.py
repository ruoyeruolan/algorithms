# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : breadthfirstsearch.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/01/26 23:07
@Description: 
"""

from typing import List
from collections import deque

class BreadthFirstSearch:
    
    def __init__(self, graph: dict, start: int = None):
        super().__init__()
        self.graph = graph
        self.start = start
    
    def bfs(self):
        visited = set()
        queue = deque(self.graph.keys())
        while queue:
            node = queue.popleft()
            if node not in visited:
                unvisited = self.graph[node] - visited
                queue.extend(unvisited)
                visited.update(unvisited)
        return visited