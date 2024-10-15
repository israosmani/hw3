from app.commands import Command

class AddCommand(Command):
    def execute(self, *args):
        try:
            
            numbers = [float(arg) for arg in args]
            return sum(numbers)
        except ValueError:
            return "Error: Please provide valid numbers."