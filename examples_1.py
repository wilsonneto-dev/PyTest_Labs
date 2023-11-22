def add(n1: int, n2: int) -> int:
    if n1 < 0 or n2 < 0:
        raise ValueError("Only positive integers are allowed")
    return n1 + n2

