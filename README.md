# Sequence Normalizer

This algorithm adjusts sequences so each element equals its 1-based index position.

## Usage
```python
from sequence_normalizer import normalize_sequence

numbers = [3, 4, 5, 6, 7]
normalize_sequence(numbers)
print(numbers)  # [1, 2, 3, 4, 5]
