class User:
    @staticmethod
    def get_parameters():
        height = User.get_height_from_user()
        width = User.get_width_from_user()
        return height, width

    @staticmethod
    def get_user_choice():
        choice = input("Enter your choice: ")
        return choice

    @staticmethod
    def get_height_from_user():
        while True:
            height_str = input("Insert height (min-2 cm): ")
            try:
                height = int(height_str)
                if height >= 2:
                    return height
                else:
                    print("Height must be at least 2 cm.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    @staticmethod
    def get_width_from_user():
        while True:
            width = input("Insert width: ")
            try:
                width = int(width)
                if width > 0:
                    return width
            except ValueError:
                print("Invalid input. Please enter a valid number.")


