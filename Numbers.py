def read_numbers():
    """
    Read a list of numbers.
    """
    try:
        numbers = input("Enter a number separated by spaces: ").split()
        numbers = [float(num) for num in numbers]
        return numbers
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return []

def calculate_sum(numbers):
    """
    Calculate the sum of a list of numbers.
    """
    return sum(numbers)

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_maximum(numbers):
    """
    Find the maximum value in a list of numbers.
    """
    if not numbers:
        return None
    return max(numbers)

def find_minimum(numbers):
    """
    Find the minimum value in a list of numbers.
    """
    if not numbers:
        return None
    return min(numbers)

def filter_even_numbers(numbers):
    """
    Filter out even numbers from a list of numbers.
    """
    return [num for num in numbers if num % 2 != 0]

def main():
    numbers = read_numbers()

    if numbers:
        print(f"Numbers: {numbers}")
        print(f"Sum: {calculate_sum(numbers)}")
        print(f"Average: {calculate_average(numbers)}")
        print(f"Maximum: {find_maximum(numbers)}")
        print(f"Minimum: {find_minimum(numbers)}")

        even_numbers = filter_even_numbers(numbers)
        print(f"Filtered Even Numbers: {even_numbers}")

if __name__ == "__main__":
    main()
