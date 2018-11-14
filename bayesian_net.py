import re

class Variable:
    def __init__(self, name, parents):
        self.name = name
        self.parents = parents

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

    def compute(self):
        
        return value

def main():
    f = open("example.txt", "r") 
    lines = f.readlines()
    for line in lines:
        print(line.strip())
    nb_nodes, nb_queries = re.split(' ', lines[0])
    nb_nodes = int(nb_nodes)
    nb_queries = int(nb_queries)
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
        #print(obj)

    # Get queries
    # Goes through each lines
    for i in range(1+nb_nodes, nb_nodes+nb_queries+1):
        x = y = z = None
        x, rest = re.split(';', lines[i])
        x = re.split(' ', x.strip())
        rest = re.sub(' ', '', rest).strip()
        y, z = re.split(r'\|', rest)
        #print(x, y, z)
        query = Query(x, y, z)
        queries.append(query)
        #print(query)

    # Get results
    for i in range(1+nb_nodes+nb_queries, nb_nodes+nb_queries+nb_queries+1):
        results.append(lines[i].strip())
    
    for var in variables:
        print(var)

    for query in queries:
        print(query)
    
    for res in results:
        print(res)

    # Compute results
    for query in queries:
        print(query.compute())

   

if __name__ == '__main__':
    main()