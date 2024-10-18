import pytest
from app import App
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'menu' command."""
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

# Add tests for the calculator commands
def test_app_add_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'add' command."""
    inputs = iter(['add 5 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    out, err = capfd.readouterr()
    assert "Result: 8" in out, "The add command did not work as expected"

def test_app_subtract_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'subtract' command."""
    inputs = iter(['subtract 10 4', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    out, err = capfd.readouterr()
    assert "Result: 6" in out, "The subtract command did not work as expected"

def test_app_multiply_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'multiply' command."""
    inputs = iter(['multiply 3 4', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    out, err = capfd.readouterr()
    assert "Result: 12" in out, "The multiply command did not work as expected"

def test_app_divide_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'divide' command."""
    inputs = iter(['divide 20 4', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    out, err = capfd.readouterr()
    assert "Result: 5" in out, "The divide command did not work as expected"

def test_app_divide_by_zero(capfd, monkeypatch):
    """Test that the REPL correctly handles divide by zero errors."""
    inputs = iter(['divide 10 0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    out, err = capfd.readouterr()
    assert "Error: Division by zero is not allowed" in out, "The divide command did not handle divide by zero as expected"