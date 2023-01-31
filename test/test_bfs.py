# write tests for bfs
import pytest
from search import graph
import networkx as nx

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    # Use nx.bfs_tree to ensure my bfs function has correct output when navigating tiny_network.
    tiny_network = nx.read_adjlist("./data/tiny_network.adjlist", create_using=nx.DiGraph, delimiter=";")
    assert graph.Graph(tiny_network).bfs(start = 'Charles Chiu') == list(nx.bfs_tree(tiny_network, 'Charles Chiu'))

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    # Assert length of the shortest path connecting any two nodes returned from my bfs function is correct.
    citation_file = './data/citation_network.adjlist'
    citation_network = nx.read_adjlist(citation_file, create_using=nx.DiGraph, delimiter=";")
    assert len(nx.shortest_path(citation_network, 'Lani Wu', 'Nevan Krogan')) == len(graph.Graph(citation_file).bfs('Lani Wu', 'Nevan Krogan'))

    # Assert None for no connection between nodes.
    assert graph.Graph(citation_file).bfs('Luke Gilbert', '34858697') == None

def test_edge_cases_bfs():
    """
    Tests for start node not in the graph and end
    node not in the graph. Raises exception for failed
    test cases.
    """
    citation_file = './data/citation_network.adjlist'
    with pytest.raises(Exception):
        graph.Graph(citation_file).bfs('Ronald McDonald') # Start node not found in graph.
        graph.Graph(citation_file).bfs('Lani Wu', 'Ronald McDonald') # End node not found in graph.
