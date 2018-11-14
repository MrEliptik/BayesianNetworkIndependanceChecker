import re

class Variable:
    def __init__(self, name, parents):
        self.name = name
        self.parents = parents

def main():
    f = open("example.txt", "r") 
    lines = f.readlines()
    for line in lines:
        print(line.strip())
    nb_nodes, nb_queries = re.split(' ', lines[0])
    nb_nodes = int(nb_nodes)
    nb_queries = int(nb_queries)

    # Get variables and their parenting links
    # Goes through each lines
    for i in range(1, 1+nb_nodes):
        # Separate the line in different items
        items = re.split(' ', lines[i])
        # Items[0] is the variable and the others are its parents
        parents = []
        var = None
        for i, item in enumerate(items):
            print(item)
            # Variable
            if(i == 0):
                var = item
            # Parents
            else:
                parents.append(item)
        # Create corresponding object
        obj = Variable(var, parents)

  

if __name__ == '__main__':
    main()