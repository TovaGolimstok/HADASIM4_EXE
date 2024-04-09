from Implementation import user_display
from issues.menu import Menu
from issues.user import User


def option_2_triangular(triangular):
    while True:
        Menu.display_triangular_options()
        choice = User.get_user_choice()
        if choice == '1':
            print(f"The perimeter of the triangle is: {triangular.perimeter()}")
            break
        elif choice == '2':
            if triangular.can_print_triangular():
                user_display.triangle_display(int(triangular.height), int(triangular.width))
            else:
                print("No option to print the triangle!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")
