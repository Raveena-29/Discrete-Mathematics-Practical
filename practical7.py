'''Write a Program to accept a directed graph G and compute the in-degree and out-degree of each vertex.'''

def compute_degrees(graph):
    in_degree = {}
    out_degree = {}

    for vertex in graph:
        out_degree[vertex] = len(graph[vertex])
        for neighbor in graph[vertex]:
            if neighbor not in in_degree:
                in_degree[neighbor] = 1
            else:
                in_degree[neighbor] += 1

    return in_degree, out_degree

def main():
    graph = {}

    num_edges = int(input("Enter the number of edges: "))

    print("Enter the edges (source destination):")
    for _ in range(num_edges):
        source, destination = map(int, input().split())
        if source not in graph:
            graph[source] = []
        graph[source].append(destination)

    in_degree, out_degree = compute_degrees(graph)

    print("\nVertex\tIn-Degree\tOut-Degree")
    for vertex in sorted(graph.keys()):
        print(f"{vertex}\t{in_degree.get(vertex, 0)}\t\t{out_degree.get(vertex, 0)}")

if __name__ == "__main__":
    main()
