'''Write a program that generates all the permutations of a given set of set, with or without repetition'''
from itertools import permutations

def generate_permutations(input_set, with_repetition=False):
    if with_repetition:
        return list(permutations(input_set))
    else:
        return list(set(permutations(input_set)))

def main():
    input_set = input("Enter the elements of the set separated by space: ").split()
    with_repetition = input("Do you want permutations with repetition? (yes/no): ").lower().strip() == "yes"
    
    permutations = generate_permutations(input_set, with_repetition)
    
    print("Permutations:")
    for perm in permutations:
        print(perm)

if __name__ == "__main__":
    main()
