

def check_unique_numbers(numbers):
    if len(numbers) == len(set(numbers)):
        return True
    else:
        return False

# Example usage:
sequence = [1, 2, 3, 4, 5]
result = check_unique_numbers(sequence)
print(result)  # Output: True

sequence = [1, 2, 3, 3, 4, 5]
result = check_unique_numbers(sequence)
print(result)  # Output: False



