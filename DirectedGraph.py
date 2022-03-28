import copy


class DirectedGraph:

    def __init__(self, vertices):

        self.__dictIn = {}

        self.__dictOut = {}

        self.__dictCosts = {}

        self.__vertices = vertices

        self.__edges = 0

        for i in range(vertices):
            self.__dictOut[i] = []
            self.__dictIn[i] = []

    def parse_keys(self):
        """Returns the keys of the dictionary dict out"""
        return list(self.__dictOut.keys())

    def is_edge(self, start, end):
        """Returns True if there is an edge from x to y, False otherwise -1 if there is an error"""
        try:
            return end in self.__dictOut[start]
        except KeyError:
            return -1

    def add_edge(self, start, end, cost):
        """Tries to add the edge to the graph. Returns 0 if the edge already exists or if it was an error.
        Returns 1 if the edge was successfully added"""
        if (self.is_edge(start, end) == -1) or (self.is_edge(start, end) is True):
            return 0
        self.__edges += 1
        self.__dictOut[start].append(end)
        self.__dictIn[end].append(start)
        self.__dictCosts[(start, end)] = cost
        return 1

    def add_vertex(self, x):
        """Tries to add the edge to the graph.
        Returns -1 if the edge already exists.
        Returns 1 if the vertex was successfully added"""
        if x in self.parse_keys():
            return -1
        self.__dictOut[x] = []
        self.__dictIn[x] = []
        return 1

    def retrieve_cost(self, start, end):
        """Retrieves the cost of the edge. If the edge doesn't exist return -1"""
        try:
            if self.is_edge(start, end):
                return self.__dictCosts[(start, end)]
        except Exception:
            return -1

    def remove_vertex(self, x):
        """Tries to remove the vertex. Returns 1if it was successfully -1 otherwise"""
        if x not in self.parse_keys():
            return -1
        for y in self.__dictOut[x]:
            self.__dictIn[y].remove(x)
            del self.__dictCosts[(x, y)]
            self.__edges -= 1
            print(self.__edges)
        del self.__dictOut[x]
        for y in self.__dictIn[x]:
            self.__dictOut[y].remove(x)
            del self.__dictCosts[(y, x)]
            self.__edges -= 1
            print(self.__edges)
        del self.__dictIn[x]

        return 1

    def remove_edge(self, x, y):
        """Tries to remove the edge. Returns 1if it was successfully -1 otherwise"""
        if not self.is_edge(x, y):
            return -1
        del self.__dictCosts[(x, y)]
        self.__dictOut[x].remove(y)
        self.__dictIn[y].remove(x)
        self.__edges -= 1

    def get_number_of_vertices(self):
        """Returns the number of vertices"""
        return len(self.parse_keys())

    def set_number_of_edges(self, edges):
        """Set the number of edges"""
        self.__edges = edges

    def get_number_of_edges(self):
        """Returns the number of edges"""
        return self.__edges

    def get_out_degree(self, x):
        """Returns the length of the dic out. Returns -1 if x is not an vertex for the graph"""
        try:
            return len(self.__dictOut[x])
        except KeyError:
            return -1

    def get_in_degree(self, x):
        """Returns the length of the in dictionary of the vertex x if it exists
        Returns False if it is an error
        """
        try:
            return len(self.__dictIn[x])
        except KeyError:
            return -1

    def modify_edge_cost(self, start, end, c):
        """
        Modify the cost of the edge (start,end) with the new cost c
        """
        if (start, end) in self.__dictCosts:
            self.__dictCosts[(start, end)] = c
        else:
            return 0

    def all_isolated_vertices(self):
        """
        Returns the isolated vertices.
        """
        vertices = []
        for k in self.parse_keys():
            if self.__dictIn[k] == [] and self.__dictOut[k] == []:
                vertices.append(k)
        return vertices[:]

    def copy_graph(self):
        """
        Copy the graph and returns the copy
        """
        new_graph = DirectedGraph(10)
        new_graph.__dictIn = copy.deepcopy(self.__dictIn)
        new_graph.__dictOut = copy.deepcopy(self.__dictOut)
        new_graph.__dictCosts = copy.deepcopy(self.__dictCosts)
        return new_graph

    def edges(self):
        """
        Returns all the edges
        """
        edges_list = []
        for edges in self.__dictCosts:
            edges_list.append(edges)
        return edges_list[:]

    def costs(self):
        """
        Returns all the costs
        """
        costs = []
        for c in self.__dictCosts:
            costs.append(self.__dictCosts[c])
        return costs[:]

    def get_cost(self, values):
        """
        Get the cost for the values
        """
        return self.__dictCosts[values]
