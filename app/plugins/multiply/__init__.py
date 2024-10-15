from app.commands import Command

class MultiplyCommand(Command):
    def execute(self, *args):
        try:
            # Convert all arguments to floats and perform multiplication
            numbers = [float(arg) for arg in args]
            result = 1
            for num in numbers:
                result *= num
            return result
        except ValueError:
            return "Error: Please provide valid numbers."