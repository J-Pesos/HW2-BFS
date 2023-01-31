![BuildStatus](https://github.com/J-Pesos/HW2-BFS/workflows/test.yml/badge.svg?event=push)

# Assignment 2
Breadth-first search

# Assignment Overview
The purpose of this assignment is to get you comfortable working with graph structures and to implement a breadth-first search function to traverse the graph and find the shortest path between nodes.

# Description of Method
## Breadth-First Search
A breadth-first search (BFS) is a search algorithm that traverses a graph of connected nodes layer-by-layer. A source node is placed in a queue and the algorithm identifies, then subsequently places, outgoing neighbors into the queue. The source node is simulatenously removed from the queue after all neighbors have been identified and placed into the queue. The process repeats itself by selecting the first node in the queue as a new source. As children nodes will always be visited after the other nodes in the same layer as the source node, BFS will find the shortest path between any two nodes in a graph.

This project creastes a Graph class containing the bfs() function. Networkx is used to import a graph object and matplotlib was used to visualize sample networks in a test file. The bfs() function takes in a networkx graph, a start node, and an optional end node as inputs. The bfs() funciton also ensures that the input graph is not empty and then runs a series of checks to ensure input nodes are both present and connected.

The output of bfs() provides the following:
1) If an end node is present, the function returns a list of nodes traversed in order of the start to end node.
2) If the start node is the end node, the function returns that node.
3) If no end node is input, the function returns a list of all traversed nodes starting from the start node.

# Reference Information
## Test Data
Two networks have been provided in an adjacency list format readable by [networkx](https://networkx.org/), is a commonly used python package for working with graph structures. These networks consist of two types of nodes:
* Faculty nodes 
* Pubmed ID nodes

However, since these are both stored as strings, you can treat them as equivalent nodes when traversing the graph. The first graph ("citation_network.adjlist") has nodes consisting of all BMI faculty members, the top 100 Pubmed papers *cited by* faculty, and the top 100 papers that *cite* faculty publications. Edges are directed and and edge from node A -> B indicates that node A *is cited by* node B. There are 5120 nodes and 9247 edges in this network.

The second network is a subgraph of the first, consisting of only the nodes and edges along the paths between a small subset of faculty. There are 30 nodes and 64 edges.

# Completing the assignment
Make sure to push all your code to github, ensure that your unit tests are correct, and submit a link to your github through the google classroom assignment.

# Grading

## Code (6 points)
* Breadth-first traversal works correctly (3)
* Traces the path from one faculty to another (2)
* Handles edge cases (1)

## Unit tests (3 points)
* Output traversal for mini data set (1)
* Tests for at least two possible edge cases (1)
* Correctly uses exceptions (1)

## Style (1 points)
* Readable code with clear comments and method descriptions
* Updated README with description of your methods

