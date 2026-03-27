def insert_and_maintain_sequence(sequence, insertion_index):
    """
    Insert a number at a specified index and reorder the list to maintain 
    consecutive numbering from 1 to n+1.

    This function takes an ordered list (1 to n) and inserts a number at the 
    specified index, then adjusts all subsequent numbers to maintain a 
    consecutive sequence from 1 to n+1.

    Args:
        sequence (list): A list of consecutive integers starting from 1
        insertion_index (int): The index where to insert the new number

    Returns:
        list: The modified list with consecutive numbering from 1 to n+1

    Example:
        >>> insert_and_maintain_sequence([1, 2, 3, 4, 5], 2)
        [1, 2, 2, 4, 5, 6]
    """
    # Insert the index value at the specified position
    sequence.insert(insertion_index, insertion_index)

    # Increment all values from the insertion point forward to maintain sequence
    for i in range(insertion_index + 1, len(sequence)):
        sequence[i] += 1

    return sequence


if __name__ == "__main__":
    # Example usage
    test_sequence = [1, 2, 3, 4, 5]
    print("Original sequence:", test_sequence)

    # Test insertions at different positions
    for idx in [0, 1, 2, 3, 5]:
        test_copy = test_sequence.copy()
        result = insert_and_maintain_sequence(test_copy, idx)
        print(f"Insert at index {idx}: {result}")
