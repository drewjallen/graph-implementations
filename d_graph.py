from collections import deque

class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        Adds a vertex to the graph
        and updates the other vertices
        to account for the new addition
        """
        self.v_count += 1
        self.adj_matrix.append([])
        new_length = len(self.adj_matrix)
        new_row = self.adj_matrix[new_length - 1]

        i = 0
        while i < new_length - 1:
            self.adj_matrix[i].append(0)
            i += 1

        while len(new_row) < new_length:
            new_row.append(0)

        return self.v_count

    def contains_vertex(self, index):
        """
        Helper method to see if vertex exists in
        graph
        """
        if (index > self.v_count - 1) or (index < 0):
            return False
        else:
            return True

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        Adds directed edge from the source index
        to the destination index provided both
        indices exist in the graph
        """
        if not self.contains_vertex(src) or not self.contains_vertex(dst):
            return
        elif src == dst:
            return
        elif weight <= 0:
            return

        self.adj_matrix[src][dst] = weight

    def edge_exists(self, src: int, dst: int) -> bool:
        """
        Helper method to check if the edge exists
        or not
        """
        if (not self.contains_vertex(src)) or (not self.contains_vertex(dst)):
            return False
        else:
            return self.adj_matrix[src][dst] > 0

    def remove_edge(self, src: int, dst: int) -> None:
        """
        Removes an edge by setting its weight to 0
        """
        if not self.edge_exists(src, dst):
            return
        else:
            self.adj_matrix[src][dst] = 0

    def get_vertices(self) -> []:
        """
        Returns list of vertices
        """
        return [i for i in range(self.v_count)]

    def get_edges(self) -> []:
        """
        TODO: Write this implementation
        """
        edges = []
        for i in range(self.v_count):
            for j in range(self.v_count):
                if i != j and self.adj_matrix[i][j] != 0:
                    edges.append((i, j, self.adj_matrix[i][j]))
        return edges

    def is_valid_path(self, path: []) -> bool:
        """
        TODO: Write this implementation
        """
        if not path:
            return True

        queue = deque(path)

        while len(queue) > 1:
            current = queue.popleft()
            next_node = queue[0]
            if self.adj_matrix[current][next_node] <= 0:
                return False
        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        Returns a list of vertices visited during DFS search
        Vertices are picked in ascending index order
        """
        if not self.contains_vertex(v_start):
            return []
        if v_end is not None:
            if not self.contains_vertex(v_end):
                v_end = None

        traversed_vertices = []
        stack = [v_start]

        while len(stack) != 0:
            current = stack.pop()
            if current not in traversed_vertices:
                traversed_vertices.append(current)
                if (v_end is not None) and (current == v_end):
                    return traversed_vertices
                options = self.adj_matrix[current]
                j = len(options) - 1
                while j >= 0:
                    if options[j] != 0:
                        stack.append(j)
                    j -= 1
        return traversed_vertices

    def bfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during BFS search
        Vertices are picked in alphabetical order
        """
        if not self.contains_vertex(v_start):
            return []
        if v_end is not None:
            if not self.contains_vertex(v_end):
                v_end = None

        traversed_vertices = []
        queue = deque([v_start])

        while len(queue) != 0:
            current = queue.popleft()
            if current not in traversed_vertices:
                traversed_vertices.append(current)
                if (v_end is not None) and (current == v_end):
                    return traversed_vertices
                options = self.adj_matrix[current]
                j = 0
                while j < len(options):
                    if options[j] != 0:
                        queue.append(j)
                    j += 1
        return traversed_vertices

    def has_cycle(self):
        """
        Return True if graph contains a cycle, False otherwise
        """

        for i in range(len(self.adj_matrix)):
            traversed = dict()
            for i in range(len(self.adj_matrix)):
                traversed[i] = False

            if not traversed[i]:
                if self.has_cycle_helper(i, traversed, -1):
                    return True
        return False

    def has_cycle_helper(self, vertex, traversed, parent):

        traversed[vertex] = True

        for i in range(len(self.adj_matrix[vertex])):
            if self.adj_matrix[vertex][i] != 0:
                if not traversed[i]:
                    if self.has_cycle_helper(i, traversed, vertex):
                        return True
                else:
                    return True
        return False

    def dijkstra(self, src: int) -> []:
        """
        TODO: Write this implementation
        """
        pass


if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = DirectedGraph()
    print(g)
    for _ in range(5):
        g.add_vertex()
    print(g)

    edges = [(0, 6, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    for src, dst, weight in edges:
        g.add_edge(src, dst, weight)
    print(g)


    print("\nPDF - method get_edges() example 1")
    print("----------------------------------")
    g = DirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    for path in test_cases:
        print(path, g.is_valid_path(path))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for start in range(5):
        print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)

    edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    for src, dst in edges_to_remove:
        g.remove_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')

    edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    for src, dst in edges_to_add:
        g.add_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')
    print('\n', g)


    print("\nPDF - dijkstra() example 1")
    print("--------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    g.remove_edge(4, 3)
    print('\n', g)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
