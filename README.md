# Dijkstra's Algorithm: Shortest Path Between Romanian Cities

This repository contains a Python implementation of Dijkstra's algorithm to calculate the shortest path between cities in Romania. Cities are represented as graph nodes, and distances between them are weighted edges.

## Features

- **Graph Representation**: Uses a Python class to create and manipulate the graph.
- **Shortest Path Calculation**: Efficiently computes the shortest path and its cost.
- **Romanian Map Simulation**: Models real Romanian cities and distances.

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Dijkstra-Romanian-Cities.git
   cd Dijkstra-Romanian-Cities
   ```

2. Run the Python script:
   ```bash
   python dijkstra.py
   ```

3. The default example calculates the shortest path between `Arad` and `Bucharest`. Modify the `start_node` and `target_node` in the script to find paths between other cities.

## Example Output

Running the program will produce output similar to this:
```
The shortest path had a value of: 418
Path Taken: Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest
```

## Cities and Distances

The program includes the following Romanian cities:
- Arad
- Zerind
- Oradea
- Sibiu
- Fagaras
- Bucharest
- Timisoara
- Lugoj
- Mehadia
- Drobeta
- Craiova
- Rimnicu Vilcea
- Pitesti

## How It Works

1. The cities are represented as nodes in a graph.
2. Edges represent distances between connected cities.
3. The program computes the least-cost path using Dijkstra's algorithm.

## Contribution

Feel free to fork this repository and submit pull requests to improve the project or add new features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
