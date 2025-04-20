from products_client import ProductsClient
from database import Database

def main():
    # Инициализация клиентов
    products_client = ProductsClient()
    db = Database()
    
    try:
        # Получение всех iPhone
        iphones = products_client.get_iphones()
        print(f"Найдено {len(iphones)} iPhone")
        
        # Сохранение в базу данных
        for iphone in iphones:
            db.save_product(iphone)
            print(f"Сохранен iPhone: {iphone['title']}")
        
        # Получение всех сохраненных продуктов
        saved_products = db.get_all_products()
        print(f"\nВсего сохранено продуктов: {len(saved_products)}")
        
    finally:
        db.close()

if __name__ == "__main__":
    main() 