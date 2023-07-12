import json

def save_budget(budget):
    with open('budget.json', 'w') as file:
        json.dump(budget, file)

def load_budget():
    try:
        with open('budget.json', 'r') as file:
            budget = json.load(file)
            return budget
    except FileNotFoundError:
        return{}

def display_menu():
    print("\nBudgeting App Menu:")
    print("1. Add Expense")
    print("2. View Category Balances")
    print("3. Modify Budget")
    print("4. Save and Exit")

def add_expenses(budget):
    category = input("Enter the expense category: ").lower()
    amount = float(input("Enter the expense amount: "))

    if category in budget:
        budget[category] -= amount
        print(f"{amount} added to {category} expenses.")
    else:
        budget[category] = -amount 
        print(f"{amount} added to {category} expenses.")

def view_balances(budget):
    print("\nCategory Balances:")
    for category, balance in budget.items():
        print(f"{category}: {balance}")

def modify_budget(budget):
    category = input("Enter the category to modify: ")

    if category in budget:
        new_budget = float(input("Enter the new budget amount: "))
    else:
        print("Invalid category!")

def main():
    budget = load_budget()
    print("Welcome to the Budgeting App!")

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            add_expenses(budget)
        elif choice == '2':
            view_balances(budget)
        elif choice == '3':
            modify_budget(budget)
        elif choice == '4':
            save_budget(budget)
            print("Budget saved. Exiting...")
            break
        else:
            print("Invalid choice! Please select again.)")

if __name__ == '__main__':
    main()    