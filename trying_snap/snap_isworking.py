import snap
import Gnuplot

G1 = snap.TNGraph.New()
G1.AddNode(1)
G1.AddNode(5)
G1.AddNode(32)
G1.AddEdge(1,1)
G1.AddEdge(1,1)
G1.AddEdge(5,5)
G1.AddEdge(5,32)


print snap.CntSelfEdges(G1)
