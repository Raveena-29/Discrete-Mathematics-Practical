'''For any number n, write a program to list all the solutions of the equation x1 + x2 + 
x3 + ...+ xn = C, where C is a constant (C<=10) and x1, x2,x3,...,xn are non-negative 
integers, using brute force strategy.'''
def find_solutions(n, C):
    solutions = []
    def generate(solution, remaining_sum, index):
        if index == n - 1:
            solution[index] = remaining_sum
            solutions.append(tuple(solution))
            return
        for i in range(remaining_sum + 1):
            solution[index] = i
            generate(solution.copy(), remaining_sum - i, index + 1)

    generate([0] * n, C, 0)
    return solutions

def main():
    n = int(input("Enter the number of variables (n): "))
    C = int(input("Enter the value of C (C <= 10): "))

    solutions = find_solutions(n, C)

    print("Solutions:")
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
