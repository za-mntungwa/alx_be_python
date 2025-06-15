
def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling division by zero and type errors."""
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        return f"The result of the division is {numerator / denominator}"
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
