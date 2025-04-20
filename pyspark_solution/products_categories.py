from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, count, lit

def get_products_with_categories(products_df, categories_df, product_category_df):
    """
    Возвращает датафрейм с парами "Имя продукта – Имя категории" и продуктами без категорий.
    
    Args:
        products_df: Датафрейм с продуктами (должен содержать колонки 'product_id' и 'product_name')
        categories_df: Датафрейм с категориями (должен содержать колонки 'category_id' и 'category_name')
        product_category_df: Датафрейм со связями продуктов и категорий (должен содержать колонки 'product_id' и 'category_id')
    
    Returns:
        DataFrame с колонками 'product_name' и 'category_name'
    """
    # Соединяем продукты с их категориями
    products_with_categories = (
        products_df
        .join(product_category_df, 'product_id', 'left')
        .join(categories_df, 'category_id', 'left')
        .select('product_name', 'category_name')
    )
    
    # Добавляем продукты без категорий
    products_without_categories = (
        products_df
        .join(product_category_df, 'product_id', 'left_anti')
        .select('product_name')
        .withColumn('category_name', lit(None))
    )
    
    # Объединяем результаты
    result = products_with_categories.union(products_without_categories)
    
    return result

def main():
    # Создаем SparkSession
    spark = SparkSession.builder.appName("ProductsCategories").getOrCreate()

    # Пример данных
    products_data = [
        (1, "Product A"),
        (2, "Product B"),
        (3, "Product C"),
        (4, "Product D")
    ]

    categories_data = [
        (1, "Category 1"),
        (2, "Category 2"),
        (3, "Category 3")
    ]

    product_category_data = [
        (1, 1),  # Product A -> Category 1
        (1, 2),  # Product A -> Category 2
        (2, 2),  # Product B -> Category 2
        (3, 3)   # Product C -> Category 3
    ]

    # Создаем датафреймы
    products_df = spark.createDataFrame(products_data, ["product_id", "product_name"])
    categories_df = spark.createDataFrame(categories_data, ["category_id", "category_name"])
    product_category_df = spark.createDataFrame(product_category_data, ["product_id", "category_id"])

    # Получаем результат
    result = get_products_with_categories(products_df, categories_df, product_category_df)
    result.show()

if __name__ == "__main__":
    main() 