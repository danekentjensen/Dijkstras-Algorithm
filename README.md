# Dijkstra's Algorithm: Shortest Path Between Romanian Cities

This repository contains a Python implementation of Dijkstra's algorithm to calculate the shortest path between cities in Romania. Cities are represented as graph nodes, and distances between them are weighted edges.

---

## Features

- **Graph Representation**: Uses a Python class to create and manipulate the graph.
- **Shortest Path Calculation**: Efficiently computes the shortest path and its cost.
- **Romanian Map Simulation**: Models real Romanian cities and distances.

---

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/danekentjensen/Dijkstras-Algorithm.git
   cd Dijkstras-Algorithm
   ```

2. Run the Python script:
   ```bash
   python dijkstras_algorithm.py
   ```

3. The default example calculates the shortest path between `Arad` and `Bucharest`. Modify the `start_node` and `target_node` in the script to find paths between other cities.

---

## Example Output

Running the program will produce output similar to this:
```
The shortest path had a value of: 418
Path Taken: Arad  ->  Sibiu  ->  Rimnicu Vilcea  ->  Pitesti  ->  Bucharest
```

---

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
- Giurgiu
- Urziceni
- Hirsova
- Eforie
- Vaslui
- Iasi
- Neamt

The program includes the following distances between cities:
- Arad -> Zerind = 75
- Arad -> Sibiu = 140
- Arad -> Timisoara = 118
- Timisoara -> Lugoj = 111
- Lugoj -> Mehadia = 70
- Mehadia -> Drobeta = 75
- Drobeta -> Craiova = 120
- Craiova -> Pitesti = 138
- Pitesti -> Bucharest = 101
- Pitesti -> Rimnicu Vilcea = 97
- Craiova -> Rimnicu Vilcea = 146
- Oradea -> Zerind = 71
- Oradea -> Sibiu = 151
- Sibiu -> Fagaras = 99
- Sibiu -> Rimnicu Vilcea = 80
- Fagaras -> Bucharest = 211
- Bucharest -> Giurgiu = 90
- Bucharest -> Urziceni = 85
- Urziceni -> Hirsova = 98
- Hirsova -> Eforie = 86
- Urziceni -> Vaslui = 142
- Vaslui -> Iasi = 92
- Iasi -> Neamt = 87 

Visualization of the cities and distances
![Romanian Cities](https://github.com/user-attachments/assets/077b7306-5ada-4d9c-bb4b-44503763aa6b)

---

## How It Works

1. The cities are represented as nodes in a graph.
2. Edges represent distances between connected cities.
3. The program computes the least-cost path using Dijkstra's algorithm.

---

## Contribution

Feel free to fork this repository and submit pull requests to improve the project or add new features.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
