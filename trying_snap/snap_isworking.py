import snap
import Gnuplot

G1 = snap.TNGraph.New()
G1.AddNode(1)
G1.AddNode(5)
G1.AddNode(32)
G1.AddEdge(1,5)
G1.AddEdge(5,1)
G1.AddEdge(5,5)
G1.AddEdge(5,32)
G1.AddEdge(5,1)

g = snap.LoadEdgeList(snap.PNGraph, "C:\Users\cic2017ge\Downloads\wiki-Vote.txt", 0, 1)
