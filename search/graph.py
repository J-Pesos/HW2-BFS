import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end n does not exist, return None
ode input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path
        """
        # Handling some edge cases.
        # Ensure graph has nodes.
        if len(self.graph.nodes()) == 0:
            raise ValueError("Graph has no nodes!")
        
        # Don't run BFS if start node is end node.
        if start == end:
            return [start]

        # Ensure start node is in the graph.
        if start not in self.graph.nodes():
            raise ValueError("The start node is not in the graph.")

        # Ensure end node is in the graph.
        if end and end not in self.graph.nodes():
            raise ValueError("There is no end node in the graph.")

        # Ensure graph is connected, evaluated depending on whether directed or undirected.
        if nx.is_directed(self):
            if nx.is_weakly_connected(self) == False:
                raise ValueError("The graph is directed, but not connected.")
        else:
            if nx.is_connected(self) == False:
                raise ValueError("The graph is undirected, but not connected.")
        
        visited = [start] # List of visited nodes. Intialized with start node.
        q = [start] # List of nodes that are queued. Initialized with start node.
        child_parent = {start:None} # Tracks parent and child nodes using a dictionary.

        while q: # While there are still nodes in the queue.
            curr_node = q.pop(0)
            
            for neighbor in self.graph.neighbors(curr_node): # Get all neighbors of current node.
                if neighbor not in visited: # If neighbor not in visited, visit it and it to queue.
                    visited.append(neighbor)
                    q.append(neighbor)
                    child_parent[neighbor] = curr_node
        
        if end == None: # Returns nodes that were visited if end node was not given.
            return(visited)

        elif end in child_parent: # If end node exists, return a list of the shortest path.
            shortest_path = [end] # Start list with end node.
            node = end # Prepare node to work backwards from.
            while child_parent[node]: # While there are still nodes in the path.
                shortest_path.append(child_parent[node]) # Add parent node to path.
                node = child_parent[node] 
            return shortest_path[::-1] # Return the shortest path reversed, as it was created backwards.
        
        else: # If end node exists, but there is no path between start and end.
            return None