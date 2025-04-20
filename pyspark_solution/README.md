# PySpark Solution for Products and Categories

This solution demonstrates how to work with products and categories in PySpark, showing how to:
- Join multiple DataFrames
- Handle products without categories
- Combine results using union operations

## Problem Description

Given three DataFrames:
1. Products DataFrame (with product_id and product_name)
2. Categories DataFrame (with category_id and category_name)
3. Product-Category relationships DataFrame (with product_id and category_id)

The task is to return all pairs of "Product Name - Category Name" and names of all products that don't have any categories.

## Solution

The solution is implemented in `products_categories.py` and includes:
- A main function that demonstrates the solution with sample data
- A reusable function `get_products_with_categories` that can be used with any DataFrames following the required schema

## Usage

```python
from products_categories import get_products_with_categories

# Assuming you have your DataFrames ready
result = get_products_with_categories(products_df, categories_df, product_category_df)
result.show()
```

## Example Output

```
+------------+------------+
|product_name|category_name|
+------------+------------+
|   Product A|  Category 1|
|   Product A|  Category 2|
|   Product B|  Category 2|
|   Product C|  Category 3|
|   Product D|        null|
+------------+------------+
```

## Requirements

- PySpark
- Python 3.x 