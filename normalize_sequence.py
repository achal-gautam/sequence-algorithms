def normalize_sequence(numbers):
    """
    Adjusts a sequence so that each element equals its 1-based index position.
    When a mismatch is found, it calculates the gap and adjusts all remaining elements.

    Args:
        numbers: List of integers to normalize
    """
    for current_index in range(len(numbers)):
        expected_value = current_index + 1  # 1-based indexing
        actual_value = numbers[current_index]

        if expected_value != actual_value:
            remaining_length = len(numbers[current_index:])
            adjustment_gap = actual_value - expected_value

            # Apply the gap adjustment to all remaining elements
            for offset in range(remaining_length):
                numbers[current_index + offset] -= adjustment_gap

# Example usage
test_array = [3, 4, 5, 6, 7]
print("Original:", test_array)
normalize_sequence(test_array)
print("Normalized:", test_array)  # Output: [1, 2, 3, 4, 5]