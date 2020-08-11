"""
Simple graph implementation
"""
class Q:
    def __init__(self): 
        self.items = []
    
    def __str__(self): 
        return ', '.join([str(x) for x in self.items])
    
    def __len__(self): 
        return len(self.items)
    
    def first(self): 
        return self.items[0]
    
    def add(self, i): 
        self.items.append(i)
    
    def pop(self):
        return self.items.pop(0)
    
    def isEmpty(self): 
        return True if len(self.items) == 0 else False

class Stack:
    def __init__(self): 
        self.items = []
    
    def __str__(self): 
        return ', '.join([str(x) for x in self.items])
    
    def __len__(self): 
        return len(self.items)
    
    def next(self): 
        return self.items[-1]
    
    def add(self, i): 
        self.items.append(i)
    
    def pop(self): 
        return self.items.pop()


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices: self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices: self.vertices[v1].add(v2)
        else: raise IndexError("Nonexistant Vert.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        
        """
            Plan:
            - Start at given index. Add that index to the Q.
            - While len(Q) is greater than 0:
            -   Check if q[0] has children.
            -       If so then make sure children have not been visited, then add those children to the Q.
            -       If they have been visited, skip over the child and DO NOT add to Q # !! will result in infinite loop !!
        """

        queue = Q()
        visited = []

        queue.add(starting_vertex)

        while len(queue):
            current = queue.first()
            children = self.vertices[current]
            
            if len(children) > 0:
                for child in children:
                    if child not in visited:
                        queue.add(child)
                    else: continue

            print(current)
            visited.append(current)
            queue.pop()

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        
        visited = []
        stack = Stack()

        stack.add(starting_vertex)

        while len(stack):
            current = stack.pop()

            if current not in visited:
                print(current)
                visited.append(current)
            
            for child in self.vertices[current]:
                if child not in visited:
                    stack.add(child)


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        
        visited = []

        def helper(vert, visited):
            visited.append(vert)
            print(vert)

            for child in self.vertices[vert]:
                if child not in visited:
                    helper(child, visited)

        helper(starting_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        
        def populate_parents():
            parents = {
                # '1': [],
                # '2': [],
                # '3': [],
            }

            for index, (k, v) in enumerate(self.vertices.items()):
                parents[k] = []

            queue = Q()
            visited = []

            queue.add(starting_vertex)
            visited.append(starting_vertex)
            
            while len(queue):
                node = queue.pop()

                for child in self.vertices[node]:
                    if child not in visited:
                        queue.add(child)
                        visited.append(child)
                        parents[child].append(node)

            return parents

        parents = populate_parents()
        path = []
        current = destination_vertex
        path.append(destination_vertex)

        while len(parents[current]):
            parent = parents[current][0]
            path.append(parent)
            current = parent

        path.reverse()

        return path

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        parents = {}

        for index, (p, c) in enumerate(self.vertices.items()):
            for child in c:
                if child not in parents:
                    parents[child] = []
                parents[child].append(p)

        path = []
        current = destination_vertex
        path.append(destination_vertex)

        while len(parents[current]):
            parent = parents[current][0]
            path.append(parent)
            if parent == starting_vertex:
                break
            current = parent

        path.reverse()
        return path

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

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
    # print(graph.vertices)

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
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
