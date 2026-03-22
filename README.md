# Mystery Module

This module provides a function to compute the roots of a quadratic equation:

ax^2 + bx + c = 0

## Function

### fn_x(a, b, c)

Returns:
- Tuple of two real roots if discriminant >= 0
- None if no real roots exist

## Example

```python
from mystery_module import fn_x

print(fn_x(1, -3, 2))  # (2.0, 1.0)