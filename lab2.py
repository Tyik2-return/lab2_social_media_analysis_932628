import networkx as nx
G = nx.cycle_graph(150)
G.add_edge(0, 75)
G.add_edge(149, 75)
centrality = nx.eigenvector_centrality_numpy(G)
for n in centrality:
    print("c(", n, ")=", centrality[n])
sum(centrality)/len(centrality)
