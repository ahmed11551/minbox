# Shapes Library

A Python library for calculating areas of different shapes.

## Features

- Calculate area of a circle
- Calculate area of a triangle
- Check if a triangle is right-angled
- Easy to extend with new shapes
- Type-safe area calculation

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from shapes.shapes import Circle, Triangle, calculate_area

# Calculate circle area
circle = Circle(1)
print(circle.area())  # 3.141592653589793

# Calculate triangle area
triangle = Triangle(3, 4, 5)
print(triangle.area())  # 6.0

# Check if triangle is right-angled
print(triangle.is_right_angled())  # True

# Calculate area without knowing shape type
print(calculate_area(circle))  # 3.141592653589793
print(calculate_area(triangle))  # 6.0
```

## Running Tests

```bash
python -m unittest discover tests
```

## Adding New Shapes

To add a new shape, create a new class that inherits from `Shape` and implements the `area()` method:

```python
from shapes.shapes import Shape

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height
```
