import matplotlib.pyplot as plt
import networkx as nx

def checkWhetherConnected(G):
    if nx.is_connected(G):
        print("Graph is connected")
    else:
        print("Graph is not connected")

def drawGraph(G):
    nx.draw_networkx(G, pos=None, arrows=None,
                     with_labels=True, node_size=20,
                     node_color='#e98c3c', font_size=8, font_color='#992161',
                     alpha=0.7, linewidths=5, edge_color='#992161', style='solid',
                     label='Erdos-Renyi graph')
    plt.show()

def findCentralities(G):
    degCentrality = nx.degree_centrality(G)
    plt.bar(list(degCentrality.keys()), degCentrality.values(), color='#723488')
    plt.title("Deg centrality distribution")
    plt.show()

    nodeCloseness = nx.closeness_centrality(G)
    plt.bar(list(nodeCloseness.keys()), nodeCloseness.values(), color='#1f9cd9')
    plt.title("Node closeness centrality")
    plt.show()

    nodeBetweeness = nx.betweenness_centrality(G)
    plt.bar(list(nodeBetweeness.keys()), nodeBetweeness.values(), color='#18d566')
    plt.title("Node betweenness centrality")
    plt.show()

    if nx.is_connected(G):
        nodeClosenessFlow = nx.current_flow_closeness_centrality(G)
        plt.bar(list(nodeClosenessFlow.keys()), nodeClosenessFlow.values(), color='#ec69af')
        plt.title("Node closeness flow centrality")
        plt.show()

        nodeBetweenessFlow = nx.current_flow_betweenness_centrality(G)
        plt.bar(list(nodeBetweenessFlow.keys()), nodeBetweenessFlow.values(), color='#e98c3c')
        plt.title("Node betweeness flow centrality")
        plt.show()

    else:
        print("Impossible to execute current_flow_closeness_centrality() and current_flow_betweenness_centrality()\n"
              "Cause: Graph is not connected")


nodes = 100
probability = 0.01
nodeIdx = [i for i in range(nodes)]

path = "/home/kiteiru/Coding/python/bioinf/Nsu.bioinformatics/R/graph.txt"
fh = open(path, "rb")
G = nx.read_edgelist(fh)
fh.close()

drawGraph(G)
checkWhetherConnected(G)
nodeDeg = [val for (node, val) in G.degree()]

edges = G.number_of_edges()
density = 2 * edges / (nodes * (nodes - 1))
print("Graph density: ", round(density, 5))

print("COEFF: ", nx.clustering(G))
print("Average: ", nx.average_clustering(G))

maxClusterLen = 0
print("All graph clusters: ")
for cluster in nx.connected_components(G):
    if len(cluster) > maxClusterLen:
        maxClusterLen = len(cluster)
    print(cluster)

print("Max graph cluster: ")
for cluster in nx.connected_components(G):
    if len(cluster) == maxClusterLen:
        print(cluster)

print("Graph cycles: ", nx.cycle_basis(G))

print("Graph assortativity: ", round(nx.degree_assortativity_coefficient(G), 5))

print("k-Components: ", nx.k_components(G))
print("Average node connectivity: ", nx.average_node_connectivity(G))

if nx.is_connected(G):
    print("Diameter: ", nx.diameter(G))
else:
    print("Graph is not connected, impossible to find diameter")

cliques = nx.find_cliques(G)
cliqueList = []
for clique in cliques:
    cliqueList.append(clique)
print("Cliques: ")
print(cliqueList)
maxCliqueLen = 0
for clique in cliqueList:
    if len(clique) > maxCliqueLen:
        maxCliqueLen = len(clique)
print("Graph max cliques: ")
for clique in cliqueList:
    if len(clique) == maxCliqueLen:
        print(clique)

path = nx.all_pairs_shortest_path_length(G)
dpath = {x[0]:x[1] for x in path}
print(dpath)
inputVertex = int(input("Enter number of vertex from 1 to 100: "))
if 1 > inputVertex > 100:
    print("Usage: vertex number should be from 1 to 100")
else:
    print("Distance table to all graph vertex from vertex number ", print(dpath[str(inputVertex)]))

findCentralities(G)