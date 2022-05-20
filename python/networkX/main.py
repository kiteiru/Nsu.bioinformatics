import igraph as ig
import matplotlib.pyplot as plt
import random
import networkx as nx
from networkx.algorithms.tournament import is_reachable

def CountNodesCentralities(G, nodeIdx, nodes):
    degCentrality = nx.degree_centrality(G)
    plt.bar(list(degCentrality.keys()), degCentrality.values(), color='#723488')
    plt.title("Deg centrality distribution")
    plt.show()

    nodeCloseness = [nx.closeness_centrality(G, i) for i in range(nodes)]
    plt.bar(nodeIdx, nodeCloseness, color='#1f9cd9')
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


def FindGraphParameters(G, nodeIdx, nodes):
    nodeDeg = [val for (node, val) in G.degree()]
    plt.bar(nodeIdx, nodeDeg, color='#eebb1b')
    plt.title("Node degree distribution")
    plt.show()

    edges = G.number_of_edges()
    density = 2 * edges / (nodes * (nodes - 1))
    print("Graph density: ", round(density, 5))

    # 3коэффициенты кластеризации для всех узлов.

    print("COEFF: ", nx.clustering(G))
    print("Average: ", nx.average_clustering(G))

    # 4максимальную связную компоненту графа.

    # 5все максимальные клики графа.

    # 6диаметр графа.

    print("Graph cycles: ", nx.cycle_basis(G))

    print("Graph assortativity: ", round(nx.degree_assortativity_coefficient(G), 5))

    # 9расстояние от заданной вершины до всех остальных вершин.

    print("k-Components: ", nx.k_components(G))
    print("Average node connectivity: ", nx.average_node_connectivity(G))

    print("Coeff: ", nx.average_clustering(G))
    # print("Diameter: ", nx.diameter(G, e=None, usebounds=False))
    cliques = nx.find_cliques(G)
    print("Cliques: ")
    for clique in cliques:
        print(clique)
    print("Max clique: ", nx.max_clique(G))

    '''
    nonZeroDegree = [i for i in range(nodes) if nx.degree(G)[i] != 0]
    
        for first in range(len(nonZeroDegree) - 1):
            for second in range(first + 1, len(nonZeroDegree)):
                if is_reachable(G, first, second):
                    print("YES" + str(first) + " " + str(second))
                    print("Length from " + str(first) + "node to " + str(second) + "node")
                    print(nx.dijkstra_path_length(G, first, second))'''


def CheckWhetherConnected(G):
    if nx.is_connected(G):
        print("Graph is connected")
    else:
        print("Graph is not connected")


def DrawGraph(G):
    nx.draw_networkx(G, pos=None, arrows=None,
                     with_labels=True, node_size=20,
                     node_color='#e98c3c', font_size=8, font_color='#992161',
                     alpha=0.7, linewidths=5, edge_color='#992161', style='solid',
                     label='Erdos-Renyi graph')
    plt.show()


def main():
    nodes = 100
    probability = 0.01
    nodeIdx = [i for i in range(nodes)]

    G = nx.erdos_renyi_graph(nodes, probability, directed=False)

    DrawGraph(G)
    CheckWhetherConnected(G)
    FindGraphParameters(G, nodeIdx, nodes)
    CountNodesCentralities(G, nodeIdx, nodes)


if __name__ == "__main__":
    main()
