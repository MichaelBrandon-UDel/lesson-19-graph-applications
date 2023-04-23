import networkx as nx
import matplotlib.pyplot as plt

# Define the edges
edges = [("https://acbart.github.io/", "/python-sneks/"),
         ("/python-sneks/", "learner_analysis.html"),
         ("/python-sneks/", "/course_faq.html"),
         ("/python-sneks/", "/assignments.html"),   
         ("https://acbart.github.io/", "/awards/"),
         ("https://acbart.github.io/", "/blog/"),
         ("https://acbart.github.io/", "/completed-projects/"),
         ("https://acbart.github.io/", "/contact/"),
         ("https://acbart.github.io/", "/potential-projects/"),
         ("https://acbart.github.io/", "/publications-and-posters/"),
         ("https://acbart.github.io/", "/sigcse-escapes-22/"),
         ("https://acbart.github.io/", "/sigcse-escapes-23/"),
         ("https://acbart.github.io/", "/students/"),
         ("https://acbart.github.io/", "/teaching-and-mentoring/"),
         ("https://acbart.github.io/", "/papers/"),
         ("/papers/Bart_CV.pdf", "/Bart_CV.pdf"),
         ("/python-sneks/", "python-sneks"),   
         ("python-sneks", "/tools.html"),         
         ("https://acbart.github.io/","runtime-case-builder/?preload=RCB_find_with_break_dynamic.json"),       
         ("python-sneks","/interventions.html"),    
         ("python-sneks","/guide_overview.html"),       
         ("python-sneks","/learner_analysis.html"),   
         ("python-sneks","/course_topics.html"),       
         ("python-sneks","/staff_roles.html"),       
         ("python-sneks","/tools.html"),
         ("python-sneks","/design_decisions.html"),
         ("python-sneks","/course_setup.html"),
         ("python-sneks","/module_guide.html"),
         ("python-sneks","/course_explanations.html"),
         ("python-sneks","/alternatives.html"),
         ("/teaching-and-mentoring/","/files/np-hard-infographic-kbagshaw-clique-cover.pdf"),
         ("/teaching-and-mentoring/","/files/np-hard-infographic-abobo-bridge-capacitated-minimum.png"),
         ("/papers/", "acbart-sigcse19-sneks.pdf"),
         ("/papers/","p160-gusukuma.pdf"),   
         ("/papers/","s03-gusukuma.pdf"),          
         ("/papers/","Bart_AC_D_2017.pdf"),      
         ("/papers/","dissertation-acbart-slides.pdf"),           
         ("/papers/","p66-bart-inroads.pdf"),     
         ("/papers/","acbart-sigcse17-corgis.pdf"),  
         ("/papers/","compsac-paper367.pdf"),           
         ("/papers/","blockpy-position-paper.pdf"),   
         ("/papers/","p63-kafura.pdf"),         
         ("/papers/","sigcse19-python-sneks.pdf")]

# Create a directed graph
G = nx.DiGraph()

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
            
bfs(visited, edges, "https://acbart.github.io/")

# Draw the graph
pos = nx.spring_layout(G, seed=11, k = 2)
plt.figure(figsize=(10, 10))

nx.draw_networkx_nodes(G, pos, node_color="lightblue")
nx.draw_networkx_edges(G, pos, edgelist=edges[:45], width=.5, edge_color="black")
nx.draw_networkx_labels(G, pos, font_size=6, font_family="sans-serif")

plt.axis("off")
plt.show()
