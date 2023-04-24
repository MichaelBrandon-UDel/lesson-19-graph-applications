import networkx as nx
import matplotlib.pyplot as plt

# Define the edges
edges = [("Dashboard", "CISC437"),
         ("Dashboard", "CISC320"),
         ("Dashboard", "FASH122"),
         ("Dashboard", "CISC355"),
         ("Dashboard", "ENTR356")
         ("Dashboard", "Groups"),
         ("Dashboard", "Inbox"),
         ("Dashboard", "Account"),
         ("Dashboard", "Courses"),
         ("Dashboard", "Calendar"),
         ("Dashboard", "History")
         ("Dashboard", "Commons"),
         ("Courses", "CISC437"),
         ("Courses", "CISC320"),
         ("Courses", "FASH122"),
         ("Courses", "CISC355"),
         ("Courses", "ENTR356"),
         ("Account", "Notifications"),
         ("Account", "Profile"),
         ("Calendar", "Lesson 19"),
         ("Calendar", "Chapter 10 Quiz"),
         ("Calendar", "Design Thinking"),
         ("Design Thinking", "ENTR356"),
         ("Lesson 19", "CISC320"),
         ("Chapter 10 Quiz", "CISC437")
         ("Groups", "Project 4"),
         ("Groups", "Different States")
         ("Project 4", "CISC437")
         ("Different States", "CISC320")]
         

# Create a undirected graph
G = nx.Graph()

# Add the edges to the graph
G.add_edges_from(edges)

# Perform BFS traversal and print the nodes visited
visited = []
queue = []

def bfs(visited: list, graph, node: str):
    visited.append(node)
    queue.append(node)
    
    while queue:
        x = queue.pop(0)
        print (x, end = " ")

    for neighbor in graph[x]:
        if neighbor not in visited:
            visited.append(neighbor)
            queue.append(neighbor)
            
bfs(visited, edges, "Dashboard")

# Draw the graph
pos = nx.spring_layout(G, seed=11, k = 2)
plt.figure(figsize=(10, 10))

nx.draw_networkx_nodes(G, pos, node_color="lightblue")
nx.draw_networkx_edges(G, pos, edgelist=edges[:45], width=.5, edge_color="black")
nx.draw_networkx_labels(G, pos, font_size=6, font_family="sans-serif")

plt.axis("off")
plt.show()
