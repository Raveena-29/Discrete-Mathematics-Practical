''' Write a Program to check if a given graph is a complete graph. Represent the graph using the Adjacency Matrix representation.'''
def is_complete_graph(adj_matrix):
    n = len(adj_matrix)
    for i in range(n):
        for j in range(n):
            if i != j and adj_matrix[i][j] != 1:
                return False
    return True

def main():
    n = int(input("Enter the number of vertices in the graph: "))

    print("Enter the adjacency matrix (separate elements by space):")
    adjacency_matrix = [[int(x) for x in input().split()] for _ in range(n)]

    if is_complete_graph(adjacency_matrix):
        print("The graph is a complete graph.")
    else:
        print("The graph is not a complete graph.")

if __name__ == "__main__":
    main()
