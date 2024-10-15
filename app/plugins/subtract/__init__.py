from app.commands import Command

class SubtractCommand(Command):
    def execute(self, *args):
        try:
            # Convert arguments to floats and perform subtraction
            numbers = [float(arg) for arg in args]
            if len(numbers) < 2:
                return "Error: Subtraction requires at least two numbers."
            result = numbers[0]
            for num in numbers[1:]:
                result -= num
            return result
        except ValueError:
            return "Error: Please provide valid numbers."