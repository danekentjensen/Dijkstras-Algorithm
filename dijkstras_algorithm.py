# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:04:45 2024

@author: Dane Jensen
"""
## Program uses Dijkstra's Algorithm to traverse weighted nodes in a graph to find the least expensive path between two nodes.  
## In this program I used Romanian cities as nodes and the edges are the distances between any two connecting cities.  
import sys
 
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        return self.nodes
    
    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):

        return self.graph[node1][node2]
    
    
	
def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())  
    shortest_path = {}
    previous_nodes = {}
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
   
    shortest_path[start_node] = 0
    
    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes: 
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node
 
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    path.append(start_node)
    
    print("The shortest path had a value of:", shortest_path[target_node])
    print("Path Taken:"," -> ".join(reversed(path)))

## Cities are input into the graph and any connecting cities are created as edges with a "weight" or distance between them.
cities = ['Arad','Zerind','Oradea','Sibiu','Fagaras','Bucharest','Timisoara','Lugoj','Mehadia','Drobeta','Craiova','Rimnicu Vilcea','Pitesti','Giurgiu','Urziceni','Hirsova','Eforie','Vaslui','Iasi','Neamt']
edges = {}
for city in cities:
    edges[city] = {}
    
edges['Arad']['Zerind'] = 75
edges['Arad']['Sibiu'] = 140
edges['Arad']['Timisoara'] = 118
edges['Timisoara']['Lugoj'] = 111
edges['Lugoj']['Mehadia'] = 70
edges['Mehadia']['Drobeta'] = 75
edges['Drobeta']['Craiova'] = 120
edges['Craiova']['Pitesti'] = 138
edges['Pitesti']['Bucharest'] = 101
edges['Pitesti']['Rimnicu Vilcea'] = 97
edges['Craiova']['Rimnicu Vilcea'] = 146
edges['Oradea']['Zerind'] = 71
edges['Oradea']['Sibiu'] = 151
edges['Sibiu']['Fagaras'] = 99
edges['Sibiu']['Rimnicu Vilcea'] = 80
edges['Fagaras']['Bucharest'] = 211
edges['Bucharest']['Giurgiu'] = 90
edges['Bucharest']['Urziceni'] = 85 
edges['Urziceni']['Hirsova'] = 98
edges['Hirsova']['Eforie'] = 86
edges['Urziceni']['Vaslui'] = 142 
edges['Vaslui']['Iasi'] = 92 
edges['Iasi']['Neamt'] = 87 

graph = Graph(cities, edges)

## Here is where you input the start node and target node for the calculation.
previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node='Arad')
print_result(previous_nodes, shortest_path, start_node='Arad', target_node='Craiova')
