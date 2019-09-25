import grafos as mg # my graph library
from pygraphml import Graph
import matplotlib.pyplot as plt
import networkx as nx


def show_graphs(list_of_graphs, with_labels=True):
    i = 1
    for graph in list_of_graphs:
        plt.figure(i)
        nx.draw_networkx(graph, with_labels=with_labels)
        i += 1
    plt.show()
# Create graph

'''
g = nx.Graph()

n1 = g.add_node("A")
n2 = g.add_node("B")
n3 = g.add_node("C")
n4 = g.add_node("D")
n5 = g.add_node("E")

g.add_edge(n1, n3)
g.add_edge(n2, n3)
g.add_edge(n3, n4)
g.add_edge(n3, n5)      


# Set a root
g.set_root(n1)

nodes = g.BFS()
for node in nodes:
    print(node)

nodes = g.DFS_prefix()
for node in nodes:
    print(node) 

#g.show()
#'''

'''
# random graph
graph = nx.gnp_random_graph(7, .3, directed=False)
for node in graph.nodes():
    graph.node[node]['label'] = "node %d" % (node + 1)
nx.readwrite.write_graphml(graph, "random.graphml")
'''
g = nx.DiGraph()
# Graph 1
# g.add_edges_from([(1,2),(2,3),(2,4),(4,3)])

# Graph 2
# g.add_edges_from([(1,2),(2,3),(3,4),(3,7)])
# g.add_edges_from([(4,5),(4,8),(5,6),(8,9)])
# g.add_edges_from([(9,10),(6,10)])

# Graph 3
g.add_edges_from([(1,2),(2,3),(3,4),(3,7)])
g.add_edges_from([(4,5),(4,8),(5,6),(8,9)])
g.add_edges_from([(6,9)])

# Graph 4 for problem 9
# g.add_edges_from([(1,2),(2,3),(3,4),(4,5)])
# g.add_edges_from([(5,6),(6,7),(1,8),(8,9)])
# g.add_edges_from([(9,10),(10,5)])

#print nx.adjacency_matrix(graph)
#tree_1 = nx.bfs_tree(graph,0, False)

T = mg.detect_cylcess(g)

# show graphs
show_graphs([g, T])

#mg.detect_node_for_problem_9(g)


