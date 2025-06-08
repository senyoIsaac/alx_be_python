def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add an item to the list
            item = input("Enter the item to add: ").strip()
            if item:  # Only add if the input isn't empty
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("No item entered. Please try again.")
                
        elif choice == '2':
            # Remove an item from the list
            if not shopping_list:
                print("The shopping list is empty.")
                continue
                
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' was not found in the shopping list.")
                
        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("Your shopping list is currently empty.")
            else:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                    
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()