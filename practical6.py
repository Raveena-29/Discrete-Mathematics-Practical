'''Write a Program to check if a given graph is a complete graph. Represent the graph using the Adjacency List representation.'''
def is_complete_graph(adj_list):
    n = len(adj_list)
    for i in range(n):
        for j in range(n):
            if i != j and j not in adj_list[i]:
                return False
    return True

def main():
    n = int(input("Enter the number of vertices in the graph: "))

    print("Enter the adjacency list:")
    adjacency_list = {}
    for i in range(n):
        vertices = list(map(int, input(f"Enter the vertices adjacent to vertex {i}: ").split()))
        adjacency_list[i] = vertices

    if is_complete_graph(adjacency_list):
        print("The graph is a complete graph.")
    else:
        print("The graph is not a complete graph.")

if __name__ == "__main__":
    main()


