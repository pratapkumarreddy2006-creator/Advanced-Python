def power(b, e):
    """Calculate b raised to the power of e.
    
    Args:
        b: Base (int or float)
        e: Exponent (int)
    
    Returns:
        b^e
    
    Raises:
        TypeError: If b or e is not numeric/int
        ValueError: If e is negative and b is 0
    """
    if not isinstance(e, int):
        raise TypeError(f"Exponent must be an integer, got {type(e).__name__}")
    
    if not isinstance(b, (int, float)):
        raise TypeError(f"Base must be numeric, got {type(b).__name__}")
    
    if e < 0:
        if b == 0:
            raise ValueError("Cannot raise 0 to a negative power")
        return 1 / power(b, -e)
    
    result = 1
    for _ in range(e):
        result *= b
    return result


if __name__ == "__main__":
    print(power(2, 3))
    print(power(2, 0))
    print(power(2, -2))