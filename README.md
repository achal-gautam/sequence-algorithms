# Sequence Normalizer

This algorithm adjusts sequences so each element equals its 1-based index position.

## Usage
```python
from sequence_normalizer import normalize_sequence

numbers = [3, 4, 5, 6, 7]
normalize_sequence(numbers)
print(numbers)  # [1, 2, 3, 4, 5]

# Sequence Inserter

A Python utility for inserting numbers into ordered sequences while maintaining consecutive numbering.

## Description

This function takes an ordered list of consecutive integers (1 to n) and inserts a number at a specified index, then adjusts all subsequent numbers to maintain proper sequential ordering.

## Features

- Maintains consecutive numbering after insertion
- Works with any insertion index within the list bounds
- Simple and efficient implementation
- Well-documented with examples

## Usage

```python
from sequence_inserter import insert_and_maintain_sequence

# Create an ordered sequence
my_sequence = [1, 2, 3, 4, 5]

# Insert at index 2
result = insert_and_maintain_sequence(my_sequence, 2)
print(result)  # Output: [1, 2, 2, 4, 5, 6]
