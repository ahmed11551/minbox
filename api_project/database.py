import sqlite3
from typing import Dict, List
import json

class Database:
    def __init__(self, db_name: str = "products.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()
    
    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                title TEXT,
                description TEXT,
                price REAL,
                discount_percentage REAL,
                rating REAL,
                stock INTEGER,
                brand TEXT,
                category TEXT,
                thumbnail TEXT,
                images TEXT
            )
        """)
        self.conn.commit()
    
    def save_product(self, product: Dict):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO products 
            (id, title, description, price, discount_percentage, rating, stock, brand, category, thumbnail, images)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            product["id"],
            product["title"],
            product["description"],
            product["price"],
            product["discountPercentage"],
            product["rating"],
            product["stock"],
            product["brand"],
            product["category"],
            product["thumbnail"],
            json.dumps(product["images"])
        ))
        self.conn.commit()
    
    def get_all_products(self) -> List[Dict]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        return [{
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "price": row[3],
            "discountPercentage": row[4],
            "rating": row[5],
            "stock": row[6],
            "brand": row[7],
            "category": row[8],
            "thumbnail": row[9],
            "images": json.loads(row[10])
        } for row in rows]
    
    def close(self):
        self.conn.close() 