"""
Simple graph implementation
"""
from queue import Queue
from queue import LifoQueue

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = { }
    
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
        

    def add_directed_edge(self, v1, v2):
        if v2 in self.vertices and v1 in self.vertices:
            self.vertices[v1].add(v2)
            # self.vertices[v2].add(v1)
        else:
            raise IndexError("Vertex doesn't exist")

    def bft(self, start_vert):

        q = Queue()

        q.put(start_vert)
        
        visited = set()

        while q.qsize() > 0:
            v = q.get()
            if v not in visited:
                visited.add(v)
                for next_vert in self.vertices[v]:
                    q.put(next_vert)

        print(visited, 'bft')

    def dft(self, first_vert):

        q = LifoQueue()

        q.put(first_vert)

        visited = set()

        while q.qsize() > 0:
            v = q.get()
            if v not in visited:
                visited.add(v)
                for next_vert in self.vertices[v]:
                    q.put(next_vert)

        print(visited,'dft')
    
    # using recursion
        # q = LifoQueue()
        # q.put(first_vert)
        # visited= set()

        # for child_vert in self.vertices[first_vert]:
        #     if child_vert is not in visited:
        #         new_vert = self.dft(child_vert)
        
        # return visited

    def bfs(self, start_vert, end_vert):

        q = Queue()

        q.put([start_vert])
        
        visited = set()

        while q.qsize() > 0:
            path = q.get()
            v = path[-1]
            if v not in visited:
                visited.add(v)
                if v == end_vert:
                    print(path)
                    return
                for next_vert in self.vertices[v]:
                    new_path= path[:]
                    new_path.append(next_vert)
                    q.put(new_path)

        return []

    def dfs(self, start_vert, end_vert):

        q = LifoQueue()

        q.put([start_vert])

        
        visited = set()

        while q.qsize() > 0:
            path = q.get()
            v = path[-1]
            if v not in visited:
                visited.add(v)
                if v == end_vert:
                    print(path)
                    return
                for next_vert in self.vertices[v]:
                    new_path = path[:]
                    new_path.append(next_vert)
                    q.put(new_path)

        print(visited)
    


        


# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# graph.add_edge('2', '1')
# graph.add_edge('2', '0')
# graph.add_edge('2', '3')
# # print(graph.vertices)
# # Continuing from previous example
# # graph.add_edge('0', '4')  # No '4' vertex, should raise an Exception!
# graph.bft('0')
# graph.dft('0')
# graph.bfs('0', '2')
# graph.dfs('0', '2')