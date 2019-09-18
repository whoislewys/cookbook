# from a given given graph 
from collections import defaultdict 
  

class Graph:   
    # A directed graph using adjacency list representation 
    def __init__(self):   
        # default dictionary to store graph 
        self.graph = defaultdict(list) 

  
    def addEdge(self, u, v): 
        # function to add an edge to graph 
        self.graph[u].append(v) 
  

    def DFSUtil(self, v, visited): 
        # Mark current node as visited
        visited[v] = True
        print(v)

        # iterate through nodes adjacent to current node
        for adj in self.graph[v]:
            if visited[adj] is False:
                self.DFSUtil(adj, visited)
        

    def DFS(self, v): 
        '''
        Parameters:
        v: the vertex (node) to start the DFS from
        The basic idea in graph DFS is to keep a list of which nodes you have visited,
        because unlike in a tree, a graph can have cycles.
        Use a visited array to avoid infinite loops
        '''  
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph)) 
  
        # Call the recursive helper function  
        # to print DFS traversal 
        self.DFSUtil(v, visited) 
  
# Driver code 
  
# Create a graph given  
# in the above diagram 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print("Following is DFS from (starting from vertex 2)") 
g.DFS(2)  