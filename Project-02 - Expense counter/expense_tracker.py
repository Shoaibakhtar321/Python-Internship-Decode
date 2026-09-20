total = 0

print("===== Expense Tracker =====")
print("Enter your expense one by one.")
print("Type 'done' when you have finished۔ \n")

while True:
    expense = input("Enter expense: ")
    if expense.lower() == 'done':
        break
    
    try:
        expense = float(expense)
        if expense < 0:
            print("Enter a positive amount. \n")
            continue
        total = total + expense
    except ValueError:
        print("Invalid input. Please enter a number or type 'done'. \n")
        
total = round(total, 2)
        
    
print("\n ==== Expense Summary ====")
print(f"Total Spent: {total}")
    


    
    

