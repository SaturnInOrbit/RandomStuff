from typing import List, Tuple

def count_odd_and_even(numbers: List[int]) -> Tuple[int, int]:
    odd_count = 0
    even_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return odd_count, even_count

# Example usage
numbers = [1, 2, 3, 4, 5, 6]
result = count_odd_and_even(numbers)
print(f"Odd numbers: {result[0]}, Even numbers: {result[1]}")

from typing import List

def find_largest(numbers: List[int]) -> int:
    if not numbers:  # Check if the list is empty
        raise ValueError("The list is empty!")

    largest = numbers[0]  # Assume the first number is the largest
    for num in numbers:
        if num > largest:  # Compare each number with the current largest
            largest = num

    return largest

# Example usage
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
largest_number = find_largest(numbers)
print(f"The largest number is: {largest_number}")

