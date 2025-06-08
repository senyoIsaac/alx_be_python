task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()

# Validate priority input
while priority not in ["high", "medium", "low"]:
    print("Invalid priority. Please enter high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower()

# Get time-bound status
time_bound = input("Is it time-bound? (yes/no): ").lower()
while time_bound not in ["yes", "no"]:
    print("Please answer with yes or no.")
    time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task using match case
match priority:
    case "high":
        priority_msg = "high priority task"
    case "medium":
        priority_msg = "medium priority task"
    case "low":
        priority_msg = "low priority task"

# Add time sensitivity
if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority_msg} that requires immediate attention today!")

elif priority == "low":
       print(f"Note: '{task}' is a {priority_msg}. Consider completing it when you have free time.")
     print(f"Reminder: '{task}' is a {priority_msg} that requires immediate attention today!")


    if priority == "low":
        reminder = f"Note: '{task}' is a {priority_msg}. Consider completing it when you have free time."
    else:
        reminder = f"Reminder: '{task}' is a {priority_msg}, but no immediate deadline."

# Print the final reminder
print("\n" + reminder)