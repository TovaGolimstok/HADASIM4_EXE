# def display_menu():
#     """Display the main menu."""
#     print("Select an option:")
#     print("1. Rectangle")
#     print("2. Triangular")
#     print("3. Exit")
#
#
# def display_triangular_options():
#     """Display options for triangular shapes."""
#     print("What do you want to do?")
#     print("1. Calculate the perimeter of the triangle")
#     print("2. Print the triangle")


def count_odd_numbers(number):
    """Count the number of odd numbers up to a given number."""
    count = 0
    for num in range(2, number):
        if num % 2 != 0:
            count += 1
    return count


def calculate_space_between_two_nums(num1, num2):
    """Calculate the space between two numbers."""
    if num1 % 2 == 0:
        raise ValueError("num1 must be an odd number")
    else:
        return (num1 - num2) // 2


def calculate_repeater_lines(num, amount):
    """Calculate the number of lines to repeat in the triangle."""
    if amount == 0:
        return 0, 0  # Return 0 for both values if amount is zero to avoid division by zero
    else:
        num_of_same_lines = num // amount
        num_of_same_lines_at_first_time = num_of_same_lines + num % amount
        return num_of_same_lines, num_of_same_lines_at_first_time


def triangle_display(height, width):
    """Display a triangular shape."""
    num_of_lines = height - 2
    amount_of_odd_numbers = count_odd_numbers(width - 1)
    num_of_same_lines, num_of_same_lines_at_first_time = calculate_repeater_lines(int(num_of_lines),
                                                                                  int(amount_of_odd_numbers))
    current_line = 0
    print("Your triangle looks:")
    print(' ' * calculate_space_between_two_nums(width, 1) + '*')
    num_of_star = 1
    while current_line < num_of_lines:
        num_of_star = num_of_star + 2
        num_of_space = calculate_space_between_two_nums(int(width), int(num_of_star))
        if current_line == 0:
            count_of_same_lines = num_of_same_lines_at_first_time
        else:
            count_of_same_lines = num_of_same_lines
        while count_of_same_lines > 0:
            print(' ' * num_of_space + '*' * num_of_star)
            count_of_same_lines -= 1
            current_line += 1
    print('*' * width)
