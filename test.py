# Function to calculate the average of a list
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# Example usage
if __name__ == "__main__":
    # Input: List of numbers
    numbers = [10, 20, 30, 40, 50]
    
    # Calculate the average
    average = calculate_average(numbers)
    
    # Output the average
    print(f"The average is: {average}")
