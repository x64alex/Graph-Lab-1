from DirectedGraph import DirectedGraph
from random import choice


def random_generate_graph(n, m):
    """
    Random generates a graph with n vertices and m edges
    """
    graph = DirectedGraph(n)
    graph.set_number_of_edges(m)
    set_of_vertices = [i for i in range(n)]
    costs = [0]
    for i in range(1, 101):
        costs.append(i)
        costs.append(-i)
    index = 0
    while index < m:
        start = choice(set_of_vertices)
        end = choice(set_of_vertices)
        cost = choice(costs)
        graph.add_edge(start, end, cost)
        index += 1

    return graph


def load_from_file(file_name):
    """Load the file from file_name and return it as a directedGraph"""
    try:
        with open(file_name, "r") as file:
            first_line = file.readline()
            first_line = first_line.strip().split()
            vertices, edges = int(first_line[0]), int(first_line[1])
            graph = DirectedGraph(vertices)

            for times in range(edges):
                line = file.readline()
                line = line.strip().split()
                start, end, cost = int(line[0]), int(line[1]), int(line[2])
                graph.add_edge(start, end, cost)
        print("Graph loaded.")
        return graph

    except FileNotFoundError:
        print("File doesn't exist!")


def write_to_file(graph, file_name):
    """Write the graph the file_name"""
    with open(file_name, "w") as file:
        edges = graph.get_number_of_edges()
        file.write(str(graph.get_number_of_vertices()) + " " + str(edges) + "\n")

        for edge in graph.edges():
            file.write(str(edge[0]) + " " + str(edge[1]) + " " + str(graph.get_cost(edge)) + "\n")
    print("Graph writen.")


class Console:

    def __init__(self):
        self.__graph = DirectedGraph(0)

    def __get_number_of_vertices(self):
        print(self.__graph.get_number_of_vertices())

    def __print_all_vertices(self):
        print(self.__graph.parse_keys())

    def __edge_from_x_to_y(self):
        print("Give vertices x and y:")
        start = int(input())
        end = int(input())
        result = {True: "Yes", False: "No", -1: "No"}
        print(result[self.__graph.is_edge(start, end)])

    def __get_degrees(self):
        vertex = int(input("Give vertex:"))
        print("Out degree: " + str(self.__graph.get_out_degree(vertex)))
        print("In degree: " + str(self.__graph.get_in_degree(vertex)))

    def __modify_cost(self):
        print("Give edge start:")
        start = int(input())
        print("Give edge end:")
        end = int(input())
        print(self.__graph.retrieve_cost(start, end))
        print("Give new cost:")
        cost = int(input())
        if self.__graph.modify_edge_cost(start, end, cost) == -1:
            print("The edge does not exists!")

    def __add_vertex(self):
        print("Give new vertex:")
        vertex = int(input())
        if self.__graph.add_vertex(vertex) == -1:
            print("The vertex already exists!")

    def __isolated_vertices(self):
        print(self.__graph.all_isolated_vertices())

    def __add_edge(self):
        start = int(input("Give edge start:"))
        end = int(input("Give edge end:"))
        cost = int(input("Give edge cost:"))
        if self.__graph.add_edge(start, end, cost) == 0:
            print("The edge already exits!")

    def __remove_edge(self):
        start = int(input("Give edge start:"))
        end = int(input("Give edge end:"))
        if self.__graph.remove_edge(start, end) == -1:
            print("The edge does not exist!")

    def __remove_vertex(self):
        vertex = int(input("Give vertex you want to remove:"))
        if self.__graph.remove_vertex(vertex) == -1:
            print("The vertex does not exist!")

    def __copy_graph(self):
        print("Copying the graph...")
        self.__graphCopy = self.__graph.copy_graph()
        print("The graph is now copied and stored in __graphCopy")

    def __print_graph_copy(self):
        print(self.__graphCopy.parseKeys())
        print(self.__graphCopy.edges())

    def __print_graph(self):
        print("The vertices of the graph are: ")
        print(self.__graph.parse_keys())
        print("The edges of the graph are: ")
        print(self.__graph.edges())

    def __read_from_file(self):
        file_name = input("Enter file name:")
        self.__graph = load_from_file(file_name)

    def __write_to_file(self):
        file_name = input("Enter file name:")
        write_to_file(self.__graph, file_name)

    def __generate_graph(self):
        try:
            number_vertices = int(input("Enter the number of vertices:"))
            number_edges = int(input("Enter the number of edges:"))
            self.__graph = random_generate_graph(number_vertices, number_edges)
        except ValueError:
            print("Invalid values for the vertices and edges")

    @staticmethod
    def print_menu():
        print("Options:\n")
        print("0.Exit the program")
        print("r.Read from a file")
        print("g.Generate random the graph")
        print("w.Write to a file")
        print("1.Get the number of vertices")
        print("2.See all vertices")
        print("3.See if there is an edge from <x> to <y>")
        print("4.Print the out degree and in degree of a vertex")
        print("5.Modify the cost of an edge")
        print("6.Add a vertex")
        print("7.Add an edge")
        print("8.Remove a vertex")
        print("9.Remove an edge")
        print("10.Make a copy of the graph. The copy will be stored in the main class as a property.")
        print("11.Print the graph vertices and edges.")
        print("12.Print the copy of the graph with its vertices and edges.")

    def run(self):
        while True:
            self.print_menu()
            cmd = input("Enter option:")
            if cmd == "0":
                return
            if cmd == "r":
                self.__read_from_file()
            if cmd == "g":
                self.__generate_graph()
            if cmd == "w":
                self.__write_to_file()
            if cmd == "1":
                self.__get_number_of_vertices()
            if cmd == "2":
                self.__print_all_vertices()
            if cmd == "3":
                self.__edge_from_x_to_y()
            if cmd == "4":
                self.__get_degrees()
            if cmd == "5":
                self.__modify_cost()
            if cmd == "6":
                self.__add_vertex()
            if cmd == "7":
                self.__add_edge()
            if cmd == "8":
                self.__remove_vertex()
            if cmd == "9":
                self.__remove_edge()
            if cmd == "10":
                self.__copy_graph()
            if cmd == "11":
                self.__print_graph()
            if cmd == "12":
                self.__print_graph_copy()


c = Console()
c.run()
