from PFBack import hill_climbing, romania_graph
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx

path_finder_window = tk.Tk()
path_finder_window.title("Path Finder")

def find_path():
    start = start_var.get()
    goal = goal_var.get()

    #heuristic values for Bucharest.
    heuristic_values = {
        'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242, 'Eforie': 161,
        'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
        'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
        'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
    }
    
    
    path = hill_climbing(romania_graph, start, goal, heuristic_values)
    ax.clear()
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color='pink', font_size=10, font_color='black', ax=ax)    
    #path highlighter
    nx.draw_networkx_nodes(graph, pos, nodelist=path, node_color='red', node_size=700, ax=ax)
    canvas.draw()


#labels and combobox 
start_label = tk.Label(path_finder_window, text="Start city:", font="Arial 12 italic")
start_label.grid(row=0, column=0, padx=5, pady=5)
goal_label = tk.Label(path_finder_window, text="Goal city:", font="Arial 12 italic")
goal_label.grid(row=1, column=0, padx=5, pady=5)
find_button = tk.Button(path_finder_window, text="Find Path", command=find_path)
find_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
start_var = tk.StringVar()
start_combobox = ttk.Combobox(path_finder_window, width=20, textvariable=start_var)
start_combobox['values'] = list(romania_graph.keys())
start_combobox.grid(row=0, column=1, padx=5, pady=5)
goal_var = tk.StringVar()
goal_combobox = ttk.Combobox(path_finder_window, width=20, textvariable=goal_var)
goal_combobox['values'] = 'Bucharest'
goal_combobox.grid(row=1, column=1, padx=5, pady=5)

#creating matplotlib figure
fig, ax = plt.subplots(figsize=(6, 6))
canvas = FigureCanvasTkAgg(fig, master=path_finder_window)
canvas_widget = canvas.get_tk_widget()
graph = nx.Graph(romania_graph)
pos = nx.spring_layout(graph, seed=42) 

#Graph
print("Romania Map")
nx.draw(graph, pos, with_labels=True, node_size=700, node_color='pink', font_size=10, font_color='black', ax=ax)
nx.draw_networkx_edges(graph, pos, width=1.0, alpha=0.5,ax=ax)
ax.set_title("Romania Map")
canvas_widget.grid(row=0, column=2, rowspan=3, padx=5, pady=5)

path_finder_window.mainloop()
