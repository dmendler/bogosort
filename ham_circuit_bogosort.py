#!/usr/bin/env python3

from collections import defaultdict
from time import time
import csv
import sys

# Type Alias
Graph = dict[int, set[int]]

def read_graph(stream=sys.stdin) -> Graph:
    ''' Read in a graph from a CSV format input stream. '''
    graph = defaultdict(set)
    vertices = set()
    
    for line in stream:
        line = line.strip()
        if not line or line.startswith('c'):
            # Ignore comments
            continue
        parts = line.split(',')
        parts = [p.strip() for p in parts]
        
        if parts[0] == 'p':
            # Problem line, ignore for now (contains meta info)
            problem_type = parts[1]
            num_vertices = int(parts[2])
            num_edges = int(parts[3])
            # Optionally, you could validate the graph size here if necessary
        elif parts[0] == 'v':
            # Vertex line, add the vertex
            vertex = int(parts[1])
            vertices.add(vertex)
        elif parts[0] == 'e':
            # Edge line, add the edge to the graph
            u = int(parts[1])
            v = int(parts[2])
            graph[u].add(v)
            graph[v].add(u)

    # Ensure the graph contains all vertices, even if they have no edges
    for vertex in vertices:
        if vertex not in graph:
            graph[vertex] = set()

    return graph

def find_circuit(graph: Graph, path: list[int], visited: set[int]) -> list[int]:
    ''' Find a Hamiltonian Cycle using DFS. '''
    if len(path) == len(graph) and path[0] in graph[path[-1]]:
        return path + [path[0]]
    
    for neighbor in graph[path[-1]]:
        if neighbor in visited:
            continue
        
        visited.add(neighbor)
        path.append(neighbor)
        if result := find_circuit(graph, path, visited):
            return result
        path.pop()
        visited.remove(neighbor)
    
    return []

def find_circuit(graph: Graph, path: list[int], visited: set[int]) -> list[int]:
    ''' Find a Hamiltonian Cycle using DFS. '''
    if len(path) == len(graph) and path[0] in graph[path[-1]]:
        return path + [path[0]]
    
    for neighbor in graph[path[-1]]:
        if neighbor in visited:
            continue
        
        visited.add(neighbor)
        path.append(neighbor)
        if result := find_circuit(graph, path, visited):
            return result
        path.pop()
        visited.remove(neighbor)
    
    return []

def main() -> None:
    '''  Time reading graph, call functions to find ciruit, and print results. '''
    start_t = time()
    graph = read_graph()
    read_t = time() - start_t

    start_t = time()
    circuit = find_circuit(graph, [1], set([1]))
    search_t = time() - start_t
    
    if circuit:
        print('Hamiltonian Circuit:', ' -> '.join(map(str, circuit)))
    else:
        print("No Hamiltonian Circuit found.")

    print(f"Time to read graph: {read_t:0.6f}s")
    print(f"Time to find path: {search_t:0.6}s")

if __name__ == '__main__':
    main()
