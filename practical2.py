'''Create a class RELATION, use Matrix notation to represent a relation. Include
member functions to check if the relation is Reflexive, Symmetric, Anti-symmetric, 
Transitive. Using these functions check whether the given relation is: Equivalence or Partial Order relation or None'''

class RELATION:
    def __init__(self, matrix):
        self.matrix = matrix

    def is_reflexive(self):
        n = len(self.matrix)
        for i in range(n):
            if self.matrix[i][i] != 1:
                return False
        return True

    def is_symmetric(self):
        n = len(self.matrix)
        for i in range(n):
            for j in range(i+1, n):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

    def is_antisymmetric(self):
        n = len(self.matrix)
        for i in range(n):
            for j in range(i+1, n):
                if self.matrix[i][j] == 1 and self.matrix[j][i] == 1:
                    return False
        return True

    def is_transitive(self):
        n = len(self.matrix)
        for i in range(n):
            for j in range(n):
                if self.matrix[i][j] == 1:
                    for k in range(n):
                        if self.matrix[j][k] == 1 and self.matrix[i][k] != 1:
                            return False
        return True

    def is_equivalence_relation(self):
        if self.is_reflexive() and self.is_symmetric() and self.is_transitive():
            return True
        return False

    def is_partial_order_relation(self):
        if self.is_reflexive() and self.is_antisymmetric() and self.is_transitive():
            return True
        return False

def main():
    n = int(input("Enter the size of the relation matrix: "))
    print("Enter the relation matrix (0 or 1):")
    relation_matrix = [[int(input()) for _ in range(n)] for _ in range(n)]

    relation = RELATION(relation_matrix)

    if relation.is_equivalence_relation():
        print("The relation is an Equivalence relation.")
    elif relation.is_partial_order_relation():
        print("The relation is a Partial Order relation.")
    else:
        print("The relation is None.")


if __name__ == "__main__":
    main()
