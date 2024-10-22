import random

# Function to generate a random list of numbers within a specified range
def generate_random_list(length: int = 10, start: int = 1, end: int = 50):
    return [random.randint(start, end) for _ in range(length)]

# Function to substitute numbers in the list with their squares if they are divisible by 5
def substitute(numbers):
    for i, num in enumerate(numbers):
        if num % 5 == 0:
            numbers[i] = num ** 2

def main():
    numbers = generate_random_list()

    print("Before substitution, the list is:", numbers)

    substitute(numbers)

    print("After substitution, the list is:", numbers)

if __name__ == "__main__":
    main() # Executes the main function if the script is run directly
