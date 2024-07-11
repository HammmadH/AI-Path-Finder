def get_neighbours(city, graph):
    return graph[city]

def select_best_neighbour(neighbours, heuristic_value):
    best_neighbour = None
    best_cost = float('inf')
    for neighbour in neighbours:
        cost = heuristic_value[neighbour]
        if cost < best_cost:
            best_neighbour = neighbour
            best_cost = cost
    return best_neighbour

def hill_climbing(graph, start, goal, heuristic_value):
    path=[]
    path.append(start)
    current_city = start
    while current_city != goal:
        neighbours = get_neighbours(current_city, graph)
        best_neighbour = select_best_neighbour(neighbours,heuristic_value)      
        if best_neighbour is None or heuristic_value[best_neighbour] >= heuristic_value[current_city]:
            break
        if heuristic_value[best_neighbour] < heuristic_value[current_city]:
             current_city = best_neighbour
             path.append(best_neighbour)
    return path

romania_graph = {
    'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
    'Zerind': ['Arad', 'Oradea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
    'Mehadia': ['Lugoj', 'Dobreta'],
    'Dobreta': ['Mehadia', 'Craiova'],
    'Craiova': ['Dobreta', 'Rimnicu Vilcea', 'Pitesti'],
    'Pitesti': ['Craiova', 'Rimnicu Vilcea', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova']
}