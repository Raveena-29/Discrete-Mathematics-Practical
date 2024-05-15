
'''1. Create A Class SET. Create Member Functions To Perform The Following SET Operations:
    1) Is Member: Check Whether An Element Belongs To The Set Or Not And Return
    Value As True/False.
    2) Powerset: List All The Elements Of The Power Set Of A Set .
    3) Subset: Check Whether One Set Is A Subset Of The Other Or Not.
    4) Union And Intersection Of Two Sets.
    5) Complement: Assume Universal Set As Per The Input Elements From The User.
    6) Set Difference And Symmetric Difference Between Two Sets.
    7) Cartesian Product Of Sets.
Write A _Menu Driven Program To Perform The Above Functions On An Instance Of The SET Class'''

class SET:
    def __init__(self):
        self.set_elements = set()

    def is_member(self, element):
        return element in self.set_elements

    def powerset(self):
        if len(self.set_elements) == 0:
            return [[]]
        element = next(iter(self.set_elements))
        rest = SET()
        rest.set_elements = self.set_elements.difference({element})
        without_element = rest.powerset()
        with_element = [ [element] + subset for subset in without_element]
        return without_element + with_element

    def subset(self, other):
        return self.set_elements.issubset(other.set_elements)

    def union(self, other):
        return self.set_elements.union(other.set_elements)

    def intersection(self, other):
        return self.set_elements.intersection(other.set_elements)

    def complement(self, universal_set):
        return universal_set.set_elements.difference(self.set_elements)

    def set_difference(self, other):
        return self.set_elements.difference(other.set_elements)

    def symmetric_difference(self, other):
        return self.set_elements.symmetric_difference(other.set_elements)

    def cartesian_product(self, other):
        return {(a, b) for a in self.set_elements for b in other.set_elements}


def main():
    set1 = SET()
    set2 = SET()
    universal_set = SET()

    print("Enter the elements of universal set separated by space:")
    universal_set.set_elements = set(input().split())

    print("Enter the elements of set1 separated by space:")
    set1.set_elements = set(input().split())

    print("Enter the elements of set2 separated by space:")
    set2.set_elements = set(input().split())

    while True:
        print("\nSet Operations Menu:")
        print("1. Check if an element is a member of set1 or set2")
        print("2. Display the power set of set1")
        print("3. Check if set1 is a subset of set2")
        print("4. Perform union of set1 and set2")
        print("5. Perform intersection of set1 and set2")
        print("6. Find complement of set1")
        print("7. Find set difference of set1 and set2")
        print("8. Find symmetric difference of set1 and set2")
        print("9. Find Cartesian product of set1 and set2")
        print("10. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            element = input("Enter the element to check: ")
            print(f"Is {element} a member of set1? {set1.is_member(element)}")
            print(f"Is {element} a member of set2? {set2.is_member(element)}")

        elif choice == 2:
            print("Power set of set1:", set1.powerset())

        elif choice == 3:
            print("Is set1 a subset of set2?", set1.subset(set2))

        elif choice == 4:
            print("Union of set1 and set2:", set1.union(set2))

        elif choice == 5:
            print("Intersection of set1 and set2:", set1.intersection(set2))

        elif choice == 6:
            print("Complement of set1:", set1.complement(universal_set))

        elif choice == 7:
            print("Set difference of set1 and set2:", set1.set_difference(set2))

        elif choice == 8:
            print("Symmetric difference of set1 and set2:", set1.symmetric_difference(set2))

        elif choice == 9:
            print("Cartesian product of set1 and set2:", set1.cartesian_product(set2))

        elif choice == 10:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose a number from 1 to 10.")


if __name__ == "__main__":
    main()

