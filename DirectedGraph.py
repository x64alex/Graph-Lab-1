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
        return list(self.__dictOut.keys())

    def parse_iterable_out(self, x):
        return list(self.__dictOut[x])

    def parse_iterable_in(self, x):
        """return a copy of all in neighbours of x"""
        try:
            return list(self.__dictIn[x])
        except KeyError:
            raise Exception("No such vertex")

    def is_edge(self, start, end):
        """Returns True if there is an edge from x to y, False otherwise"""
        try:
            return end in self.__dictOut[start]
        except KeyError:
            raise Exception("No such pair of vertices in the graph.")

    def add_edge(self, start, end, cost):
        exception = ""
        if self.is_edge(start, end):
            exception += "Already an edge;"
        if len(exception):
            raise Exception(exception)
        self.__edges += 1
        self.__dictOut[start].append(end)
        self.__dictIn[end].append(start)
        self.__dictCosts[(start, end)] = cost

    def add_vertex(self, x):
        if x in self.parse_keys():
            raise Exception("Already existing vertex")
        self.__dictOut[x] = []
        self.__dictIn[x] = []

    def retrieve_cost(self, start, end):
        if self.is_edge(start, end):
            return self.__dictCosts[(start, end)]

    def remove_vertex(self, x):
        if x not in self.parse_keys():
            raise Exception("Vertex doesn't exist")
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

    def remove_edge(self, x, y):
        if not self.is_edge(x, y):
            raise Exception("This edge doesn't exist")
        del self.__dictCosts[(x, y)]
        self.__dictOut[x].remove(y)
        self.__dictIn[y].remove(x)
        self.__edges -= 1

    def get_number_of_vertices(self):
        return len(self.parse_keys())

    def set_number_of_edges(self, edges):
        self.__edges = edges

    def get_number_of_edges(self):
        return self.__edges

    def get_out_degree(self, x):
        try:
            return len(self.__dictOut[x])
        except KeyError:
            raise Exception("No such vertex")

    def get_in_degree(self, x):
        try:
            return len(self.__dictIn[x])
        except KeyError:
            raise Exception("No such vertex")

    def modify_edge_cost(self, start, end, c):
        if (start, end) in self.__dictCosts:
            self.__dictCosts[(start, end)] = c
        else:
            raise Exception("No such edge")

    def all_isolated_vertices(self):
        vertices = []
        for k in self.parse_keys():
            if self.__dictIn[k] == [] and self.__dictOut[k] == []:
                vertices.append(k)
        return vertices[:]

    def copy_graph(self):
        new_graph = DirectedGraph(10)
        new_graph.__dictIn = copy.deepcopy(self.__dictIn)
        new_graph.__dictOut = copy.deepcopy(self.__dictOut)
        new_graph.__dictCosts = copy.deepcopy(self.__dictCosts)
        return new_graph

    def edges(self):
        edges_list = []
        for edges in self.__dictCosts:
            edges_list.append(edges)
        return edges_list[:]

    def costs(self):
        costs = []
        for c in self.__dictCosts:
            costs.append(self.__dictCosts[c])
        return costs[:]

    def get_cost(self, values):
        return self.__dictCosts[values]
