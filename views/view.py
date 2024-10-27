class View:
    def display_message(self, message):
        """Display a message to the user"""
        print(message)

    def get_input(self, prompt):
        """Ask the user for an input with a prompt"""
        return input(prompt)

    def get_choice(self, choices):
        """Ask the user for an input with a list of choices"""
        for index, choice in enumerate(choices):
            print(f"{index+1}. {choice}")

        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice in range(1, len(choices)+1):
                    return choice
            except ValueError:
                print("Invalid choice. Please try again.")

