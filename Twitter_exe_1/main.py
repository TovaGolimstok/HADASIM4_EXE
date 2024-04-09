from Implementation.rectangle import option_1_rectangle
from Implementation.triangular import option_2_triangular
from issues.menu import Menu
from issues.rectangle import Rectangle
from issues.triangular import Triangular
from issues.user import User


def main():
    while True:
        Menu.display()
        choice = User.get_user_choice()

        if choice == '1':
            height, width = User.get_parameters()
            rectangle = Rectangle(height, width)
            option_1_rectangle(rectangle)
        elif choice == '2':
            height, width = User.get_parameters()
            triangular = Triangular(height, width)
            option_2_triangular(triangular)
        elif choice == '3':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
