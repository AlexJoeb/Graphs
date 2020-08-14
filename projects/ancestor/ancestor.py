class Q:
    def __init__(self): 
        self.items = []
    
    def __str__(self): 
        return ', '.join([str(x) for x in self.items])
    
    def __repr__(self): 
        return repr(self.items)
    
    def __len__(self): 
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]
    
    def first(self): 
        return self.items[0]

    def clear(self):
        list = self.items
        self.items = []
        return list
    
    def add(self, i):
        self.items.append(i) if isinstance(i, int) else self.items.extend(i)
    
    def pop(self):
        return self.items.pop(0)

    def getItems(self): return self.items

    def anItemHasParent(self, ancestors):
        for item in self.items:
            for indx, (parent, children) in enumerate(ancestors.items()):
                if str(item) in [str(x) for x in children]:
                    return True
        return False
    
    def isEmpty(self): 
        return True if len(self.items) == 0 else False

def earliest_ancestor(ancestors, starting_node):
    # Convert ancestors to dict data-type.
    a = ancestors
    ancestors = {}
    for tup in a:
        if tup[0] not in ancestors:
            ancestors[tup[0]] = []

        ancestors[tup[0]].append(tup[1])

    queue = Q()
    queue.add(starting_node)

    # Make sure the starting node is in the ancestor list and has at least one parent.
    def starting_has_parent(): return len([0 for index, (p, c) in enumerate(ancestors.items()) if starting_node in c])
    def starting_in_ancestors(): return True if starting_node in ancestors else len([0 for index, (p, c) in enumerate(ancestors.items()) if starting_node in c])
    if not starting_has_parent() or not starting_in_ancestors(): return -1
    
    # Starting node has at least one parent, traverse through the 
    while queue.anItemHasParent(ancestors):
        children = queue.clear()
        for child in children:
            parents = [p for index, (p, c) in enumerate(ancestors.items()) if child in c]
            queue.add(parents)

    return queue.getItems()[0]