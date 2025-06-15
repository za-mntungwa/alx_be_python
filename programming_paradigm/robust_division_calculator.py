
def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling division by zero and type errors."""
    numerator = float(numerator)
    denominator = float(denominator)
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except ValueError:
        print("Error: Please enter numeric values only.")
        return None
