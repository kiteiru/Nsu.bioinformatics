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
     vertex.label=NA, 
     vertex.color="purple", 
     edge.arrow.size=6)

vertex_con <- vertex_connectivity(g, source = NULL, target = NULL, checks = TRUE)
edge_con <- edge_connectivity(g, source = NULL, target = NULL, checks = TRUE)

if (vertex_con == 0) {
  print("Vertex cnnectivity: Graph is not strongly connected")
} else {
  print("Vertex cnnectivity:", vertex_con)
}

if (edge_con == 0) {
  print("Edges cnnectivity: Graph is not strongly connected")
} else {
  print("Edges cnnectivity:", edge_con)
}

deg <- degree(g)
print(deg)
plot(deg)

distr <- degree.distribution(g)
plot(distr)

density <- edge_density(g)
print("Graph density: ", density)

assort <- assortativity_degree(g, directed = FALSE)
print("Graph assortativity coefficient: ", assort)

cliq <- largest_cliques(g)
print("Largest cliques in graph: ")
print(cliq)


if (has_eulerian_cycle(g) == TRUE) {
  print("Graph has Eulerian cycles: ")
  print(eulerian_path(g))
} else {
  print("Graph has no Eulerian cycles")
}


table <- data.frame(distances(g, mode="all"))
print(table[43, ])

