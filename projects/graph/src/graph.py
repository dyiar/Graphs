"""
Simple graph implementation
"""
from queue import Queue

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = { }
    
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
        

    def add_edge(self, v1, v2):
        if v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
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

        print(visited)


        


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('2', '1')
graph.add_edge('2', '0')
graph.add_edge('2', '3')
# print(graph.vertices)
# Continuing from previous example
# graph.add_edge('0', '4')  # No '4' vertex, should raise an Exception!
graph.bft('0')