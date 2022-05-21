install.packages("igraph")
library(igraph)

g <- erdos.renyi.game(
  n = 100,
  p = 0.01,
  type = c("gnp"),
  directed = FALSE,
  loops = FALSE
)

plot(g, vertex.size=4,
     vertex.size=30,
     vertex.label.size=1,
     vertex.color="purple", 
     edge.arrow.size=6)

vertex_con <- vertex_connectivity(g, source = NULL, target = NULL, checks = TRUE)
edge_con <- edge_connectivity(g, source = NULL, target = NULL, checks = TRUE)

if (vertex_con == 0) {
  print("Vertex cnnectivity: Graph is not strongly connected")
} else {
  cat("Vertex cnnectivity:", vertex_con)
}

if (edge_con == 0) {
  print("Edges cnnectivity: Graph is not strongly connected")
} else {
  cat("Edges cnnectivity:", edge_con)
}

vertex_degree <- degree(g)
hist(vertex_degree)

density <- edge_density(g)
cat("Graph density: ", density)

connectivity_coeff <- transitivity(g, type = c("undirected"))
cat("Graph connectivity coefficient: ", connectivity_coeff)

clusters <- clusters(g)
max_cluster_id <- which.max(clusters$csize)
vertex_ids <- V(g)[clusters$membership == max_cluster_id]
max_cluster <- induced_subgraph(g, vertex_ids)
print("Graph maximal connected component: ")
print(max_cluster)

cliq <- largest_cliques(g)
cat("Largest cliques in graph:")
print(cliq)

graph_diameter <- diameter(g)
cat("Graph diameter: ", graph_diameter)

all_cycles = NULL
for(v1 in V(g)) {
  for(v2 in neighbors(g, v1, mode="out")) {
    all_cycles = c(all_cycles, 
                   lapply(all_simple_paths(g, v2,v1, mode="out"), 
                   function(p) c(v1,p)))
  }
}
unique_cycles = all_cycles[which(sapply(all_cycles, length) > 3)]
print("Cycles in graph:")
unique_cycles[sapply(unique_cycles, min) == sapply(unique_cycles, `[`, 1)]

if (has_eulerian_cycle(g) == TRUE) {
  cat("Graph has Eulerian cycles: ", eulerian_path(g))
} else {
  print("Graph has no Eulerian cycles")
}

assort <- assortativity_degree(g, directed = FALSE)
cat("Graph assortativity coefficient: ", assort)

table <- data.frame(distances(g, mode="all"))
input_vertex <- as.integer(readline(prompt = "Enter number of vertex from 1 to 100: "))
if (input_vertex < 1 || input_vertex > 100) {
  print("Usage: vertex number should be from 1 to 100")
} else {
  cat("Distance table to all graph vertex from vertex number ", input_vertex)
  print(table[input_vertex])
}

degree_centrality <- degree(g)
print(degree_centrality)
plot(degree_distribution(g))

closeness_centrality <- closeness(g, v = V(g))
print(closeness_centrality)
hist(closeness_centrality)

betweenness_centrality <- betweenness(g, v = V(g))
print(betweenness_centrality)
hist(betweenness_centrality)

file <- "/home/kiteiru/Coding/python/bioinf/Nsu.bioinformatics/R/graph.txt"
write_graph(g, file, format = "edgelist")
