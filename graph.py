class Graph:

    def __init__(self):
        self.dict = {}

    def __init__(self, dictArg):
        self.dict = dictArg

    def get_adjlist(self,node):
        return self.dict.get(node)

    def is_adjacent(self,node1,node2):
        x = self.dict.get(node1)
        if(node2 in x):
            return True
        return False

    def num_nodes(self):
        return len(self.dict)

    def __str__(self):
        return str(self.dict)

    def __iter__(self):
        iter(self.dict)
        return

    def __contains__(self, node):
        if(self.dict.has_key(node)):
            return True
        return False

    def __len__(self):
        return len(self.dict)

    def add_node(self,node):
        if(not (self.__contains__(node))):
            self.dict.update(node)
            return True
        return False

    def link_nodes(self,node1,node2):
        if((not (self.__contains__(node1))) or (not (self.__contains__(node2))) or (node1 == node2) or self.is_adjacent(node1,node2)):
            return False
        else:
            x = self.get_adjlist(node1).append(node2)
            y = self.get_adjlist(node2).append(node1)
            del self.dict[node1]
            del self.dict[node2]
            self.dict.update({node1:x})
            self.dict.update({node2:y})

            return True
    def unlink_nodes(self, node1, node2):
        if(not(self.is_adjacent(node1,node2)) or (not (self.__contains__(node1))) or (not (self.__contains__(node2)))):
            return False
        else:
            x = self.get_adjlist(node1).remove(node2)
            y = self.get_adjlist(node2).remove(node1)
            del self.dict[node1]
            del self.dict[node2]
            self.dict.update({node1: x})
            self.dict.update({node2: y})
            return True

    def del_node(self, node):
        if(not (self.__contains__(node))):
            return False
        else:
            x = self.get_adjlist(node)
            for key in x:
                y = self.get_adjlist(key).remove(node)
                del self.dict[key]
                self.dict.update({key: y})
            del self.dict[node]
            return True

