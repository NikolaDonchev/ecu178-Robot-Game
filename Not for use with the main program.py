#Liam Walsh
#Dijkstra's algorithm
#Code based on https://gist.github.com/econchick/4666413

class Graph:
    def __init__(self):
        self.nodes= set()
        self.edges = defdict(list)
        self.distances = {}

    def addNode(self,value):
        self.nodes.add(value)

    def addEdge(self,from_node,to_node):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


#initalisation
    def dijskra_start(graph,initial):
        visited ={initial:0}
        path = {}

        nodes = set(graph.nodes)

        while nodes: #Replacment of 
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node]< visited [min_node]:
                        min_node = node

                    if node is None:
                        break
                    #Removal of previous 
                    nodes.remove(min.node)
                    current_weight = visited[min_node]

            for edge in graph.edges [min_node]:
                weight = current_weight + graph.distance[(min_node,edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = min_node
                    
        return visited, path
#interpreting the data unsure if this is needed not finished either 
def shortest_path(graph, origin, destination):


    visited = dijkstra(graph,origin,destination
    full_path = x()
    destination_end = paths(destination)
                
        
                                            
