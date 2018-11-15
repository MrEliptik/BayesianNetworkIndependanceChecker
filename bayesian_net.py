import re

class Variable:
    def __init__(self, name, parents):
        self.name = name
        self.parents = parents
        self.visited = False

    def __str__(self):
        return "Variale : " + self.name + " Parents : " + str(self.parents)

class Query:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        x_str = y_str = z_str = ""
        for c in self.x:
            x_str += c
        for c in self.y:
            y_str += c
        for c in self.z:
            z_str += c
        return "Query : " + x_str + ";" + y_str + "|" + z_str

    def compute(self, graph):
        # True by default, if one path is correct then False
        value = True
        for x in self.x:
            # Works only for case with direct path
            paths = find_all_paths(graph.graph, x, self.y)   
            print(paths)    
            # no path between x and y 
            if(not paths):
                # no z value
                if(not self.z):   
                    for var in graph.variables:
                        # same parent
                        if(x in graph.graph[var.name] and self.y in graph.graph[var.name]):
                            return False
                    # not same parent
                    return True
                # z is parent of x and y
                elif(x in graph.graph[self.z] and self.y in graph.graph[self.z]):
                    return True
                # y or x is parent of z
                elif(self.z in graph.graph[self.y] or self.z in graph.graph[x]):
                    return False
                # z is parent of x or y
                elif(x in graph.graph[self.z] or self.y in graph.graph[self.z]):
                    return False
                else:
                    return False
            for path in paths:
                # Look if Z is in the path
                # Removing starting and ending point
                if(not self.z in path[1:-1]):
                    return False
        return value

class Graph():
    def __init__(self, variables):
        self.variables = variables
        self.graph = {}
        self.undirected_graph = {}
        self.createGraph()
        self.createUndirectedGraph()

    def createGraph(self):
        for var in self.variables:
            for parent in var.parents:
                if(not (parent in self.graph)):
                    self.graph[parent] = [var.name]
                else:
                    self.graph[parent].append(var.name)
        for var in self.variables:
            if(not (var.name in self.graph)):
                self.graph[var.name] = []

    def createUndirectedGraph(self):
        self.undirected_graph = self.graph.copy()
        for var in self.variables:
            nodes = self.graph[var.name]
            for node in nodes:
                if(node in self.undirected_graph):
                    self.undirected_graph[node].append(var.name)
                

    def __str__(self):
        return str(self.graph) + "\n" + str(self.undirected_graph)

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def find_all_paths_undirected(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def main():
    f = open("example.txt", "r") 
    lines = f.readlines()
    nb_nodes, nb_queries = re.split(' ', lines[0])
    nb_nodes = int(nb_nodes)
    nb_queries = int(nb_queries)

    graph = {}
    variables = []
    queries = []
    results = [] 

    # Get variables and their parenting links
    # Goes through each lines
    for i in range(1, 1+nb_nodes):
        # Separate the line in different items
        items = re.split(' ', lines[i])
        # Items[0] is the variable and the others are its parents
        parents = []
        var = None
        for i, item in enumerate(items):
            # Variable
            if(i == 0):
                var = item.strip()
            # Parents
            else:
                parents.append(item.strip())
        # Create corresponding object
        obj = Variable(var, parents)
        variables.append(obj)
    graph = Graph(variables)
    print(graph)

    # Get queries
    # Goes through each lines
    for i in range(1+nb_nodes, nb_nodes+nb_queries+1):
        x = y = z = None
        x, rest = re.split(';', lines[i])
        x = re.split(' ', x.strip())
        rest = re.sub(' ', '', rest).strip()
        y, z = re.split(r'\|', rest)
        query = Query(x, y, z)
        queries.append(query)

    # Get results
    for i in range(1+nb_nodes+nb_queries, nb_nodes+nb_queries+nb_queries+1):
        results.append(lines[i].strip())

    # Compute results
    for i, query in enumerate(queries):
        print(query)
        print(query.compute(graph))
        print(results[i])
        print("")
   

if __name__ == '__main__':
    main()
