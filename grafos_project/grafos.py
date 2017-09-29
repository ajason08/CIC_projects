import networkx as nx

def detect_node_for_problem_9(g):
    T = nx.Graph()
    root = g.nodes()[0]
    layers = [[root]]
    descubiertos = [root]
    count_L = 0
    layer_actual = layers[count_L]
    while len(layer_actual)>0:
        new_layer = []
        for nodo_u in layer_actual:
            neighborhood = g.neighbors(nodo_u)
            for neighbor in neighborhood:
                if not descubiertos.__contains__(neighbor):
                    descubiertos.append(neighbor)
                    T.add_edges_from([(nodo_u,neighbor)])
                    new_layer.append(neighbor)
        print layer_actual
        if len(layer_actual) ==1 and layer_actual[0] <> root:
            print "deleting this node will destroy all s-t paths", layer_actual[0]
            break
        count_L+=1
        layers.append(new_layer)
        layer_actual = layers[count_L]
    return T

def detect_cylcess(g):
    #using bfs strategy
    T = nx.Graph()
    root = g.nodes()[0]
    layers = [[root]]
    descubiertos = [root]
    count_L = 0
    layer_actual = layers[count_L]
    while len(layer_actual)>0:
        new_layer = []
        for nodo_u in layer_actual:
            neighborhood = g.neighbors(nodo_u)
            for neighbor in neighborhood:
                if not descubiertos.__contains__(neighbor):
                    descubiertos.append(neighbor)
                    T.add_edges_from([(nodo_u,neighbor)])
                    new_layer.append(neighbor)
                else:
                    print "encotre ciclo con ", nodo_u, neighbor
                    if layer_actual.__contains__(neighbor):
                        b = neighbor
                        ciclo = []
                    else:
                        b = T.neighbors(neighbor)[0]
                        ciclo = [neighbor]

                    a = nodo_u
                    while a <> b:# the path through the cycle is finished
                        print a, b
                        ciclo.append(a)
                        ciclo.append(b)
                        if not ciclo.__contains__(T.neighbors(a)[0]):
                            a = T.neighbors(a)[0]
                        else:
                            a = T.neighbors(a)[1]

                        if not ciclo.__contains__(T.neighbors(b)[0]):
                            b = T.neighbors(b)[0]
                        else:
                            b = T.neighbors(b)[1]
                    ciclo.append(a)
                    print ciclo
        count_L+=1
        layers.append(new_layer)
        layer_actual = layers[count_L]
    return T