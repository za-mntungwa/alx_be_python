
def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling division by zero and type errors."""
    numerator = float(numerator)
    denominator = float(denominator)
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: Both numerator and denominator must be numbers.")
        return None
