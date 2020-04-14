"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):

        self.vertices = {}

    def add_vertex(self, vertex_id):

        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):

        if v1 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):

        if vertex_id in self.vertices:
            return self.vertices[vertex_id]

    def bft(self, starting_vertex):

        cur = starting_vertex
        visited = set()

        tQueue = Queue()
        tQueue.enqueue(cur)

        while tQueue.size():
            cur = tQueue.dequeue()
            visited.add(cur)
            print(cur)

            for n in self.vertices[cur]:
                if n not in visited:
                    tQueue.enqueue(n)
                    visited.add(cur)

    def dft(self, starting_vertex):

        cur = starting_vertex
        visited = set()

        tStack = Stack()
        tStack.push(cur)

        while tStack.size():
            cur = tStack.pop()
            visited.add(cur)
            print(cur)

            for n in self.vertices[cur]:
                if n not in visited:
                    tStack.push(n)
                    visited.add(n)

    def dft_recursive(self, starting_vertex, visited=None):

        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)

        for n in self.vertices[starting_vertex]:
            if n not in visited:
                self.dft_recursive(n, visited)

    def bfs(self, starting_vertex, destination_vertex):
        cur = starting_vertex
        path = []
        sQueue = Queue()
        visited = set()
        sQueue.enqueue([cur])
        visited.add(cur)
        while sQueue.size():
            path = sQueue.dequeue()
            cur = path[-1]
            visited.add(cur)
            if cur == destination_vertex:
                return path
            for n in self.vertices[cur]:
                if n not in visited:
                    newPath = list(path)
                    newPath.append(n)
                    sQueue.enqueue(newPath)

    def dfs(self, starting_vertex, destination_vertex):

        visited = set()
        sStack = Stack()
        cur = starting_vertex
        sStack.push([cur])
        visited.add(cur)
        while sStack.size():
            path = sStack.pop()
            cur = path[-1]
            if cur == destination_vertex:
                return path

            for n in self.vertices[cur]:
                if n not in visited:
                    newPath = list(path)
                    newPath.append(n)
                    sStack.push(newPath)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):

        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(starting_vertex)
        new_path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return new_path

        for n in self.vertices[starting_vertex]:
            if n not in visited:
                neighbor_path = self.dfs_recursive(
                    n, destination_vertex, visited, new_path)
                if neighbor_path:
                    return neighbor_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
