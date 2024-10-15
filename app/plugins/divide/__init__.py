from app.commands import Command

class DivideCommand(Command):
    def execute(self, *args):
        try:
            # Convert arguments to floats and perform division
            numbers = [float(arg) for arg in args]
            if len(numbers) < 2:
                return "Error: Division requires at least two numbers."
            result = numbers[0]
            for num in numbers[1:]:
                if num == 0:
                    return "Error: Division by zero is not allowed."
                result /= num
            return result
        except ValueError:
            return "Error: Please provide valid numbers."