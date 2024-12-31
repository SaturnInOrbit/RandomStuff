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
