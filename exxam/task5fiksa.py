# Function to get integer input from the user
def get_input(prompt: str) -> int:
    while True:
        user_input = input(prompt)
        if user_input == "":  # If the input is empty (user presses Enter), return None
            return None
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Main function to categorize and display numbers
def main() -> None:
    positive_numbers = []
    zeros = []
    negative_numbers = []

 # Loop to continuously get input from the user until an empty input is provided
    while True:
        user_input = get_input("Enter an integer (blank to quit): ")
        if user_input is None:
            break
        elif user_input > 0:
            positive_numbers.append(user_input)
        elif user_input == 0:
            zeros.append(user_input)
        else:
            negative_numbers.append(user_input)

  # Combine all lists into one list
    all_numbers = positive_numbers + zeros + negative_numbers

 # Print all numbers
    print("The numbers were:")
    print(" ".join(map(str, all_numbers)))


if __name__ == "__main__":
    main()  # Call the main function if the script is run directly
