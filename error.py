def add_numbers(a, b):
    result = a + b
    return result

def subtract_numbers(a, b):
    result = a - b
    return result

# Example of intentional errors
def divide_numbers(a, b):
    return a / b

def multiply_numbers(a, b):
    return a * b

# Calling the functions
print(add_numbers(5, 'three'))  # Error: Mixing integer with string
print(subtract_numbers(10, 'five'))  # Error: Mixing integer with string
print(divide_numbers(10, 0))  # Error: Division by zero
