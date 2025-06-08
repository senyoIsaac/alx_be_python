from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in a readable format"""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(days):
    """Calculate and return the date after adding specified days to current date"""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Date after {days} days: {formatted_future_date}")
    return future_date

def main():
    print("Datetime Module Exploration")
    print("-------------------------")
    
    # Part 1: Display current date and time
    print("\nPart 1: Current Date and Time")
    current_date = display_current_datetime()
    
    # Part 2: Calculate future date
    print("\nPart 2: Future Date Calculation")
    try:
        days = int(input("Enter the number of days to add to current date: "))
        future_date = calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter a valid integer number of days.")

if __name__ == "__main__":
    main()