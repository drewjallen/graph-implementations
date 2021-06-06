from collections import deque


class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> None:
        """
        Adds a new vertex to the graph if one
        with the same name doesn't already exist
        """
        if self.contains_vertex(v):
            return
        else:
            self.adj_list[v] = []

    def contains_vertex(self, v_name: str) -> bool:
        """
        Helper method to find if a vertex already exists
        or not in the graph
        """
        for i in self.adj_list:
            if i == v_name:
                return True
        return False

    def add_edge(self, u: str, v: str) -> None:
        """
        Adds edge to the graph between specified
        vertices. If the vertices don't already exist,
        they are created.
        """
        if (u == v):
            return
        else:
            # add_vertex handles the checks
            # for if the vertices already
            # exist and if they already do,
            # nothing happens. Else it adds them
            self.add_vertex(u)
            self.add_vertex(v)

            # check if the edge already exists
            if self.contains_edge(u, v):
                return

            # create the edge
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)

    def contains_edge(self, u: str, v: str) -> bool:
        """
        Helper method to check if an edge
        already exists between two vertices
        """
        if v in self.adj_list[u]:
            return True
        else:
            return False

    def remove_edge(self, v: str, u: str) -> None:
        """
        Removes the edge from the graph
        """
        # check if vertices and/or edge even exists
        if not self.contains_vertex(v) or not self.contains_vertex(u):
            return
        if not self.contains_edge(u, v):
            return

        # remove the edge
        self.adj_list[v].remove(u)
        self.adj_list[u].remove(v)

    def remove_vertex(self, v: str) -> None:
        """
        Remove vertex and all connected edges
        """

        # verify the vertex exists
        if not self.contains_vertex(v):
            return

        # obtain its list of connected vertices
        connections = self.adj_list[v].copy()

        # remove the vertex
        self.adj_list.pop(v)

        # go to each of the connected vertices and remove
        # the connection to the removed vertex
        for vertex in connections:
            self.adj_list[vertex].remove(v)

    def get_vertices(self) -> []:
        """
        Returns list of vertices in the graph
        """
        return [i for i in self.adj_list]

    def get_edges(self) -> []:
        """
        Return list of edges in the graph (any order)
        """
        graph_edges = []

        for vertex in self.adj_list:
            for connection in self.adj_list[vertex]:
                if (vertex, connection) not in graph_edges and (connection, vertex) not in graph_edges:
                    graph_edges.append((vertex, connection))

        return graph_edges

    def is_valid_path(self, path: []) -> bool:
        """
        Return true if provided path is valid, False otherwise
        """
        if not path:
            return True

        if len(path) == 1:
            return self.contains_vertex(path[0])

        i = 0
        j = 1
        while j < len(path):
            if path[j] not in self.adj_list[path[i]]:
                return False
            else:
                i += 1
                j += 1

        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        Returns a list of vertices visited during DFS search
        Vertices are picked in alphabetical order
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
                options = sorted(self.adj_list[current], reverse=True)
                for vertex in options:
                    stack.append(vertex)
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
                options = sorted(self.adj_list[current])
                for vertex in options:
                    queue.append(vertex)
        return traversed_vertices

        

    def count_connected_components(self):
        """
        Return number of connected componets in the graph
        """
      

    def has_cycle(self):
        """
        Return True if graph contains a cycle, False otherwise
        """
       

   


if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = UndirectedGraph()
    print(g)

    for v in 'ABCDE':
        g.add_vertex(v)
    print(g)

    g.add_vertex('A')
    print(g)

    for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
        g.add_edge(u, v)
    print(g)


    print("\nPDF - method remove_edge() / remove_vertex example 1")
    print("----------------------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    g.remove_vertex('DOES NOT EXIST')
    g.remove_edge('A', 'B')
    g.remove_edge('X', 'B')
    print(g)
    g.remove_vertex('D')
    print(g)


    print("\nPDF - method get_vertices() / get_edges() example 1")
    print("---------------------------------------------------")
    g = UndirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    test_cases = ['ABC', 'ADE', 'ECABDCBE', 'ACDECB', '', 'D', 'Z']
    for path in test_cases:
        print(list(path), g.is_valid_path(list(path)))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = 'ABCDEGH'
    for case in test_cases:
        print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    print('-----')
    for i in range(1, len(test_cases)):
        v1, v2 = test_cases[i], test_cases[-1 - i]
        print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')


    print("\nPDF - method count_connected_components() example 1")
    print("---------------------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print(g.count_connected_components(), end=' ')
    print()


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
        'add FG', 'remove GE')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print('{:<10}'.format(case), g.has_cycle())
